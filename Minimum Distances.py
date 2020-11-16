#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    res = []
    for i in range(len(a)-1):
        if a[i] in a[i+1:]:
            index = a[i+1:].index(a[i]) + len(a[:i+1])
            res.append(index-i)
    return min(res) if len(res) > 0 else -1
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
