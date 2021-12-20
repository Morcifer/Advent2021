from typing import List, Union, Tuple, Dict, Set


def day19_parser(s: List[str]) -> Union[str, Tuple[int, int, int]]:
    if s[0] == "":
        return None

    if "," in s[0]:
        x, y, z = s[0].split(",")
        return int(x), int(y), int(z)

    return f"{s[1]} {s[2]}"


def split_data_to_scanners_and_beacons(
        data: List[Union[str, Tuple[int, int, int]]]
) -> Dict[str, List[Tuple[int, int, int]]]:
    result = {}
    sensor_name = ""

    for datum in data:
        if datum is None:
            continue

        if type(datum) == str:
            sensor_name = datum
            result[sensor_name] = []
        else:
            result[sensor_name].append(datum)

    return result


def get_shifted_beacons(beacon: Tuple[int, int, int], beacons: List[Tuple[int, int, int]]) -> Set[Tuple[int, int, int]]:
    return {shift_reference(b, beacon) for b in beacons}


def normalize_beacons(scanner_results:  Dict[str, List[Tuple[int, int, int]]]) -> Tuple[Set[Tuple[int, int, int]], int]:
    identified_scanners = {"scanner 0"}
    unidentified_scanners = {s for s in scanner_results}.difference(identified_scanners)

    all_identified_beacon_references = {
        "scanner 0": {
            b: get_shifted_beacons(b, scanner_results["scanner 0"])
            for b in scanner_results["scanner 0"]
        }
    }
    scanner_spots = {"scanner 0": (0, 0, 0)}

    while len(identified_scanners) < len(scanner_results):
        found_match = False

        for unidentified_scanner in unidentified_scanners:
            # Try to match to one of the identified ones
            unidentified_scanner_spot = (0, 0, 0)

            for beacon in scanner_results[unidentified_scanner]:
                shifted_beacons = [shift_reference(b, beacon)
                                   for b in scanner_results[unidentified_scanner]]
                shifted_unidentified_scanner_spot = shift_reference(unidentified_scanner_spot, beacon)

                for rotation in all_rotations:
                    rotated_beacons = {rotate(b, rotation) for b in shifted_beacons}
                    rotated_unidentified_scanner_spot = rotate(shifted_unidentified_scanner_spot, rotation)

                    for identified_scanner in identified_scanners:
                        for identified_beacon, shifted_identified_beacons in all_identified_beacon_references[identified_scanner].items():
                            if len(rotated_beacons.intersection(shifted_identified_beacons)) >= 12:
                                print(f"Found match for unidentified {unidentified_scanner} with {identified_scanner}. "
                                      f"{len(unidentified_scanners) - 1} to go!")
                                print(f"Reference point is {identified_beacon} and rotation is {rotation}")
                                found_match = True

                                identified_scanners.add(unidentified_scanner)
                                unidentified_scanners.remove(unidentified_scanner)
                                re_shift = (-identified_beacon[0], -identified_beacon[1], -identified_beacon[2])
                                scanner_results[unidentified_scanner] = [shift_reference(b, re_shift) for b in rotated_beacons]
                                all_identified_beacon_references[unidentified_scanner] = {
                                    b: get_shifted_beacons(b, scanner_results[unidentified_scanner])
                                    for b in scanner_results[unidentified_scanner]
                                }

                                scanner_spot = shift_reference(rotated_unidentified_scanner_spot, re_shift)
                                scanner_spots[unidentified_scanner] = scanner_spot

                            if found_match:
                                break

                        if found_match:
                            break

                    if found_match:
                        break

                if found_match:
                    break

            if found_match:
                break

        if not found_match:
            print("I'm stuck!!!")
            print(f"Identified scanners: {identified_scanners}")
            print(f"Unidentified scanners: {unidentified_scanners}")

    all_beacons = set([b for scanner, beacons in scanner_results.items() for b in beacons])

    max_distance = 0
    for scanner1, spot1 in scanner_spots.items():
        for scanner2, spot2 in scanner_spots.items():
            dist_x = abs(spot1[0] - spot2[0])
            dist_y = abs(spot1[1] - spot2[1])
            dist_z = abs(spot1[2] - spot2[2])
            dist = dist_x + dist_y + dist_z
            max_distance = max(max_distance, dist)

    return all_beacons, max_distance


def shift_reference(beacon: Tuple[int, int, int], reference: Tuple[int, int, int]) -> Tuple[int, int, int]:
    return beacon[0] - reference[0], beacon[1] - reference[1], beacon[2] - reference[2]


def rotate_x(beacon: Tuple[int, int, int]) -> Tuple[int, int, int]:
    return beacon[0], -beacon[2], beacon[1]


def rotate_y(beacon: Tuple[int, int, int]) -> Tuple[int, int, int]:
    return beacon[2], beacon[1], -beacon[0]


def rotate_z(beacon: Tuple[int, int, int]) -> Tuple[int, int, int]:
    return -beacon[1], beacon[0], -beacon[2]


def rotate(beacon: Tuple[int, int, int], rotation: str) -> Tuple[int, int, int]:
    result = (beacon[0], beacon[1], beacon[2])
    for c in rotation:
        if c == "I":
            result = result
        elif c == "X":
            result = rotate_x(result)
        elif c == "Y":
            result = rotate_y(result)
        elif c == "Z":
            result = rotate_z(result)
    return result


all_rotations = [
    "I",
    "X",
    "Y",
    "XX",
    "XY",
    "YX",
    "YY",
    "XXX",
    "XXY",
    "XYX",
    "XYY",
    "YXX",
    "YYX",
    "YYY",
    "XXXY",
    "XXYX",
    "XXYY",
    "XYXX",
    "XYYY",
    "YXXX",
    "YYYX",
    "XXXYX",
    "XYXXX",
    "XYYYX",
]

