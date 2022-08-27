# ./in/challengenine.txt


def solve(n: str):
    iList = list(map(int, n))
    r = sum(iList) % 9
    d = 9 - r if r else 0
    for i in range(len(iList)):
        if d < iList[i]:
            if i == 0 and d == 0:
                continue
            return n[:i] + str(d) + n[i:]
    return n + str(d)


t = int(input())
for x in range(1, t + 1):
    i = input()
    print("Case #{}: {}".format(x, solve(i)))
