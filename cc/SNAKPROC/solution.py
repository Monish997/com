R = int(input())
for _ in range(R):
    L = int(input())
    report = input()
    counter = 0
    d = {"H": 1, ".": 0, "L": -1}
    for i in report:
        counter += d[i]
        if counter not in (0, 1):
            print("Invalid")
    print("Invalid" if counter != 0 else "Valid")
