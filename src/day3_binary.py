from collections import Counter
from typing import List, Callable


def day3_parser(s: List[str]) -> str:
    return s[0]


def calculate_gamma_and_epsilon(data: List[str]) -> (int, int):
    gamma = ""
    epsilon = ""
    for i in range(12):
        digits = [datum[i] for datum in data]
        counter = Counter(digits)
        # print(digits)
        # print(counter)

        gamma = gamma + ("0" if counter["0"] > counter["1"] else "1")
        epsilon = epsilon + ("1" if counter["0"] > counter["1"] else "0")

    return int(gamma, 2), int(epsilon, 2)


def calculate_oxygen_and_scrubber(data: List[str]) -> (int, int):
    oxygen = calculate_based_on_criteria(data, lambda c: "0" if c["0"] > c["1"] else "1")
    scrubber = calculate_based_on_criteria(data, lambda c: "0" if c["0"] <= c["1"] else "1")

    return oxygen, scrubber


def calculate_based_on_criteria(data: List[str], criteria_getter: Callable[[Counter], str]) -> int:
    position = 0
    relevant_numbers = data

    while len(relevant_numbers) > 1:
        digits = [datum[position] for datum in relevant_numbers]
        counter = Counter(digits)
        criteria = criteria_getter(counter)
        relevant_numbers = [number for number in relevant_numbers if number[position] == criteria]
        position += 1

    return int(relevant_numbers[0], 2)