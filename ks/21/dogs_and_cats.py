from io import StringIO
import sys
from time import time
from os.path import basename

program_name = basename(sys.argv[0]).rstrip(".py")
with open(f"input_{program_name}.txt") as f:
    sys.stdin = StringIO(f.read())

deb = lambda x: print(f"{x=}")
# cook your dish here
import sys

input = sys.stdin.readline


def solve():
    N, D, C, M = map(int, input().split())
    S = input()
    last_dog = -1
    for i in range(N - 1, -1, -1):
        if S[i] == "D":
            last_dog = i
            break
    for i in range(last_dog + 1):
        a = S[i]
        if a == "D":
            if D:
                D -= 1
                C += M
            else:
                print("NO")
                return
        elif a == "C":
            if C:
                C -= 1
            elif i < last_dog:
                print("NO")
                return
    else:
        print("YES")
        return


def presum(arr):
    ret = [0] * len(arr)
    ret[0] = arr[0]
    for i in range(1, len(arr)):
        ret[i] = ret[i - 1] + arr[i]
    return ret


start = time()
T = int(input())
for _ in range(T):
    solve()

end = time()
print("Execution took", end - start, "s")
