T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    elapsed = 0
    count = 0
    for i in range(len(A)):
        if elapsed + B[i] <= A[i]:
            count += 1
        elapsed = A[i]
    print(count)
