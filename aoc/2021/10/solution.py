from statistics import median

with open("input.txt") as f:
    data = f.read().splitlines()
n_lines = len(data)


def part1():
    open_chars = ["(", "[", "{", "<"]
    close_chars = [")", "]", "}", ">"]
    open2close = dict(zip(open_chars, close_chars))
    score_dict = dict(zip(close_chars, [3, 57, 1197, 25137]))
    score = 0
    for _ in range(n_lines):
        line = input()
        opened = [line[0]]
        for char in line[1:]:
            if char in open_chars:
                opened.append(char)
            elif open2close[opened[-1]] == char:
                opened.pop()
            else:
                score += score_dict[char]
                break
    return score


def part2():
    lines = [input() for _ in range(n_lines)]
    open_chars = ["(", "[", "{", "<"]
    close_chars = [")", "]", "}", ">"]
    open2close = dict(zip(open_chars, close_chars))
    incomplete = []
    for line in lines:
        opened = [line[0]]
        for char in line[1:]:
            if char in open_chars:
                opened.append(char)
            elif open2close[opened[-1]] == char:
                opened.pop()
            else:
                break
        else:
            rem = map(open2close.get, reversed(opened))
            incomplete.append(rem)

    score_dict = dict(zip(close_chars, [1, 2, 3, 4]))
    scores = []
    for rem in incomplete:
        score = 0
        for char in rem:
            score *= 5
            score += score_dict[char]
        scores.append(score)

    return median(scores)

