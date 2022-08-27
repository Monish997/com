T = int(input())
op = []
for _ in range(T):
    N, K = tuple(map(int, input().split()))
    scores = tuple(map(int, input().split()))
    sorted_scores = sorted(scores, reverse=True)
    threshold = sorted_scores[K - 1]
    qualified = filter(lambda x: x >= threshold, scores)
    print(sum(1 for _ in qualified))
