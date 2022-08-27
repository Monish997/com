T = int(input())
for _ in range(T):
    _, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for ai, bi in zip(a, b):
        if bi - ai != x and bi - ai != y:
            print("No")
            break
    else:
        print("Yes")
