from copy import deepcopy
import numpy as np

def zero_padded(array):
    r, c = array.shape
    zparray = np.zeros((r + 2, c + 2))
    zparray[1:-1, 1:-1] = array
    return zparray


def trimmed(array):
    array = deepcopy(array)
    while not any(array[0]):
        array.pop(0)
    while not any(array[-1]):
        array.pop()
    transposed = [list(i) for i in zip(*array)]
    while not any(transposed[0]):
        transposed.pop(0)
    while not any(transposed[-1]):
        transposed.pop()
    ret = [list(i) for i in zip(*transposed)]
    return ret if ret else [[0]]


def alive_neighbors(cells, r, c):
    alive = 0
    rows, cols = len(cells), len(cells[0])
    if r > 0:
        alive += cells[r - 1][c]
        if c > 0:
            alive += cells[r - 1][c - 1]
        if c < cols - 1:
            alive += cells[r - 1][c + 1]
    if r < rows - 1:
        alive += cells[r + 1][c]
        if c > 0:
            alive += cells[r + 1][c - 1]
        if c < cols - 1:
            alive += cells[r + 1][c + 1]
    if c > 0:
        alive += cells[r][c - 1]
    if c < cols - 1:
        alive += cells[r][c + 1]
    return alive


def get_generation(cells, n):
    for _ in range(n):
        cells = zero_padded(cells)
        next_gen = deepcopy(cells)
        for r in range(len(cells)):
            for c in range(len(cells[0])):
                n_alive = alive_neighbors(cells, r, c)
                if cells[r][c] and (n_alive < 2 or n_alive > 3):
                    next_gen[r][c] = 0
                elif not cells[r][c] and n_alive == 3:
                    next_gen[r][c] = 1
        cells = trimmed(next_gen)
    return cells


def pretty_print(cells):
    mapping = {0: ".", 1: "#"}
    for row in cells:
        print("".join(mapping[cell] for cell in row))


start = np.array([
    [1, 0, 0],
    [0, 1, 1],
    [1, 1, 0],
])
end = np.array([
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
])


for i in range(10):
    gen = get_generation(start, i)
    pretty_print(gen)
    print()
