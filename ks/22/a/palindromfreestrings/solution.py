def solve(s: str):
    if len(s) < 5:
        return "POSSIBLE"
    for i in range(len(s) - 5):
        if (
            s[i] == s[i + 4]
            and s[i] != "?"
            and s[i + 4] != "?"
            or s[i + 1] == s[i + 3]
            and s[i + 1] != "?"
            and s[i + 3] != "?"
        ):
            return "IMPOSSIBLE"


t = int(input())
for x in range(1, t + 1):
    s = input()
    print("Case #{}: {}".format(x, solve(s)))
