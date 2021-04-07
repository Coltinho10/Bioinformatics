from os import listdir
from os.path import isfile, join
import numpy as np
import matplotlib.pyplot as mpl

s1 = []
s2 = []
s3 = []
fullname = 'test.txt'


def get_rna_seq_and_Seq_Struct(filename):
    file = open(fullname, 'r')
    while 1:
        # Get next line from file
        line = file.read(1)
        if line in 'AGCU':
            if line == 'A':
                s1.append('A')

            if line == 'C':
                s1.append('C')

            if line == 'G':
                s1.append('G')

            if line == 'U':
                s1.append('U')

        if line in '().':
            if line == '(':
                s2.append('(')

            if line == ')':
                s2.append(')')

            if line == '.':
                s2.append('.')
        # if line is empty
        # end of file is reached
        if not line:
            break

        if line.startswith('>'):
            next(file)
        for i in range(len(s2)):
            if s2[i] == '[' or ']' or '{' or '}':
                s2[i] == '.'

        [x.upper() for x in s1]
    #print(*s1, sep='')
    #print(*s2, sep='')


def count_bp(rna_seq, rna_sec_struct):
    count_au = 0
    count_gc = 0
    count_gu = 0
    final_count = 0
    for i in range(len(rna_sec_struct)):
        if rna_sec_struct[i] == '(':
            s3.append(i)

        if rna_sec_struct[i] == ')':
            close_index = i
            open_index = s3.pop()

            if rna_seq[open_index] == 'A' and rna_seq[close_index] == 'U':
                count_au += 1
            if rna_seq[open_index] == 'U' and rna_seq[close_index] == 'A':
                count_au += 1

            if rna_seq[open_index] == 'G' and rna_seq[close_index] == 'U':
                count_gu += 1
            if rna_seq[open_index] == 'U' and rna_seq[close_index] == 'G':
                count_gu += 1

            if rna_seq[open_index] == 'G' and rna_seq[close_index] == 'C':
                count_gc += 1
            if rna_seq[open_index] == 'C' and rna_seq[close_index] == 'G':
                count_gc += 1
    total_count = count_gu + count_au + count_gc
    au_perc = count_au / total_count
    gu_perc = count_gu / total_count
    gc_perc = count_gc / total_count
    final_count += total_count

    return count_gc, count_au, count_gu


def get_filename():
    total_au_count = 0
    total_gu_count = 0
    total_gc_count = 0
    dir_path = 'real_sec_structures'
    for f in listdir(dir_path):
        full_name = join(dir_path, f)
        if isfile(full_name):
            #print(full_name)
            get_rna_seq_and_Seq_Struct(fullname)
            count_bp(s1, s2)
            au, gu, gc = count_bp(s1, s2)
            total_au_count += au
            total_gc_count += gc
            total_gu_count += gu
            total_overall = total_gc_count + total_au_count + total_gu_count
            gu_perc = total_gu_count / total_overall
            au_perc = total_au_count / total_overall
            gc_perc = total_gc_count / total_overall
    data = {'GU': total_gu_count, 'GC': total_gc_count, 'AU': total_au_count}
    basepairs = list(data.keys())
    values = list(data.values())
    graph = mpl.figure(figsize=(10, 5))
    mpl.bar(basepairs, values, color='blue', width=0.4)
    mpl.xlabel("Basepair Types")
    mpl.ylabel("Total Number of each Basepair type")
    mpl.title("Basepairs in RNA sequences")
    mpl.show()
    data2 = {'GU': gu_perc, 'GC': gc_perc, 'AU': au_perc}
    basepairs2 = list(data2.keys())
    values2 = list(data2.values())
    graph2 = mpl.figure(figsize=(10, 5))
    mpl.bar(basepairs2, values2, color='blue', width=0.4)
    mpl.xlabel("Basepair Types")
    mpl.ylabel("Percentrage of each Basepair type")
    mpl.title("Percentage of basepairs in RNA sequences")
    mpl.show()


def main():
    get_filename()


if __name__ == '__main__':
    main()
