with open("input.txt") as f:
    data = f.read().splitlines()
    totalLines = len(data)

input = lambda: data.pop(0)


def part1():
    count = 0
    for _ in range(totalLines):
        _, out_digits = [i.split(" ") for i in input().split(" | ")]
        for digit in out_digits:
            if len(digit) in (2, 4, 3, 7):
                count += 1
    return count


def part2():
    sum_ = 0
    for _ in range(totalLines):
        maps = [set() for _ in range(10)]
        signals, out_digits = [list(map(set, i.split(" "))) for i in input().split(" | ")]
        for s in signals:
            if len(s) == 2:
                maps[1] = s
            elif len(s) == 4:
                maps[4] = s
            elif len(s) == 3:
                maps[7] = s
            elif len(s) == 7:
                maps[8] = s
        for s in signals:
            if len(s) == 5:
                if maps[1].issubset(s):
                    maps[3] = s
                elif len(s.intersection(maps[4])) == 3:
                    maps[5] = s
                else:
                    maps[2] = s
            elif len(s) == 6:
                if maps[4].issubset(s):
                    maps[9] = s
                elif maps[1].issubset(s):
                    maps[0] = s
                else:
                    maps[6] = s
        digits = []
        for d in out_digits:
            digits.append(maps.index(d))
        sum_ += int("".join(map(str, digits)))

    return sum_

