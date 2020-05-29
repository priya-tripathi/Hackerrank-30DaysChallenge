# Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed
# characters as  space-separated strings on a single line (see the Sample below for more detail).

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        example = input()
        temp1 = ""
        temp2 = ""
        for x in range(len(example)):
            if x % 2 == 0:
                temp1 += example[x]
            else:
                temp2 += example[x]
        print(temp1 + " " + temp2)
