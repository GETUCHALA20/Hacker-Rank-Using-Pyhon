#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    res = m%n+(s-1)
    if n == 1:
        return 1
    if s == 1:
        if n != m:
            if m%n == 0:
                return n
            return m%n
        return n
    if res <= n:
        return res
    else:
        return res-n
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
