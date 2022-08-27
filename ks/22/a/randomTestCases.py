import random
from os.path import abspath, dirname


def testcase():
    bounds = [random.randint(1, 10 ** 12) for _ in range(2)]
    bounds.sort()
    return " ".join(map(str, bounds))


bd = dirname(abspath(__file__))
pn = "interestingintegers"
with open(f"{bd}/in/{pn}.txt", "w") as f:
    f.write("100\n")
    for x in range(100):
        f.write(testcase() + "\n")
