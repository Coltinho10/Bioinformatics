import math

M = 502
c = [50, 25, 5, 1]
d = len(c)

c1 = [M // i for i in c]
max_val = (((c1[0]) + 1) * ((c1[1]) + 1) * ((c1[2]) + 1) * ((c1[3]) + 1)) - 1


def brute_force_change(M, c):
    best_change = [0, 0, 0, 0]
    smallest_num_coins = 9999999999
    for i in range(0, max_val + 1):
        tup = to_digits(i)
        val_coins = ((tup[0] * c[0]) + (tup[1] * c[1]) + (tup[2] * c[2]) + (tup[3] * c[3]))
        if val_coins == M:
            num_coins = sum(tup)
            if num_coins < smallest_num_coins:
                smallest_num_coins = num_coins
                best_change = tup
    return best_change


def to_digits(n):
    row = []
    for i in range(len(c) - 1, -1, -1):
        temp = n % (c1[i] + 1)
        row.append(temp)
        n //= (c1[i] + 1)
    row.reverse()
    return row


def main():
    test = brute_force_change(M, c)
    print(test)


if __name__ == '__main__':
    main()


