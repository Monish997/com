from io import StringIO
import sys
from time import time
from os.path import basename

program_name = basename(sys.argv[0]).rstrip(".py")
with open(f"input_{program_name}.txt") as f:
    sys.stdin = StringIO(f.read())

# cook your dish here
import sys

input = lambda: sys.stdin.readline().strip()


def solve():
    n = int(input())
    p = input()
    maps = {
        "U": set(),
        "R": {"R"},
        "Y": {"Y"},
        "B": {"B"},
        "O": {"R", "Y"},
        "P": {"R", "B"},
        "G": {"Y", "B"},
        "A": {"R", "Y", "B"},
    }
    squares = [maps[p[i]] for i in range(n)]
    strokes = 0
    prev_sq = set()
    for sq in squares:
        strokes += len(set.difference(sq, prev_sq))
        prev_sq = sq

    return strokes


start = time()
T = int(input())
for t in range(T):
    y = solve()
    print(f"Case #{t + 1}: {y}")

print("Execution took", time() - start, "s")
