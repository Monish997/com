S = int(input())
for _ in range(S):
    N = int(input())
    H = tuple(map(int, input().split()))
    if len(H) % 2 != 1 or H[0] != 1:
        print("no")
        continue
    mid_index = len(H) // 2
    mid = H[mid_index]
    for i in range(mid):
        if not H[i] == H[mid_index + i + 1] == i + 1:
            print("no")
            break
    else:
        print("yes")
