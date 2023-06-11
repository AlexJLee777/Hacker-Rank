# Given an array of integers, calculated the ratios of its elements that are positive, negative and zero.
# Print the decimal value of each fraction on a new line with 6 places after the decimal.

# Note:
# This challenge introduces precision problems.
# The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.

# Example:
# arr = [1,1,0,-1,-1]
# There are n=5 elements, two positive, two negative and one zero. Their ratios are 0.4, 0.4, 0.2.
# The Results are printed as:
# 0.4
# 0.4
# 0.2

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    n = len(arr)
    zeros = arr.count(0)
    if zeros == 0:
        arr.append(0)
        zeros = 1
    arr = sorted(arr)
    negatives = arr.index(0)
    positives = n - zeros - negatives
    print(positives/n)
    print(negatives/n)
    print(zeros/n)
    # Write your code here


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
