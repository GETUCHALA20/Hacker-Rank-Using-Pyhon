#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    tot = 0
    count = 0
    prevtot = 0
    for i in range(len(path)):
        if path[i] == 'U':
            tot+= 1
        else:
            tot-= 1
        if tot < 0 and prevtot >= 0:
            count += 1
        prevtot = tot
        
    return count
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
