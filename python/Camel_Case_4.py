# Camel Case is a naming style common in many programming languages. In Java, method and variable names typically start with a lowercase letter, with all subsequent words starting with a capital letter (example: startThread). Names of classes follow the same pattern, except that they start with a capital letter (example: BlueCar).

# Your task is to write a program that creates or splits Camel Case variable, method, and class names.

# Input Format:
# - Each line of the input file will begin with an operation (S or C) followed by a semi-colon followed by M, C, or V followed by a semi-colon followed by the words you'll need to operate on.
# - The operation will either be S (split) or C (combine)
# - M indicates method, C indicates class, and V indicates variable
# - In the case of a split operation, the words will be a camel case method, class or variable name that you need to split into a space-delimited list of words starting with a lowercase letter.
# - In the case of a combine operation, the words will be a space-delimited list of words starting with lowercase letters that you need to combine into the appropriate camel case String. Methods should end with an empty set of parentheses to differentiate them from variable names.

# Output Format:
# - For each input line, your program should print either the space-delimited list of words (in the case of a split operation) or the appropriate camel case string (in the case of a combine operation).

#!/bin/python3

import math
import os
import random
import re
import sys


def formatName(s):
    nameArr = s.rsplit(';')
    op = nameArr[0]
    _type = nameArr[1]
    subject = nameArr[2]
    subjectList = subject.split(
        " ") if " " in subject else re.findall(".[^A-Z]*", subject)

    if (op == 'S'):
        print(splitSubject(subjectList, _type))
    else:
        print(combineSubject(subjectList, _type))


def splitSubject(subjectList, _type):
    return " ".join(subjectList).lower().replace("()", "")


def combineSubject(subjectList, _type):

    firstWord = subjectList[0]
    otherWords = " ".join(subjectList[1:]).title()

    if _type == "M":
        otherWords += "()"
    elif _type == "C":
        firstWord = firstWord.capitalize()

    return firstWord + otherWords.replace(" ", "")


if __name__ == '__main__':
    for line in sys.stdin:
        line = line.rstrip()
        if 'Exit' == line:
            break
        formatName(line)
