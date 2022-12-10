from typing import List


def day25_parser(s: List[str]) -> str:
    return s[0]


class Cucumber:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.c_type = type

    def is_east(self):
        return self.c_type == ">"

    def is_south(self):
        return self.c_type == "v"

    def next_point(self, height, width) -> (int, int):
        if self.is_east():
            right = self.x + 1 if self.x < width - 1 else 0
            return right, self.y

        down = self.y + 1 if self.y < height - 1 else 0
        return self.x, down

    def go(self, next_x, next_y):
        self.x = next_x
        self.y = next_y


def simulate_cucumbers(map: List[str]) -> int:
    height = len(map)
    width = len(map[0])

    cucumbers = []
    for i in range(height):
        for j in range(width):
            cell = map[i][j]
            if cell != ".":
                cucumbers.append(Cucumber(x=j, y=i, type=cell))

    right_going = [c for c in cucumbers if c.is_east()]
    down_going = [c for c in cucumbers if c.is_south()]

    step = 0

    while True:
        print(f"After {step} steps:")
        print_map(get_map(map, cucumbers))

        step += 1
        moved = False

        # Go right
        all_occupied = {(c.x, c.y) for c in cucumbers}

        for cucumber in right_going:
            next_x, next_y = cucumber.next_point(height, width)
            if (next_x, next_y) not in all_occupied:
                moved = True
                cucumber.go(next_x, next_y)

        # Go Down
        all_occupied = {(c.x, c.y) for c in cucumbers}

        for cucumber in down_going:
            next_x, next_y = cucumber.next_point(height, width)
            if (next_x, next_y) not in all_occupied:
                moved = True
                cucumber.go(next_x, next_y)

        if not moved:
            # Deadlock!
            break

    return step


def simulate_cucumbers_map(map: List[str]) -> int:
    height = len(map)
    width = len(map[0])

    print_map(map)

    # Go right
    new_map = []
    for i in range(height):
        row = map[i]
        new_row = "".join('.' for j in range(width))
        for j in range(width):
            if row[j] != ">":
                continue

            right = j + 1 if j < width - 1 else 0
            on_your_right = row[right] != "."
            if on_your_right:
                new_row = new_row[:j] + ">" + new_row[j + 1:]
            else:
                new_row = new_row[:right] + ">" + new_row[right + 1:]
        new_map.append(new_row)

    print_map(new_map)

    return 5


def get_map(original_map: List[str], cucumbers: List[Cucumber]):
    height = len(original_map)
    width = len(original_map[0])

    map = ["".join('.' for j in range(width)) for i in range(height)]

    for cucumber in cucumbers:
        old_row = map[cucumber.y]
        new_row = old_row[:cucumber.x] + cucumber.c_type + old_row[cucumber.x + 1:]
        map[cucumber.y] = new_row

    return map


def print_map(map: List[str]):
    for row in map:
        print(row)
    print()
