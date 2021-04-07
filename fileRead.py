import numpy as np
import matplotlib.pyplot as mpl


def readFile():
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0
    count = 0
    file1 = open("thermophile.fasta", 'r')
    while 1:
        # Get next line from file
        line = file1.read(1)

        if line == 'A':
            a_count += 1
            count += 1

        if line == 'C':
            c_count += 1
            count += 1

        if line == 'G':
            g_count += 1
            count += 1

        if line == 'T':
            t_count += 1
            count += 1

        # if line is empty
        # end of file is reached
        if not line:
            break

        if line.startswith('>'):
            next(file1)
        # print("Line{}: {}".format(count, line.strip()))
    a_percent = a_count / count
    g_percent = g_count / count
    c_percent = c_count / count
    t_percent = t_count / count
    data = {'A': a_count, 'C': c_count, 'G': g_count, 'T': t_count}
    nucleotides = list(data.keys())
    values = list(data.values())
    graph = mpl.figure(figsize=(10, 5))
    mpl.bar(nucleotides, values, color='blue', width=0.4)
    mpl.xlabel("Nucleotide types")
    mpl.ylabel("Total number of each nucleotide")
    mpl.title("Nucleotides in a Thermophile")
    mpl.show()
    file1.close()


def main():
    readFile()


if __name__ == '__main__':
    main()
