# Maria plays college basketball and wants to go pro. Each season she maintains a record of her paly. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

# Example:
# scores = [12, 24, 10, 24]
# Scores are in the same order as teh games played. She tabulates her results as follows:

# Game  Score    Minimum    Maximum     Min Max
#  0     12         12         12        0   0
#  0     24         12         24        0   1
#  0     10         10         24        1   1
#  0     24         10         24        1   1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    # Write your code here
    init = scores[0]
    mini = [init]
    maxi = [init]
    for i in range(len(scores)):
        if scores[i] < init and scores[i] < min(mini):
            mini.append(scores[i])
        elif scores[i] > init and scores[i] > max(maxi):
            maxi.append(scores[i])

    return [(len(maxi) - 1), (len(mini) - 1)]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
