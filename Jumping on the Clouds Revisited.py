#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    i = 0
    energy = 100
    if c[0] == 1:
        energy -= 2
    while (i+k)%len(c) != 0:
        if c[(i+k)%len(c)] == 0:
            energy -= 1
        else:
            energy -=3
        i = (i+k)%len(c)
    return energy-1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
