with open("input.txt") as f:
    data = f.read().splitlines()
    totalLines = len(data)

input = lambda: data.pop(0)


def part1():
    depth, hor = 0, 0
    for _ in range(totalLines):
        _dir, step = input().split()
        step = int(step)
        if _dir == "forward":
            hor += step
        elif _dir == "up":
            depth -= step
        elif _dir == "down":
            depth += step

    return depth * hor


def part2():
    depth, hor, aim = 0, 0, 0
    for _ in range(totalLines):
        _dir, step = input().split()
        step = int(step)
        if _dir == "forward":
            hor += step
            depth += step * aim
        elif _dir == "up":
            aim -= step
        elif _dir == "down":
            aim += step

    return depth * hor
