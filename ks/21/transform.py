from io import StringIO
import sys
from time import time
from os.path import basename

program_name = basename(sys.argv[0]).rstrip(".py")
with open(f"input_{program_name}.txt") as f:
    sys.stdin = StringIO(f.read())

deb = lambda x: print(f"{x=}")

# You are given a string S which denotes a padlock consisting of lower case English letters. You are also given a string F consisting of set of favorite lower case English letters. You are allowed to perform several operations on the padlock. In each operation, you can change one letter of the string to the one following it or preceding it in the alphabetical order. For example: for the letter c, you are allowed to change it to either b or d in an operation. The letters can be considered in a cyclic order, i.e., the preceding letter for letter a would be letter z. Similarly, the following letter for letter z would be letter a.

# Your aim is to find the minimum number of operations that are required such that each letter in string S after applying the operations, is present in string F.

# cook your dish here
import sys

input = lambda: sys.stdin.readline().strip()


def solve():
    s = input()
    f = input()
    count = 0
    for i in range(len(s)):
        ord_char = ord(s[i])
        if s[i] not in f:
            mindiff = 26
            for j in range(len(f)):
                ord_target = ord(f[j])
                straight = abs(ord_target - ord_char)
                cycle = 26 - straight
                if straight < mindiff or cycle < mindiff:
                    mindiff = min(cycle, straight)
                    if mindiff == 1:
                        break
            count += mindiff
    return count


start = time()
T = int(input())
for t in range(T):
    count = solve()
    print(f"Case #{t+1}: {count}")

print("Execution took", time() - start, "s")
