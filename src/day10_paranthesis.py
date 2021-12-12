from typing import List


def day10_parser(s: List[str]) -> str:
    return s[0]


error_score = {
    "": 0,
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

correction_score = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


def find_all_corrupted_scores(lines: List[str]) -> List[int]:
    return [find_corrupted_score(l) for l in lines]


def find_all_autocorrect_scores(lines: List[str]) -> List[int]:
    return [find_autocorrect_score(l) for l in lines]


# TODO: unit-test.
def find_autocorrect_score(line: [str]) -> int:
    corruption, remainder = find_corruption(line)
    if corruption != "":
        return -1

    list.reverse(remainder)

    score = 0
    for r in remainder:
        score = 5 * score + correction_score[r]

    # print(score, remainder)
    return score


# TODO: unit-test.
def find_corrupted_score(line: str) -> int:
    corruption, remainder = find_corruption(line)
    return error_score[corruption]


def find_corruption(line: str) -> (str, List[str]):
    stack = []

    for c in line:
        if c in {"(", "[", "{", "<"}:
            stack.append(c)
        else:
            last = stack.pop() if len(stack) else ""
            if last == "(" and c == ")":
                # print("()")
                continue
            elif last == "[" and c == "]":
                # print("[]")
                continue
            elif last == "{" and c == "}":
                # print("{}")
                continue
            elif last == "<" and c == ">":
                # print("<>")
                continue
            else:
                # print("corrupted!")
                return c, stack

    return "", stack
