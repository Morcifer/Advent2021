from typing import List, Union, Tuple


def day13_parser(s: List[str]) -> Union[Tuple[int, int], Tuple[str, int]]:
    if len(s) == 1 and s[0] == "":
        return None

    if len(s) == 3:
        t, space = s[2].split("=")
        return t, int(space)

    # print(s)
    x, y = s[0].split(",")
    return int(x), int(y)


def split_data_to_points_and_cuts(
        data: List[Union[Tuple[int, int], Tuple[str, int]]]
) -> (List[Tuple[int, int]], List[Tuple[str, int]]):
    all_points = [point for point in data if point is not None and type(point[0]) == int]
    all_cuts = [cut for cut in data if cut is not None and type(cut[0]) == str]
    return all_points, all_cuts


def apply_cuts(points: List[Tuple[int, int]], cuts: List[Tuple[str, int]]) -> List[Tuple[int, int]]:
    for cut in cuts:
        points = apply_cut(points, cut)

    return points


def apply_cut(points: List[Tuple[int, int]], cut: (str, int)) -> List[Tuple[int, int]]:
    new_points = []
    for point in points:
        if cut[0] == "x":
            if point[0] < cut[1]:
                new_points.append(point)
            else:
                new_points.append((2 * cut[1] - point[0], point[1]))
        else:
            if point[1] < cut[1]:
                new_points.append(point)
            else:
                new_points.append((point[0], 2 * cut[1] - point[1]))
        # print(new_points[-1])
    return list(set(new_points))


def show_result(points: List[Tuple[int, int]]):
    size_x = max(p[0] for p in points)
    size_y = max(p[1] for p in points)
    result = ["".join(["." for _ in range(size_x+1)]) for _ in range(size_y+1)]

    for point in points:
        # print(point)
        if point[1] >= len(result):
            print("gah")
        row = result[point[1]]
        new_row = row[:point[0]] + "#" + row[point[0]+1:]
        result[point[1]] = new_row

    for y in range(size_y+1):
        print(result[y])
