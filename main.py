from functools import reduce
from statistics import median

from src.day10_paranthesis import day10_parser, find_all_corrupted_scores, find_all_autocorrect_scores
from src.day11_flashes import day11_parser, simulate_all_steps_of_map, find_first_simultaneous_flash
from src.day12_graph import day12_parser, find_all_paths
from src.day13_dots import day13_parser, split_data_to_points_and_cuts, apply_cuts, show_result
from src.day14_insertions import day14_parser, apply_insertions, apply_insertions_quick
from src.day15_cave import day15_parser, run_dijkstra, extend_map
from src.day16_bits import day16_parser, parse
from src.day17_rocket_science import get_max_height, get_all_speeds
from src.day18_snails import day18_parser, add_all, calculate_score
from src.day19_beacons import day19_parser, split_data_to_scanners_and_beacons, normalize_beacons
from src.day1_calculators import count_increases, rolling_horizon, day1_parser
from src.day20_image import day20_parser, enhance, split_data, count_lights, print_image
from src.day21_die import get_final_score_deterministic, get_final_score_dirac
from src.day22_cubed import day22_parser, reboot, reboot_all
from src.day24_assembly import day24_parser, find_highest_model_number
from src.day25_cucumbers import day25_parser, simulate_cucumbers
from src.day2_commands import calculate_final_location, day2_parser
from src.day3_binary import day3_parser, calculate_gamma_and_epsilon, calculate_oxygen_and_scrubber
from src.day4_bingo import load_bingo_data, find_winning_board, find_losing_board
from src.day5_lines import day5_parser, calculate_final_grid
from src.day6_FIESH import day6_parser, simulate_fish, simulate_fish_better
from src.day7_crabs import day7_parser, find_best_location_and_fuel
from src.day8_digits import day8_parser, count_digits_in_output, get_number
from src.day9_lava import day9_parser, find_high_spots, find_basins_values
from src.utilities import load_data


def day1_1() -> int:
    data = load_data(1, day1_parser, "data")
    return count_increases(data)


def day1_2() -> int:
    data = load_data(1, day1_parser, "data")
    return count_increases(rolling_horizon(data))


def day2_1() -> int:
    commands = load_data(2, day2_parser, "data")
    x, y = calculate_final_location(commands, "move")
    return x * y


def day2_2() -> int:
    commands = load_data(2, day2_parser, "data")
    x, y = calculate_final_location(commands, "move_with_aim")
    return x * y


def day3_1() -> int:
    diagnostics = load_data(3, day3_parser, "data")
    gamma, epsilon = calculate_gamma_and_epsilon(diagnostics)
    return gamma * epsilon


def day3_2() -> int:
    diagnostics = load_data(3, day3_parser, "data")
    oxygen, scrubber = calculate_oxygen_and_scrubber(diagnostics)
    return oxygen * scrubber


def day4_1() -> int:
    numbers, boards = load_bingo_data("data")
    winning_board, number = find_winning_board(numbers, boards)
    return winning_board.score() * number


def day4_2() -> int:
    numbers, boards = load_bingo_data("data")
    losing_board, number = find_losing_board(numbers, boards)
    return losing_board.score() * number


def day5_1() -> int:
    lines = load_data(5, day5_parser, "data")
    final_grid = calculate_final_grid(lines, filter_diagonal=True)
    return final_grid.get_high_risk_count()


def day5_2() -> int:
    lines = load_data(5, day5_parser, "data")
    final_grid = calculate_final_grid(lines, filter_diagonal=False)
    return final_grid.get_high_risk_count()


def day6_1() -> int:
    fish = load_data(6, day6_parser, "data")[0]
    fish = simulate_fish_better(fish, time=80)
    return fish


def day6_2() -> int:
    fish = load_data(6, day6_parser, "data")[0]
    fish = simulate_fish_better(fish, time=256)
    return fish


def day7_1() -> int:
    positions = load_data(7, day7_parser, "data")[0]
    location, fuel = find_best_location_and_fuel(positions, linear=True)
    return fuel


