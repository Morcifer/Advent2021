from copy import deepcopy
from typing import List, Tuple


def day15_parser(s: List[str]) -> List[int]:
    return [int(c) for c in s[0]]


def extend_map(map: List[List[int]]) -> List[List[int]]:
    new_map = []

    for horizontal in range(5):
        for row in map:
            new_map.append([x + horizontal - 9 if x + horizontal > 9 else x + horizontal for x in row])

    new_new_map = []
    for new_row in new_map:
        new_new_row = []
        for vertical in range(5):
            new_new_row.extend([x + vertical - 9 if x + vertical > 9 else x + vertical for x in new_row])
        new_new_map.append(new_new_row)

    return new_new_map


def run_dijkstra(risks: List[List[int]]) -> List[int]:
    height = len(risks)
    width = len(risks)

    # create vertex set Q
    q = set((i, j) for j in range(width) for i in range(height))
    dist = {v: float('inf') for v in q}
    prev = {v: None for v in q}

    source = (0, 0)
    dist[source] = risks[source[0]][source[1]]

    while len(q):
        u = min(q, key=lambda v: dist[v])
        q.remove(u)

        print(f"{len(q)} vertices left to investigate")

        neighbours = []
        if u[0] > 0:
            neighbours.append((u[0] - 1, u[1]))
        if u[0] < height - 1:
            neighbours.append((u[0] + 1, u[1]))
        if u[1] > 0:
            neighbours.append((u[0], u[1] - 1))
        if u[1] < width - 1:
            neighbours.append((u[0], u[1] + 1))

        for v in neighbours:
            if v in q:
                alt = dist[u] + risks[v[0]][v[1]]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

    target = (height - 1, width - 1)
    path = [target]
    while path[-1] != source:
        path.append(prev[path[-1]])

    reversed(path)

    return [risks[v[0]][v[1]] for v in path]
