# Given an array, , of  integers, print 's elements in reverse
# order as a single line of space-separated numbers.



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    for x in arr:
        print(x, end=' ')