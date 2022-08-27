import numpy as np

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    c = list(map(int, input().split()))
    cumfreq = np.zeros(n)
    scores = []
    h_index = 0
    for ci in c:
        cumfreq[:ci] += 1
        for j in range(h_index, n):
            if cumfreq[j] > j:
                h_index = j + 1
            else:
                break
        scores.append(h_index)
    print("Case #{}: {}".format(i, " ".join(map(str, scores))))
