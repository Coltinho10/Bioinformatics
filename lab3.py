from os import listdir
from os.path import isfile, join

s1 = []
s2 = []
fullname = 'test.txt'


def get_RNAseq_and_Seq_Struct(filename):
    file1 = open(fullname, 'r')
    while 1:
        # Get next line from file
        line = file1.read(1)
        if line in 'AGCU':
            if line == 'A':
                s1.append('A')

            if line == 'C':
                s1.append('C')

            if line == 'G':
                s1.append('G')

            if line == 'T':
                s1.append('T')

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
            next(file1)
    print(*s1, sep='')
    print(*s2, sep='')


def get_filename():
    dir_path = 'real_sec_structures'
    for f in listdir(dir_path):
        full_name = join(dir_path, f)
        if isfile(full_name):
            print(full_name)
            get_RNAseq_and_Seq_Struct(fullname)


def main():
    get_filename()


if __name__ == '__main__':
    main()
