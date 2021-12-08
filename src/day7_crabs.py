from collections import Counter
from typing import List


def day7_parser(s: List[str]) -> List[int]:
    all_positions = s[0].split(",")
    return [int(x) for x in all_positions]


def find_best_location_and_fuel(positions: List[int], linear: bool) -> (int, int):
    counter = Counter(positions)

    best_location = 0
    best_fuel = len(positions) * (max(counter.keys()) ** 2)

    for this_location in range(min(counter.keys()), max(counter.keys()) + 1):
        fuel_calculator = linear_fuel if linear else non_linear_fuel
        this_fuel = sum(v * fuel_calculator(p, this_location) for p, v in counter.items())
        # print(f"location {this_location} requires {this_fuel} fuel")
        if this_fuel < best_fuel:
            best_location = this_location
            best_fuel = this_fuel
            # print(f"better location {best_location} requires {best_fuel} fuel")

    return best_location, best_fuel


def linear_fuel(position1: int, position2: int) -> int:
    return abs(position1 - position2)


def non_linear_fuel(position1: int, position2: int) -> int:
    n = abs(position1 - position2)
    return int(n * (n+1)/2)
