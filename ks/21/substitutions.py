from io import StringIO
import sys
from time import time
from os.path import basename

program_name = basename(sys.argv[0]).rstrip(".py")
with open(f"input_{program_name}.txt") as f:
    sys.stdin = StringIO(f.read())

start = time()
# cook your dish here
import sys

input = lambda: sys.stdin.readline().strip()


def solve():
    n = int(input())
    s = input()
    prev_str = ""
    while prev_str != s:
        prev_str = s
        for k, v in maps.items():
            s = s.replace(k, v)

    return s


maps = {
    "01": "2",
    "12": "3",
    "23": "4",
    "34": "5",
    "45": "6",
    "56": "7",
    "67": "8",
    "78": "9",
    "89": "0",
    "90": "1",
}

T = int(input())
for t in range(1, T + 1):
    r = solve()
    print(f"Case #{t}: {r}")

print("Execution took", time() - start, "s")
