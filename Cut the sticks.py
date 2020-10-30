#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    if len(arr) == 1:
        return [1]
    elif len(arr) == 0:
        return []
    length = len(arr)
    mini = min(arr)
    for i in range(len(arr)):
        arr[i] -= mini
    arr = [arr[i] for i in range(len(arr)) if arr[i] != 0]
    return [length] + cutTheSticks(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
