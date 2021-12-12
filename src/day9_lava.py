from typing import List, Tuple


def day9_parser(s: List[str]) -> List[int]:
    return [int(c) for c in s[0]]


def find_high_spots(heights: List[List[int]]) -> (List[Tuple[int, int]], List[int]):
    high_spots = []
    high_spots_values = []
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            this_height = heights[i][j]
            # print(i, j)

            if i > 0 and this_height >= heights[i-1][j]:
                continue
            if i < len(heights) - 1 and this_height >= heights[i+1][j]:
                continue

            if j > 0 and this_height >= heights[i][j-1]:
                continue
            if j < len(heights[0]) - 1 and this_height >= heights[i][j+1]:
                continue

            high_spots.append((i, j))
            high_spots_values.append(this_height)

    return high_spots, high_spots_values


def find_basins_values(heights: List[List[int]]) -> List[int]:
    high_spots, high_spots_values = find_high_spots(heights)
    basin_sizes = []

    for high_spot_i, high_spot_j in high_spots:
        # print(high_spot_i, high_spot_j)
        # Flood fill algorithm
        q = []
        encountered = set()
        q.append((high_spot_i, high_spot_j))
        while len(q):
            i, j = q.pop(0)

            if (i, j) in encountered:
                continue

            encountered.add((i, j))

            this_height = heights[i][j]

            if i > 0 and this_height < heights[i - 1][j] and heights[i - 1][j] != 9:
                q.append((i - 1, j))
            if i < len(heights) - 1 and this_height < heights[i + 1][j] and heights[i + 1][j] != 9:
                q.append((i + 1, j))
            if j > 0 and this_height < heights[i][j - 1] and heights[i][j - 1] != 9:
                q.append((i, j - 1))
            if j < len(heights[0]) - 1 and this_height < heights[i][j + 1] and heights[i][j + 1] != 9:
                q.append((i, j + 1))

        # print(len(encountered))
        basin_sizes.append(len(encountered))

    # print(basin_sizes)
    return basin_sizes
