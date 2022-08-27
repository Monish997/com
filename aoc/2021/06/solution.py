with open("input.txt") as f:
    data = f.read().split(",")
    data = list(map(int, data))


def solve(days):
    timers = [0] * 9
    fishes = data.copy()
    for fish in fishes:
        timers[fish] += 1
    for _ in range(days):
        n0 = timers[0]
        timers[:8] = timers[1:]
        timers[8] = n0
        timers[6] += n0

    return sum(timers)


def part1():
    return solve(80)


def part2():
    return solve(256)
