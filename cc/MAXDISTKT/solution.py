T = int(input())
for _ in range(T):
    N = int(input())
    B = list(map(int, input().split()))
    C = [0] * N
    rems = set()
    for i in range(N):
        available = {j for j in range(B[i])} - rems
        rem = available.pop() if available != set() else 0
        rems.add(rem)
        C[i] = rem
    A = [x + y for x, y in zip(B, C)]
    print(" ".join(map(str, A)))
