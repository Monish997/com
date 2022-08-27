T = int(input())
for _ in range(T):
    s1 = input()
    s2 = input()
    x = input()
    l1, l2, lx = len(s1), len(s2), len(x)
    seen = set()
    count = 0
    pairs = []
    for i in range(lx):
        for j in range(i, lx + 1):
            sub = x[i:j]
            if sub not in seen:
                seen.add(sub)
                for k in range(len(sub)):
                    p1 = sub[:k]
                    p2 = sub[k:]
                    if p1 in s1 and p2 in s2:
                        count += 1
                        pairs.append((p1, p2))
    print(count)
    print(pairs)
    print(all((pairs.count(p) == 1) for p in pairs))
