from math import ceil, floor
from statistics import mean, median

with open("input.txt") as f:
    data = f.read().split(",")
    locations = list(map(int, data))


def part1():
    med = int(median(locations))
    return sum(abs(n - med) for n in locations)


def part2():
    x = mean(locations)
    x1, x2 = floor(x), ceil(x)
    d1 = sum(abs(x1 - n) * (abs(x1 - n) + 1) / 2 for n in locations)
    d2 = sum(abs(x2 - n) * (abs(x2 - n) + 1) / 2 for n in locations)
    return int(min(d1, d2))

