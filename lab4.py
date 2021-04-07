import numpy as np
s1 = 'GCACU'
s2 = 'UUGA'


def seq_alignment(s1, s2):
    M = np.zeros((len(s1) + 1, len(s2) + 1))
    i = 0
    for x in M:
        j = 0
        for _ in x:
            if i != 0 and j != 0:
                if s1[i - 1] == s2[j - 1]:
                    M[i][j] = M[i-1][j-1] + 1
                if s1[i - 1] != s2[j - 1]:
                    if M[i - 1][j] > M[i][j]:
                        M[i][j] = M[i - 1][j]
                    if M[i][j - 1] > M[i][j]:
                        M[i][j] = M[i][j - 1]
            j += 1
        i += 1
    print(M[i - 1][j - 1])


def main():
    seq_alignment(s1, s2)


if __name__ == '__main__':
    main()
