from typing import List


def day1_parser(s: List[str]) -> int:
    return int(s[0])


def count_increases(data: List[int]) -> int:
    zero_term = data[:-1]
    one_term = data[1:]
    diff = [x1 - x2 for x1, x2 in zip(one_term, zero_term)]

    # print(data)
    # print(diff)
    # print(len(data))

    return sum(d > 0 for d in diff)


def rolling_horizon(data: List[int]) -> List[int]:
    return [data[i] + data[i+1] + data[i+2] for i in range(0, len(data) - 2)]
