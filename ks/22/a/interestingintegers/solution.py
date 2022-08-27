from operator import mul
from functools import reduce, lru_cache

@lru_cache(maxsize=None)
def isInteresting(iTup: tuple):
    prod = reduce(mul, iTup)
    s = sum(iTup)
    return prod % s == 0


def solve(a: int, b: int):
    cnt = 0
    for i in range(a, b + 1):
        digits = tuple(sorted(map(int, str(i))))
        if isInteresting(digits):
            cnt += 1
    return cnt


t = int(input())
for x in range(1, t + 1):
    a, b = map(int, input().split())
    print("Case #{}: {}".format(x, solve(a, b)))
