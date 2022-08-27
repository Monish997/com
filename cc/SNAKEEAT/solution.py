def solution(n, arr, prefixSum, k):
    if arr[0] >= k:
        return n

    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] < k:
            temp = mid
            l = mid + 1
        elif arr[mid] >= k:
            r = mid - 1

    ans = n - 1 - temp
    l = 0
    r = temp
    newtemp = 0
    while l <= r:
        mid = (l + r) // 2
        requiredSum = (temp - mid + 1) * k
        if mid != 0:
            haveSum = prefixSum[temp] - prefixSum[mid - 1]
        else:
            haveSum = prefixSum[r]
        snakeRequired = requiredSum - haveSum
        snakeWeHave = mid
        # print(l,r,mid,requiredSum,haveSum,snakeRequired,snakeWeHave)
        if snakeWeHave >= snakeRequired:
            newtemp = max(temp - mid + 1, newtemp)
            r = mid - 1
        else:
            l = mid + 1

    ans += newtemp
    return ans


for _ in range(int(input())):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    prefixSum = [0] * (n)
    prefixSum[0] = arr[0]
    for i in range(1, n):
        prefixSum[i] = arr[i] + prefixSum[i - 1]

    for _ in range(q):
        k = int(input())
        temp = solution(n, arr, prefixSum, k)
        print(temp)
