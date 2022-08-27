T = int(input())
hand = {"d": "left", "f": "left", "j": "right", "k": "right"}

for _ in range(T):
    seen = set()
    N = int(input())
    words = [input() for _ in range(N)]
    time = 0
    for word in words:
        prev = word[0]
        word_time = 2
        for char in word[1:]:
            word_time += 2 if hand[prev] != hand[char] else 4
            prev = char
        time += word_time if word not in seen else word_time / 2
        seen.add(word)
    print(int(time))
