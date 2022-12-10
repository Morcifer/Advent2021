import itertools
from typing import List, Tuple, Set

import numpy as np

from src.utilities import load_data


class Box:
    # Describes an *on* box
    x_min: int
    x_max: int
    y_min: int
    y_max: int
    z_min: int
    z_max: int

    def __init__(self, x_min, x_max, y_min, y_max, z_min, z_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.z_min = z_min
        self.z_max = z_max

    @staticmethod
    def split_single_axis(
            this_min: int,
            this_max: int,
            other_min: int,
            other_max: int,
            status: str
    ) -> List[Tuple[int, int]]:
        # No intersection
        if this_min > other_max or this_max < other_min:
            return [(this_min, this_max)]

        # Other fully within this
        if this_min < other_min and other_max < this_max:
            if status == "on":
                return [(this_min, this_max)]
            else:
                return [
                    (this_min, other_min - 1),
                    (other_max + 1, this_max)
                ]

        # This fully within other
        if other_min < this_min and this_max < other_max:
            if status == "on":
                return [(other_min, other_max)]
            else:
                return []

        # Partial overlap
        if status == "on":
            new_min = min(this_min, other_min)
            new_max = max(this_max, other_max)
            return [(new_min, new_max)]

        if other_min <= this_min and other_max <= this_max:
            return [(other_max + 1, this_max)]
        else:
            return [(this_min, other_min - 1)]

    def split_for_other_box(self, other: 'Box', status: str) -> List['Box']:
        x_split = self.split_single_axis(self.x_min, self.x_max, other.x_min, other.x_max, status)
        y_split = self.split_single_axis(self.y_min, self.y_max, other.y_min, other.y_max, status)
        z_split = self.split_single_axis(self.z_min, self.z_max, other.z_min, other.z_max, status)
        sub_boxes = [x_split, y_split, z_split]

        this_split = [
            Box(box_x[0], box_x[1], box_y[0], box_y[1], box_z[0], box_z[1])
            for box_x, box_y, box_z in itertools.product(*sub_boxes)
        ]

        if status == "on" and len(this_split) == 1 and this_split[0] != self and this_split[0] != other:
            return this_split + [other]

        return this_split

    def count_on(self):
        return (self.x_max - self.x_min + 1) * (self.y_max - self.y_min + 1) * (self.z_max - self.z_min + 1)

    def __hash__(self):
        return hash(str(self.x_min) + str(self.x_max) +
                    str(self.y_min) + str(self.y_max) +
                    str(self.z_min) + str(self.z_max))

    def __eq__(self, other):
        return (self.x_min == other.x_min and self.x_max == other.x_max and
                self.y_min == other.y_min and self.y_max == other.y_max and
                self.z_min == other.z_min and self.z_max == other.z_max)

    def __repr__(self):
        return f"{self.x_min}..{self.x_max}, {self.y_min}..{self.y_max}, {self.z_min}..{self.z_max}"


class Step:
    state: str
    box: Box

    def __init__(self, s, x_min, x_max, y_min, y_max, z_min, z_max):
        self.state = s
        self.box = Box(x_min, x_max, y_min, y_max, z_min, z_max)

    def on(self) -> bool:
        return self.state == "on"

    def off(self) -> bool:
        return self.state == "off"


def day22_parser(s: List[str]) -> Step:
    state = s[0]
    positions = s[1].split(",")
    x_min, x_max = positions[0][2:].split("..")
    y_min, y_max = positions[1][2:].split("..")
    z_min, z_max = positions[2][2:].split("..")

    return Step(
        state,
        int(x_min), int(x_max),
        int(y_min), int(y_max),
        int(z_min), int(z_max))


def reboot(steps: List[Step]):
    reactor = np.zeros((101, 101, 101))

    for step in steps:
        if step.box.x_max < -50 and step.box.x_min > 50:
            continue
        if step.box.y_max < -50 and step.box.y_min > 50:
            continue
        if step.box.z_max < -50 and step.box.z_min > 50:
            continue
        x_min = max(step.box.x_min, -50) + 50
        x_max = min(step.box.x_max, 50) + 50
        y_min = max(step.box.y_min, -50) + 50
        y_max = min(step.box.y_max, 50) + 50
        z_min = max(step.box.z_min, -50) + 50
        z_max = min(step.box.z_max, 50) + 50

        reactor[x_min:x_max+1, y_min:y_max+1, z_min:z_max+1] = (1 if step.on() else 0)
        # print(f"turning {step.state} meant {np.sum(reactor)} are on")
        # print("g")

    return int(np.sum(reactor))


def reboot_all(steps: List[Step]) -> int:
    all_xs = [s.box.x_min for s in steps] + [s.box.x_max for s in steps]
    all_ys = [s.box.y_min for s in steps] + [s.box.y_max for s in steps]
    all_zs = [s.box.z_min for s in steps] + [s.box.z_max for s in steps]

    all_xs = sorted(list(set(list(all_xs) + [x - 1 for x in all_xs] + [x + 1 for x in all_xs])))
    all_ys = sorted(list(set(list(all_ys) + [y - 1 for y in all_ys] + [y + 1 for y in all_ys])))
    all_zs = sorted(list(set(list(all_zs) + [z - 1 for z in all_zs] + [z + 1 for z in all_zs])))

    x_mapping = {x: i for i, x in enumerate(all_xs)}
    y_mapping = {y: i for i, y in enumerate(all_ys)}
    z_mapping = {z: i for i, z in enumerate(all_zs)}

    reactor = np.zeros((len(all_xs) + 1, len(all_ys) + 1, len(all_zs) + 1), dtype=np.bool8)

    for i, step in enumerate(steps):
        print(f"Step {i} out of {len(steps) - 1}")
        x_min_spot = x_mapping[step.box.x_min]
        x_max_spot = x_mapping[step.box.x_max]
        y_min_spot = y_mapping[step.box.y_min]
        y_max_spot = y_mapping[step.box.y_max]
        z_min_spot = z_mapping[step.box.z_min]
        z_max_spot = z_mapping[step.box.z_max]

        reactor[x_min_spot:x_max_spot + 1, y_min_spot:y_max_spot + 1, z_min_spot:z_max_spot + 1] = (1 if step.on() else 0)
        # print(f"turning {step.state} meant {np.sum(reactor)} are on")
        # print("g")

    diff_x = np.array(all_xs[1:], dtype=np.longlong) - np.array(all_xs[:-1], dtype=np.longlong)
    diff_y = np.array(all_ys[1:], dtype=np.longlong) - np.array(all_ys[:-1], dtype=np.longlong)
    diff_z = np.array(all_zs[1:], dtype=np.longlong) - np.array(all_zs[:-1], dtype=np.longlong)

    y_matrix, z_matrix = np.ix_(diff_y, diff_z)
    temp = y_matrix * z_matrix

    result = 0
    for i, dx in enumerate(diff_x):
        print(f"At {i+1} out of {len(diff_x)}")
        temp_temp = np.multiply(temp, reactor[i+1, 1:-1, 1:-1])
        result += dx * np.sum(temp_temp)

    return result


if __name__ == "__main__":
    xs = np.array([x*x for x in range(5)])
    diff_x = xs[1:] - xs[:-1]

    ys = np.array([y*y for y in range(10)])
    diff_y = ys[1:] - ys[:-1]

    zs = np.array([z*z for z in range(15)])
    diff_z = zs[1:] - zs[:-1]

    # matrix_1 = np.outer(diff_y, diff_x)
    # matrix_2 = np.outer(ys, xs)

    x_matrix, y_matrix, z_matrix = np.ix_(diff_x, diff_y, diff_z)
    temp = x_matrix * y_matrix * z_matrix


    print(temp.shape)