def weight(subarr):
    diff = [abs(subarr[i] - subarr[i + 1]) for i in range(len(subarr) - 1)]
    diff.sort()
    return diff[-1] * diff[-2]


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(3, n):
        for s in range(n - i):
            ans += weight(a[s : s + i])
    print(ans)


T = int(input())
for t in range(1, T + 1):
    solve()
