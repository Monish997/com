from time import perf_counter
from os.path import basename
from collections import defaultdict

with open("input.txt") as f:
    data = f.read().splitlines()

graph = defaultdict(list)
for line in data:
    a, b = line.split("-")
    graph[a].append(b)
    graph[b].append(a)


def find_paths(start, end, revisit_small=True, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node1 in graph[start]:
        if node1.isupper() or node1 not in path:
            newpaths = find_paths(node1, end, revisit_small, path)
            for newpath in newpaths:
                paths.append(newpath)
        elif node1 not in ("start", "end") and revisit_small:
            seen = set()
            for node2 in path:
                if node2.islower() and node2 in seen:
                    revisit_small = False
                    break
                seen.add(node2)
            else:
                newpaths = find_paths(node1, end, revisit_small, path)
                for newpath in newpaths:
                    paths.append(newpath)
    return paths


def solve(revisit_small):
    paths = find_paths("start", "end", revisit_small)
    return len(paths)

