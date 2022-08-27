from time import perf_counter
from os.path import basename
import numpy as np

np.set_printoptions(threshold=np.inf)
with open("input.txt") as f:
    data = f.read().splitlines()

sep = data.index("")
dots, folds = data[:sep], data[sep + 1 :]
dots = [tuple(map(int, x.split(","))) for x in dots]
cols, rows = map(lambda x: max(x) + 1, zip(*dots))
grid = np.zeros((rows, cols), dtype=np.uint8)
for x, y in dots:
    grid[y, x] = 1


def solve(part):
    g = np.copy(grid)
    for f in folds:
        ax, val = f.split()[-1].split("=")
        val = int(val)
        if ax == "x":
            affected = g[:, 2 * val - cols + 1 : val]
            np.logical_or(affected, np.fliplr(g[:, val + 1 :]), out=affected)
            g = np.delete(g, slice(val, None), axis=1)
        else:
            affected = g[2 * val - rows + 1 : val, :]
            np.logical_or(affected, np.flipud(g[val + 1 :, :]), out=affected)
            g = np.delete(g, slice(val, None), axis=0)
        if part == 1:
            return np.where(g == 1)[0].size
    char_map = {0: " ", 1: "@"}
    return "\n".join([" ".join(map(char_map.get, row)) for row in g])

