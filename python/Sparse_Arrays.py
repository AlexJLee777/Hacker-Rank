# There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

# Example:
# strings = ['ab', ' ab', 'abc']
# queries = ['ab', ' abc', ' bc']
# There are 2 instances of 'ab'. 1 of 'abc' and 0 of 'bc'. for each query, add an element to the return array, results = [2, 1, 0].

# Function Description:
# Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in strings.
# matchingStrings has the following parameters:
# - string strings[n] - an array of strings to search
# - string queries[q] - an array of query strings

# Returns:
# - int[q]: an array of results for each query

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#


def matchingStrings(strings, queries):
    # Write your code here
    arr = []
    for query in queries:
        cnt = 0
        for string in strings:
            if query == string:
                cnt += 1
        arr.append(cnt)
    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
