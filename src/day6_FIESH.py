from collections import Counter
from typing import List


def day6_parser(s: List[str]) -> List[int]:
    all_fish = s[0].split(",")
    return [int(x) for x in all_fish]


def simulate_fish(fish: List[int], time: int) -> int:
    for day in range(time):
        # print(f"After {day} days, I have {len(fish)} fish")

        fish_of_the_day = fish[:]

        for fish_index in range(len(fish_of_the_day)):
            if fish_of_the_day[fish_index] == 0:
                fish[fish_index] = 6
                fish.append(8)
            else:
                fish[fish_index] -= 1


    return len(fish)


def simulate_fish_better(fish: List[int], time: int) -> int:
    counter = Counter(fish)
    for i in range(9):
        if i not in counter:
            counter[i] = 0

    for day in range(time):
        # print(f"After {day} days, I have {sum(counter.values())} fish")
        # print(counter)

        new_fish = counter[0]
        for i in range(8):
            counter[i] = counter[i+1]
        counter[6] += new_fish
        counter[8] = new_fish

    # print(f"After {day+1} days, I have {sum(counter.values())} fish")

    return sum(counter.values())
