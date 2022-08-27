T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    s = list(map(int, input()))
    z = 0
    prev = k
    for i in range(n):
        unit = 10 - s[i]
        if prev < unit:
            j = i
            while j < n and s[j] == 0:
                z += 1
                j += 1
            break
        if prev % 10 < unit:
            prev = 10 * (prev // 10 - 1) + unit
        else:
            prev = 10 * (prev // 10) + unit
        z += 1
    print(z)