def day7_2() -> int:
    positions = load_data(7, day7_parser, "data")[0]
    location, fuel = find_best_location_and_fuel(positions, linear=False)
    return fuel


def day8_1() -> int:
    data = load_data(8, day8_parser, "data")
    number_of_digits = count_digits_in_output(data)
    return number_of_digits


def day8_2() -> int:
    data = load_data(8, day8_parser, "data")
    numbers = [get_number(datum) for datum in data]
    return sum(numbers)


def day9_1() -> int:
    heights = load_data(9, day9_parser, "data")
    high_spots, high_spots_values = find_high_spots(heights)
    return sum(high_spots_values) + len(high_spots_values)


def day9_2() -> int:
    heights = load_data(9, day9_parser, "data")
    basins_values = find_basins_values(heights)
    basins_values = sorted(basins_values)
    return reduce((lambda x, y: x * y), basins_values[-3:])


def day10_1() -> int:
    data = load_data(10, day10_parser, "data")
    scores = find_all_corrupted_scores(data)
    return sum(scores)


def day10_2() -> int:
    data = load_data(10, day10_parser, "data")
    scores = find_all_autocorrect_scores(data)
    return median([s for s in scores if s != -1])


def day11_1() -> int:
    data = load_data(11, day11_parser, "data")
    flashes = simulate_all_steps_of_map(data)
    return flashes


def day11_2() -> int:
    data = load_data(11, day11_parser, "data")
    step = find_first_simultaneous_flash(data)
    return step


def day12_1() -> int:
    edges = load_data(12, day12_parser, "data")
    paths = find_all_paths(edges, once_at_most=True)
    return len(paths)


def day12_2() -> int:
    edges = load_data(12, day12_parser, "data")
    paths = find_all_paths(edges, once_at_most=False)
    return len(paths)


def day13_1() -> int:
    data = load_data(13, day13_parser, "data")
    all_points, all_cuts = split_data_to_points_and_cuts(data)
    result = apply_cuts(all_points, all_cuts[0:1])
    return len(result)


def day13_2() -> int:
    data = load_data(13, day13_parser, "data")
    all_points, all_cuts = split_data_to_points_and_cuts(data)
    result = apply_cuts(all_points, all_cuts)
    show_result(result)
    return len(result)


def day14_1() -> int:
    data = load_data(14, day14_parser, "data")
    result = apply_insertions(data[0], data[2:], steps=10)
    return result


def day14_2() -> int:
    data = load_data(14, day14_parser, "data")
    result = apply_insertions_quick(data[0], data[2:], steps=40)
    return result


def day15_1() -> int:
    map = load_data(15, day15_parser, "data")
    result = run_dijkstra(map)
    return sum(result) - map[0][0]


def day15_2() -> int:
    map = load_data(15, day15_parser, "data")
    map = extend_map(map)
    result = run_dijkstra(map)
    return sum(result) - map[0][0]


def day16_1() -> int:
    data = load_data(16, day16_parser, "data")[0]
    data = data[:-4]  # Manual Cheat
    result = []
    parse(data, False, result)
    return sum(result)


def day17_1() -> int:
    result = get_max_height()
    return result


def day17_2() -> int:
    result = get_all_speeds()
    return len(result)


def day18_1() -> int:
    numbers = load_data(18, day18_parser, "data")
    result = add_all(numbers)
    return calculate_score(result)


def day18_2() -> int:
    numbers = load_data(18, day18_parser, "data")
    max_score = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            new_result = add_all([numbers[i], numbers[j]])
            new_score = calculate_score(new_result)
            if new_score > max_score:
                print(f"Found new max score ({new_score})")
                max_score = new_score

    return max_score


def day19() -> (int, int):
    data = load_data(19, day19_parser, "data")
    data = split_data_to_scanners_and_beacons(data)
    beacons, max_distance = normalize_beacons(data)
    return len(beacons), max_distance


def day20_2() -> int:
    data = load_data(20, day20_parser, "data")
    enhancement, image = split_data(data)

    for _ in range(50):
        print(f"enhancement {_}")
        image = enhance(enhancement, image)

    cheat = [r[5:-5] for r in image[5:-5]]
    print_image(cheat)

    return count_lights(cheat)


