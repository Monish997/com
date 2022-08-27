T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    grid = [input() for _ in range(N)]
    distances = [0] * (N + M - 2)
    houses = [(i, j) for i in range(N) for j in range(M) if grid[i][j] == "1"]
    n_houses = len(houses)
    for i in range(n_houses):
        h1 = houses[i]
        for j in range(i + 1, n_houses):
            h2 = houses[j]
            dist = abs(h1[0] - h2[0]) + abs(h1[1] - h2[1])
            distances[dist - 1] += 1
    print(" ".join(map(str, distances)))
