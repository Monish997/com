T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    start = 0
    print(a)
    _sum = 0
    while n > start:
        prefix_sums = [0] * (n - start)
        prefix_sums[0] = a[0]
        for i in range(start + 1, n):
            prefix_sums[i] = a[i] + prefix_sums[i - 1]
        print(prefix_sums)
        _sum += sum(prefix_sums)
        start += 1
    print(_sum + sum(a) - a[0])
