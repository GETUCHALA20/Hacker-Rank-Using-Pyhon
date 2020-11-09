#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    d = {}
    for elem in arr:
        if elem in d.keys():
            d[elem]+=1
        else:
            d[elem]=1
    
    maximum = max(list(d.values()))
    return len(arr) - maximum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
