#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    if k == 0:
        return range(1,n+1)
    elif (n/k)%2!=0.0:
        return [-1]
    else:
        arr = []
        for i in range(1,n,k*2):
            d = list(range(i, i+k*2)) 
            arr+=d[k:]+d[:k]
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
