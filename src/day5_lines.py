from collections import Counter
from typing import List


class Grid:
    points: List[List[int]]

    def __init__(self):
        self.points = [[0 for _ in range(1000)]
                       for _ in range(1000)]

    def increase_risk(self, i: int, j: int):
        self.points[i][j] += 1

    def get_max_risk_count(self):
        counter = Counter([v for row in self.points for v in row])
        max_risk = max(counter.keys())
        return counter[max_risk]

    def get_high_risk_count(self):
        counter = Counter([v for row in self.points for v in row])
        return sum(value for key, value in counter.items() if key >= 2)


class Line:
    point_1: (int, int)
    point_2: (int, int)

    def __init__(self, p1, p2):
        self.point_1 = p1
        self.point_2 = p2

    def get_range(self, number_1: int, number_2: int) -> List[int]:
        return list(
            range(number_1, number_2 + 1)
            if number_2 > number_1
            else range(number_1, number_2 - 1, -1)
        )

    def apply_line(self, grid: Grid, filter_diagonal: bool) -> None:
        x_range = self.get_range(self.point_1[0], self.point_2[0])
        y_range = self.get_range(self.point_1[1], self.point_2[1])

        if self.point_1[0] == self.point_2[0]:
            for j in y_range:
                grid.increase_risk(self.point_1[0], j)
        elif self.point_1[1] == self.point_2[1]:
            for i in x_range:
                grid.increase_risk(i, self.point_1[1])
        else:
            if filter_diagonal:
                return
            else:
                for i, j in zip(x_range, y_range):
                    grid.increase_risk(i, j)


def day5_parser(s: List[str]) -> Line:
    p1_str = s[0].split(",")
    p2_str = s[2].split(",")
    p1 = (int(p1_str[0]), int(p1_str[1]))
    p2 = (int(p2_str[0]), int(p2_str[1]))
    return Line(p1, p2)


def calculate_final_grid(data: List[Line], filter_diagonal: bool) -> Grid:
    grid = Grid()
    for line in data:
        line.apply_line(grid, filter_diagonal)

    return grid
