# Enter your code here. Read input from STDIN. Print output to STDOUT

phoneBook = {}
n = int(input())
for i in range(n):
    entry = list(map(str, input().rstrip().split()))
    phoneBook[entry[0]] = entry[1]

test = ""
try:
    while test != None:
        test = str(input())
        if test is not None:
            if phoneBook.keys().__contains__(test):
                print(test + "=" + phoneBook[test])
            else:
                print("Not found")
except EOFError:
    pass