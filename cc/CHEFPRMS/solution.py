def is_prime(num):
    lim = int(pow(num, 0.5)) + 1
    for i in range(2, lim):
        if num % i == 0:
            return False
    return True


def is_sub_prime(num):
    lim = int(pow(num, 0.5)) + 1
    for i in range(2, lim):
        if num % i == 0 and is_prime(i) and is_prime(num / i) and i * i != num:
            return True
    return False


T = int(input())
for _ in range(T):
    N = int(input())
    if N < 4:
        print("NO")
        continue
    for i in range(2, N // 2 + 1):
        if is_sub_prime(i) and is_sub_prime(N - i):
            print("YES")
            break
    else:
        print("NO")
