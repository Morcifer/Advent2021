from typing import List, Tuple


def day12_parser(s: List[str]) -> (str, str):
    from_to = s[0].split("-")
    return from_to[0], from_to[1]


class Path:
    def __init__(self, once_at_most: bool):
        self.once_at_most = once_at_most
        self.small_cave_multiple = None

        self.path_nodes = list()
        self.visited = set()

    def clone(self) -> 'Path':
        clone = Path(self.once_at_most)
        clone.small_cave_multiple = self.small_cave_multiple
        clone.path_nodes = self.path_nodes[:]
        clone.visited = set(self.visited)
        return clone

    def last_node(self) -> str:
        return self.path_nodes[-1]

    def try_add(self, s: str) -> bool:
        if self.is_small_cave(s) and s in self.visited:
            if self.once_at_most:
                return False
            if s in {"start", "end"}:
                return False
            if self.small_cave_multiple is not None:
                return False
            self.small_cave_multiple = s

        self.path_nodes.append(s)
        self.visited.add(s)
        return True

    def is_finished(self) -> bool:
        return self.path_nodes[-1] == "end"

    @staticmethod
    def is_small_cave(s: str) -> bool:
        return s.lower() == s

    @staticmethod
    def is_large_cave(s: str) -> bool:
        return s.upper() == s

    def __str__(self):
        return "-".join(self.path_nodes)

    def __hash__(self):
        return self.__str__().__hash__()

    def __eq__(self, other):
        return isinstance(other, Path) and other.__hash__ == self.__hash__


class Graph:
    def __init__(self, edges: List[Tuple[str, str]]):
        self.edges = edges
        self.nodes = set(n for edge in edges for n in edge)

        self.connected_nodes = {n: [] for n in self.nodes}
        for edge in self.edges:
            self.connected_nodes[edge[0]].append(edge[1])
            self.connected_nodes[edge[1]].append(edge[0])

    # I refuse to do dynamic programming here.
    def find_paths_from_start_to_end(self, once_at_most: bool) -> List[Path]:
        all_finished_paths = []
        paths_to_explore = set()
        explored_paths = set()

        starting_path = Path(once_at_most)
        starting_path.try_add("start")
        paths_to_explore.add(starting_path)

        while any(paths_to_explore):
            path_to_explore = paths_to_explore.pop()
            explored_paths.add(path_to_explore)

            for target in self.connected_nodes[path_to_explore.last_node()]:
                clone = path_to_explore.clone()
                if clone.try_add(target):
                    if clone.is_finished():
                        all_finished_paths.append(clone)
                        # print(clone)
                    else:
                        if clone not in explored_paths:
                            paths_to_explore.add(clone)

        return all_finished_paths


def find_all_paths(data: List[Tuple[str, str]], once_at_most: bool) -> List[Path]:
    graph = Graph(data)
    result = graph.find_paths_from_start_to_end(once_at_most)
    return result
