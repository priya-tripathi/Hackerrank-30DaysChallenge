#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    # binaryValue = (bin(n)[2:])
    # print(binaryValue)
    # count = 0
    # max =0
    # for i in range(len(binaryValue)):
    #     if binaryValue[i].__eq__("1"):
    #          count += 1
    #          i = i+1
    # print(count)
    # for i in range(len(binaryValue)):
    #     if binaryValue[i].__eq__("1"):
    #         count += 1
    #         continue
    #     if binaryValue[i].__eq__("0") and i > 0:
    #         if count > max:
    #             max=count
    #         count = 0
    # if count> max:
    #     print(count)
    # else:
    #     print(max)
    numbers = str(bin(n)[2:]).split('0')
    lengths = [len(num) for num in numbers]
    print(max(lengths))

