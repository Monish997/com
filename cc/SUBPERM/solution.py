from itertools import chain

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    if k == 1 and n > 1:
        print(-1)
    else:
        print(" ".join(map(str, chain(range(k, n + 1), range(1, k)))))
