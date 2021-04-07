import numpy as np

s1 = 'TTCATA'
s2 = 'TGCTCGTA'
length_s1 = len(s1) + 1
length_s2 = len(s2) + 1
diagonal = '↖'
up = '↑'
left = '←'
stack1 = []
stack2 = []


def print_alignment(s1, s2):
    pairs = 0
    M = np.zeros((length_s1, length_s2))
    BT = [['s' for x in range(length_s2)] for y in range(length_s1)]
    i = 0
    for x in M:
        j = 0
        for y in x:
            if i != 0 and j != 0:
                if s1[i - 1] == s2[j - 1]:
                    M[i][j] = M[i - 1][j - 1] + 1
                    BT[i][j] = diagonal

                if M[i][j - 1] > M[i][j]:
                    M[i][j] = M[i][j - 1]
                    BT[i][j] = left

                if s1[i - 1] != s2[j - 1]:
                    if M[i - 1][j] > M[i][j]:
                        M[i][j] = M[i - 1][j]
                        BT[i][j] = up

            j += 1
        i += 1
    i = len(s1)
    j = len(s2)
    print(M)
    print(np.matrix(BT))

    while BT[i][j] != 's':
        if BT[i][j] == '↖':
            stack1.append(s1[i - 1])
            stack2.append(s2[j - 1])
            i = i - 1
            j = j - 1

        if BT[i][j] == '←':
            stack1.append('-')
            stack2.append(s2[j - 1])
            j = j - 1

        if BT[i][j] == '↑':
            stack1.append(s1[i - 1])
            stack2.append('-')
            i = i - 1


    stack1.reverse()
    stack2.reverse()
    print(*stack1, sep='')
    print(*stack2, sep='')

    for i in range(len(stack1)):
        if stack1.pop() == stack2.pop():
            pairs = pairs + 1
    print(pairs)


def main():
    print_alignment(s1, s2)


if __name__ == '__main__':
    main()
