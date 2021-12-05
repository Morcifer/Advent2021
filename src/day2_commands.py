from typing import List


class Command:
    direction: str
    units: int

    up = "up"
    down = "down"
    forward = "forward"

    def __init__(self, d, u):
        self.direction = d
        self.units = u

    def move(self, x: int, y: int) -> (int, int):
        if self.direction == self.up:
            return x, y - self.units
        if self.direction == self.down:
            return x, y + self.units
        if self.direction == self.forward:
            return x + self.units, y

    def move_with_aim(self, x: int, y: int, aim: int) -> (int, int, int):
        if self.direction == self.up:
            return x, y, aim - self.units
        if self.direction == self.down:
            return x, y, aim + self.units
        if self.direction == self.forward:
            return x + self.units, y + aim * self.units, aim


def day2_parser(s: List[str]) -> Command:
    return Command(s[0], int(s[1]))


def calculate_final_location(commands: List[Command], move_method: str) -> (int, int):
    x, y, aim = 0, 0, 0
    for command in commands:
        if move_method == "move":
            x, y = command.move(x, y)
        elif move_method == "move_with_aim":
            x, y, aim = command.move_with_aim(x, y, aim)
    return x, y
