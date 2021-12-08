from typing import List, Tuple, Dict


def day8_parser(s: List[str]) -> (List[str], List[str]):
    digits = s[0:10]
    output = s[11:15]
    return digits, output


def count_digits_in_output(data: List[Tuple[List[str], List[str]]]) -> int:
    result = 0
    for _, output in data:
        result += sum(len(x) in {2, 3, 4, 7} for x in output)
    return result


def get_number(datum: Tuple[List[str], List[str]]) -> int:
    digits = [set(d) for d in datum[0]]

    digit_1 = next(x for x in digits if len(x) == 2)
    digit_4 = next(x for x in digits if len(x) == 4)
    digit_7 = next(x for x in digits if len(x) == 3)
    digit_8 = next(x for x in digits if len(x) == 7)

    line_a = next(c for c in digit_7 if c not in digit_1)
    almost_9 = digit_4.union({line_a})

    digit_9 = next(x for x in digits
                   if len(x) == 6 and len(x.intersection(almost_9)) == 5)

    line_g = list(digit_9.difference(almost_9))[0]

    almost_3 = digit_1.union({line_a, line_g})

    digit_3 = next(x for x in digits
                   if len(x) == 5 and len(x.intersection(almost_3)) == 4)

    line_d = list(digit_3.difference(almost_3))[0]
    digit_0 = next(x for x in digits if x == digit_8.difference({line_d}))

    line_b = list(digit_9.difference(digit_3))[0]

    almost_5 = {line_a, line_d, line_g, line_b}

    digit_5 = next(x for x in digits if len(x) == 5 and len(x.intersection(almost_5)) == 4)

    digit_6 = next(x for x in digits
                   if len(x) == 6 and len(x.intersection(digit_5)) == 5 and len(x.intersection(digit_9)) == 5)

    digit_2 = next(x for x in digits
                   if x not in [digit_0, digit_1, digit_3, digit_4, digit_5, digit_6, digit_7, digit_8, digit_9])

    mapping = {
        "".join(sorted(digit_0)): 0,
        "".join(sorted(digit_1)): 1,
        "".join(sorted(digit_2)): 2,
        "".join(sorted(digit_3)): 3,
        "".join(sorted(digit_4)): 4,
        "".join(sorted(digit_5)): 5,
        "".join(sorted(digit_6)): 6,
        "".join(sorted(digit_7)): 7,
        "".join(sorted(digit_8)): 8,
        "".join(sorted(digit_9)): 9,
    }

    corrupted_number = ["".join(sorted(d)) for d in datum[1]]

    return 1000 * mapping[corrupted_number[0]] + 100 * mapping[corrupted_number[1]] \
           + 10 * mapping[corrupted_number[2]] + mapping[corrupted_number[3]]