from typing import Tuple, List

# Train
# target_x = (20, 30)
# target_y = (-5, -10)

# Test
target_x = (32, 65)
target_y = (-177, -225)


def get_max_height() -> int:
    max_max_y = 0

    max_x_speed = target_x[1]
    max_y_speed = max(abs(target_y[0]), abs(target_y[1]))

    for x_speed in range(1, max_x_speed):
        for y_speed in range(1, max_y_speed):
            speed = (x_speed, y_speed)
            success, max_y = simulate(speed)
            if success:
                if max_y > max_max_y:
                    # print(f"Found better speed, ({x_speed}, {y_speed}), for height {max_y}")
                    max_max_y = max_y

    return max_max_y


def get_all_speeds() -> List[Tuple[int, int]]:
    result = []

    max_x_speed = target_x[1]
    min_y_speed = target_y[1]
    max_y_speed = max(abs(target_y[0]), abs(target_y[1]))

    for x_speed in range(1, max_x_speed + 1):
        for y_speed in range(min_y_speed, max_y_speed + 1):
            speed = (x_speed, y_speed)
            success, max_y = simulate(speed)
            if success:
                print(f"Found speed {speed}, for height {max_y}")
                result.append(speed)

    return result


def simulate(speed: Tuple[int, int]) -> (bool, int):
    x, y = 0, 0
    x_speed, y_speed = speed
    max_y = 0

    if x_speed < 0:  # Negative x speed is nonsensical.
        return False, -1

    while x <= target_x[1] and y >= target_y[1] and (x_speed > 0 or x >= target_x[0]):
        if target_x[0] <= x <= target_x[1] and target_y[1] <= y <= target_y[0]:
            # print("Success!")
            return True, max_y

        x += x_speed
        y += y_speed
        max_y = max(max_y, y)

        if x_speed != 0:
            x_speed -= 1
        y_speed -= 1

    print(f"Failure!!! Reached ({x}, {y}) at speed ({x_speed}, {y_speed}) (from {speed})")
    return False, -1
