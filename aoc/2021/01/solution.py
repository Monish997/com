with open("input.txt") as f:
    data = f.read().splitlines()
    data = list(map(int, data))
    totalLines = len(data)

input = lambda: data.pop(0)


def part1():
    a = input()
    prev, count = a, 0
    for _ in range(totalLines - 1):
        depth = input()
        if depth > prev:
            count += 1
        prev = depth
    return count


def part2():
    a, b, c = [input() for _ in range(3)]
    prev = a + b + c
    count = 0
    for _ in range(totalLines - 3):
        d = input()
        depth = b + c + d
        if depth > prev:
            count += 1
        prev = depth
        b, c = c, d
    return count
