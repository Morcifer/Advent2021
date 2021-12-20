from math import floor, ceil
from typing import List, Optional


def day18_parser(s: List[str]) -> List[str]:
    s = s[0]

    result = []
    i = 0

    while i < len(s):
        if s[i] in "[],":
            result.append(s[i])
            i += 1
            continue

        if s[i].isdigit():
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            result.append(s[i:j])
            i = j
            continue

    return result


# def day18_parser(s: List[str]) -> List:
#     return parse_string(s[0])


# def parse_string(s: str):
#     if len(s) == 1:
#         return int(s[0])
#
#     if s[0] == "[":
#         s = s[1:-1]
#         count = 0
#         for index in range(len(s)):
#             if s[index] == "[":
#                 count += 1
#             elif s[index] == "]":
#                 count -= 1
#             if count == 0:
#                 break
#         elem_1 = parse_string(s[:index+1])
#         elem_2 = parse_string(s[index+2:])
#
#         return [elem_1, elem_2]


def add_all(numbers: List[str]) -> List[str]:
    # To add two snailfish numbers, form a pair from the left and right parameters of the addition operator.
    # For example, [1,2] + [[3,4],5] becomes [[1,2],[[3,4],5]].
    sum = numbers[0]
    for i in range(1, len(numbers)):
        sum = add(sum, numbers[i])

    return sum


def add(number1: List[str], number2: List[str]) -> List[str]:
    # To add two snailfish numbers, form a pair from the left and right parameters of the addition operator.
    # For example, [1,2] + [[3,4],5] becomes [[1,2],[[3,4],5]].
    result = ["["] + number1 + [","] + number2 + ["]"]
    result = reduce(result)

    return result


def reduce(number: List[str]) -> List[str]:
    # print_number(number)

    e_spot = explosion_spot(number)
    s_spot = split_spot(number)

    while e_spot is not None or s_spot is not None:
        if e_spot is not None:
            number = explode(number, e_spot)
        else:
            number = split(number, s_spot)

        # print_number(number)

        e_spot = explosion_spot(number)
        s_spot = split_spot(number)

    return number


# If any pair is nested inside four pairs, the leftmost such pair explodes.
def explosion_spot(number: List[str]) -> Optional[int]:
    count = 0
    for i in range(len(number)):
        if count >= 5 and number[i].isdigit() and i + 2 < len(number) and number[i+2].isdigit():
            return i

        if number[i] == "[":
            count += 1
        elif number[i] == "]":
            count -= 1

    return None


# If any regular number is 10 or greater, the leftmost such regular number splits.
def split_spot(number: List[str]) -> Optional[int]:
    for i in range(len(number)):
        if number[i].isdigit() and int(number[i]) >= 10:
            return i

    return None


def explode(number: List[str], explode_index: int) -> List[str]:
    # print("Explode!")

    left_index = -1
    right_index = -1
    # print_number(number)

    left_number = int(number[explode_index])
    right_number = int(number[explode_index + 2])

    for i in range(explode_index):
        if number[i].isdigit():
            left_index = i

    for i in range(explode_index + 3, len(number)):
        if number[i].isdigit():
            right_index = i
            break

    if left_index != -1:
        number[left_index] = str(int(number[left_index]) + left_number)

    if right_index != -1:
        number[right_index] = str(int(number[right_index]) + right_number)

    return number[:explode_index-1] + ["0"] + number[explode_index + 4:]


def split(number: List[str], split_index: int) -> List[str]:
    # print("Split...")

    old_number = int(number[split_index])
    left_element = int(floor(old_number / 2))
    right_element = int(ceil(old_number / 2))

    return number[:split_index] + ["[", str(left_element), ",", str(right_element), "]"] + number[split_index+1:]


def print_number(number: List[str]):
    print("".join(number))


def calculate_score(number: List[str]) -> int:
    # The magnitude of a pair is
    # 3 times the magnitude of its left element plus 2 times the magnitude of its right element.
    # The magnitude of a regular number is just that number.
    # Split into numbers:
    if len(number) == 1:
        return int(number[0])

    if number[0] == "[":
        number = number[1:-1]
        count = 0
        for index in range(len(number)):
            if number[index] == "[":
                count += 1
            elif number[index] == "]":
                count -= 1
            if count == 0:
                break

        score_1 = calculate_score(number[:index+1])
        score_2 = calculate_score(number[index+2:])

        return 3 * score_1 + 2 * score_2


if __name__ == "__main__":
    # data = day18_parser(["[[[[[9,8],1],2],3],4]"])
    # print_number(explode(data, explosion_spot(data)))
    #
    # data = day18_parser(["[7,[6,[5,[4,[3,2]]]]]"])
    # print_number(explode(data, explosion_spot(data)))
    #
    # data = day18_parser(["[[6,[5,[4,[3,2]]]],1]"])
    # print_number(explode(data, explosion_spot(data)))
    #
    # data = day18_parser(["[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"])
    # print_number(explode(data, explosion_spot(data)))
    #
    # data = day18_parser(["[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"])
    # print_number(explode(data, explosion_spot(data)))

    number_1 = day18_parser(["[[[[4,3],4],4],[7,[[8,4],9]]]"])
    number_2 = day18_parser(["[1,1]"])
    print_number(add(number_1, number_2))
