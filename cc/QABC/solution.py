T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for i in range(N - 2):
        diff = B[i] - A[i]
        if diff < 0:
            print("NIE")
            break
        elif diff > 0:
            A[i] += diff
            A[i + 1] += 2 * diff
            A[i + 2] += 3 * diff
    else:
        print("TAK" if A == B else "NIE")
