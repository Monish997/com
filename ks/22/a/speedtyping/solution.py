def solve(i: str, p: str):
    start = 0
    d = 0
    for char in i:
        l = p.find(char, start)
        if l != -1:
            d += l - start
            start = l + 1
        else:
            return "IMPOSSIBLE"
    else:
        if p[start:]:
            return d + len(p) - start
    return d


t = int(input())
for x in range(1, t + 1):
    i = input()
    p = input()
    print("Case #{}: {}".format(x, solve(i, p)))
