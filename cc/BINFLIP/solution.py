def solve():
    n, k = map(int, input().split())
    i = 1
    indices = []
    while i < 30 and k >= 0:
        if k == 0:
            print("YES")
            print(len(indices))
            for j in indices:
                print(j)
            return
        if k < _range[i - 1]:
            print("NO")
            return
        k -= _range[i - 1]
        indices.append(k + 1)
        i += 1
    else:
        print("NO")


_range = [2 ** (i - 1) for i in range(1, 30)]


def presum(arr):
    ret = [0] * len(arr)
    ret[0] = arr[0]
    for i in range(1, len(arr)):
        ret[i] = ret[i - 1] + arr[i]
    return ret


T = int(input())
for _ in range(T):
    solve()
