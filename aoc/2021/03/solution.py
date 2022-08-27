from collections import Counter
from copy import deepcopy

with open("input.txt") as f:
    data = f.read().splitlines()


def part1():
    bits = [map(int, i) for i in zip(*data)]
    gamma_bits = [Counter(bits[i]).most_common(1)[0][0] for i in range(12)]
    epsilon_bits = [1 - gamma_bits[i] for i in range(12)]

    gamma = int("".join(map(str, gamma_bits)), 2)
    epsilon = int("".join(map(str, epsilon_bits)), 2)
    return gamma * epsilon


def filter_entries(arr, i, ref):
    j = 0
    while j < len(arr[i]):
        if arr[i][j] != ref:
            for k in range(12):
                del arr[k][j]
        else:
            j += 1


def part2():
    bits = [list(map(int, i)) for i in zip(*data)]
    o2_list = deepcopy(bits)
    co2_list = deepcopy(bits)

    for i in range(12):
        common = Counter(o2_list[i]).most_common(2)
        mcb = 1 if common[0][1] == common[1][1] else common[0][0]

        filter_entries(o2_list, i, mcb)
        if len(o2_list[i]) == 1:
            o2_list = [j[0] for j in o2_list]
            break

    for i in range(12):
        common = Counter(co2_list[i]).most_common(2)
        lcb = 0 if common[0][1] == common[1][1] else common[1][0]

        filter_entries(co2_list, i, lcb)
        if len(co2_list[i]) == 1:
            co2_list = [j[0] for j in co2_list]
            break

    o2_rate = int("".join(map(str, o2_list)), 2)
    co2_rate = int("".join(map(str, co2_list)), 2)

    return o2_rate * co2_rate
