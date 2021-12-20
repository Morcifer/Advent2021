from collections import Counter
from typing import List, Union, Tuple, Dict

from setuptools._vendor.more_itertools import pairwise


def day14_parser(s: List[str]) -> Union[str, Tuple[str, str]]:
    if len(s) == 1 and s[0] == "":
        return None

    if len(s) == 3:
        return s[0], s[2]

    return s[0]


def apply_insertions(template: str, insertions: List[Tuple[str, str]], steps: int) -> str:
    insertions = {i[0]: i[1] for i in insertions}

    for _ in range(steps):
        # print(_)
        # print(template)
        template = apply_insertion(template, insertions)

    # print(template)
    counter = Counter(template)
    max_counter = max(counter.values())
    min_counter = min(counter.values())
    return max_counter - min_counter


def apply_insertion(template: str, insertions: Dict[str, str]) -> str:
    new_template = ""
    for i in range(len(template) - 1):
        pair = template[i:i+2]
        new_template += pair[0] + insertions[pair]
    new_template += template[-1]
    return new_template


def apply_insertions_quick(template: str, insertions: List[Tuple[str, str]], steps: int) -> str:
    template_counter = Counter([template[i:i + 2] for i in range(len(template) - 1)])
    insertions = {i[0]: i[1] for i in insertions}

    for _ in range(steps):
        # print(_)
        # print(template_counter)
        template_counter = apply_insertion_quick(template_counter, insertions)

    # print(template_counter)

    new_counter = Counter()
    for pair, value in template_counter.items():
        for s in pair:
            if s not in new_counter:
                new_counter[s] = 0
            new_counter[s] += value
    new_counter[template[0]] += 1
    new_counter[template[-1]] += 1

    # print(new_counter)
    max_counter = max(new_counter.values())
    min_counter = min(new_counter.values())

    return (max_counter - min_counter) / 2


def apply_insertion_quick(template: Counter, insertions: Dict[str, str]) -> str:
    new_template = Counter()
    for pair, value in template.items():
        insert = insertions[pair]
        new_pair_1 = pair[0] + insert
        new_pair_2 = insert + pair[1]
        if new_pair_1 not in new_template:
            new_template[new_pair_1] = 0
        if new_pair_2 not in new_template:
            new_template[new_pair_2] = 0
        new_template[new_pair_1] += value
        new_template[new_pair_2] += value

    return new_template


# Template:     NNCB
# After step 1: NCNBCHB
# After step 2: NBCCNBBBCBHCB
# After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
# After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB