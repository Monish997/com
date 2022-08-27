from time import perf_counter
from os.path import basename
from collections import Counter

with open("input.txt") as f:
    data = f.read().splitlines()
template = data[0]
insertions = dict(line.split(" -> ") for line in data[2:])


def solve(steps):
    t = list(template)
    for _ in range(steps):
        i = 0
        while i < len(t) - 1:
            if t[i] + t[i + 1] in insertions:
                t.insert(i + 1, insertions[t[i] + t[i + 1]])
                i += 1
            i += 1
    freq = Counter(t).most_common()
    return freq[0][1] - freq[-1][1]

