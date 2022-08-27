from collections import defaultdict

with open("input.txt") as f:
    data = f.read().splitlines()
    totalLines = len(data)

input = lambda: data.pop(0)

def part1():
    freq = defaultdict(int)
    for _ in range(totalLines):
        p1, p2 = map(eval, input().split(" -> "))
        if p1[0] == p2[0]:
            s, e = sorted([p1[1], p2[1]])
            for i in range(s, e + 1):
                freq[(p1[0], i)] += 1
        elif p1[1] == p2[1]:
            s, e = sorted([p1[0], p2[0]])
            for i in range(s, e + 1):
                freq[(i, p1[1])] += 1

    ans = 0
    for _, f in freq.items():
        if f > 1:
            ans += 1
    return ans


def part2():
    freq = defaultdict(int)
    for _ in range(totalLines):
        p1, p2 = map(eval, input().split(" -> "))
        if p1[0] == p2[0]:
            s, e = sorted([p1[1], p2[1]])
            for i in range(s, e + 1):
                freq[(p1[0], i)] += 1
        elif p1[1] == p2[1]:
            s, e = sorted([p1[0], p2[0]])
            for i in range(s, e + 1):
                freq[(i, p1[1])] += 1
        else:
            s, e = sorted([p1, p2])
            d = 1 if e[1] > s[1] else -1
            l = e[0] - s[0] + 1
            for i in range(l):
                freq[(s[0] + i, s[1] + d * i)] += 1

    ans = 0
    for _, f in freq.items():
        if f > 1:
            ans += 1
    return ans

