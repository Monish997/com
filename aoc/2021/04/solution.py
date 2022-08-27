from collections import defaultdict

with open("input.txt") as f:
    data = f.read().splitlines()
    totalLines = len(data)
    totalBoards = int((totalLines - 1) / 6)

input = lambda: data.pop(0)

nums = input().split(",")
num_map = defaultdict(list)

boards = []
for i in range(totalBoards):
    _ = input()
    board = []
    for j in range(5):
        row = input().split()
        for k, n in enumerate(row):
            num_map[n].append((i, j, k))
        board.append(row)
    boards.append(board)


def getWinningBoard(boards):
    for board in boards:
        for row in board:
            if all(x == "x" for x in row):
                return board
        for col in zip(*board):
            if all(x == "x" for x in col):
                return board
    return


def part1():
    for num in nums:
        for loc in num_map[num]:
            i, j, k = loc
            boards[i][j][k] = "x"
        winner = getWinningBoard(boards)
        if winner:
            unmarked = [i for row in winner for i in row if i != "x"]
            return sum(map(int, unmarked)) * int(num)


def getLosingBoard(boards):
    for board in boards:
        if all(row.count("x") < 5 for row in board) and all(
            col.count("x") < 5 for col in zip(*board)
        ):
            return board
    return


def part2():
    boards = [[["x"] * 5 for _ in range(5)] for _ in range(totalBoards)]

    for num in reversed(nums):
        for loc in num_map[num]:
            i, j, k = loc
            boards[i][j][k] = num
        loser = getLosingBoard(boards)
        if loser:
            for loc in num_map[num]:
                i, j, k = loc
                boards[i][j][k] = "x"
            unmarked = [i for row in loser for i in row if i != "x"]
            return sum(map(int, unmarked)) * int(num)