def day20_1() -> int:
    data = load_data(20, day20_parser, "data")
    enhancement, image = split_data(data)

    for _ in range(50):
        print(f"enhancement {_}")
        image = enhance(enhancement, image)

    cheat = [r[5:-5] for r in image[5:-5]]
    print_image(cheat)

    return count_lights(cheat)


def day21_1() -> int:
    result = get_final_score_deterministic()
    return result


def day21_2() -> int:
    result = get_final_score_dirac()
    return result


def day22_1() -> int:
    steps = load_data(22, day22_parser, "data")
    result = reboot(steps)
    return result


def day22_2() -> int:
    steps = load_data(22, day22_parser, "data")
    result = reboot_all(steps)
    return result


def day24_1() -> int:
    instructions = load_data(24, day24_parser, "data")
    result = find_highest_model_number(instructions)
    return result


def day25_1() -> int:
    cucumbers = load_data(25, day25_parser, "data")
    result = simulate_cucumbers(cucumbers)
    return result


if __name__ == '__main__':
    # print(f"Day 1 result 1: {day1_1()}")
    # print(f"Day 1 result 2: {day1_2()}")
    # print(f"Day 2 result 1: {day2_1()}")
    # print(f"Day 2 result 2: {day2_2()}")
    # print(f"Day 3 result 1: {day3_1()}")
    # print(f"Day 3 result 2: {day3_2()}")
    # print(f"Day 4 result 1: {day4_1()}")
    # print(f"Day 4 result 2: {day4_2()}")
    # print(f"Day 5 result 1: {day5_1()}")
    # print(f"Day 5 result 2: {day5_2()}")
    # print(f"Day 6 result 1: {day6_1()}")
    # print(f"Day 6 result 2: {day6_2()}")
    # print(f"Day 7 result 1: {day7_1()}")
    # print(f"Day 7 result 2: {day7_2()}")
    # print(f"Day 8 result 1: {day8_1()}")
    # print(f"Day 8 result 2: {day8_2()}")
    # print(f"Day 9 result 1: {day9_1()}")
    # print(f"Day 9 result 2: {day9_2()}")
    # print(f"Day 10 result 1: {day10_1()}")
    # print(f"Day 10 result 2: {day10_2()}")
    # print(f"Day 11 result 1: {day11_1()}")
    # print(f"Day 11 result 2: {day11_2()}")
    # print(f"Day 12 result 1: {day12_1()}")
    # print(f"Day 12 result 2: {day12_2()}")  # Run-time too long because I'm lazy
    # print(f"Day 13 result 1: {day13_1()}")
    # print(f"Day 13 result 2: {day13_2()}")
    # print(f"Day 14 result 1: {day14_1()}")
    # print(f"Day 14 result 2: {day14_2()}")
    # print(f"Day 15 result 1: {day15_1()}")
    # print(f"Day 15 result 2: {day15_2()}")  # No A*, no quick run time
    # print(f"Day 16 result 1: {day16_1()}")
    # print(f"Day 16 result 2: {day16_2()}")  # CHEAT
    # print(f"Day 17 result 1: {day17_1()}")
    # print(f"Day 17 result 2: {day17_2()}")
    # print(f"Day 18 result 1: {day18_1()}")
    # print(f"Day 18 result 2: {day18_2()}")
    # print(f"Day 19 result 1, 2: {day19()}")
    # print(f"Day 20 result 1: {day20_1()}")
    # print(f"Day 20 result 2: {day20_2()}")
    # print(f"Day 21 result 1: {day21_1()}")
    # print(f"Day 21 result 2: {day21_2()}")
    # print(f"Day 22 result 1: {day22_1()}")
    # print(f"Day 22 result 2: {day22_2()}")
    print(f"Day 24 result 1: {day24_1()}")
    # print(f"Day 24 result 2: {day24_2()}")
    # print(f"Day 25 result 1: {day25_1()}")
