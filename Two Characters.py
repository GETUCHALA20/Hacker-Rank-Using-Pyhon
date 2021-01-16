#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
from itertools import combinations

# Complete the alternate function below.
def alternate(s):
    maximum = 0
    d = defaultdict(int)
    for elm in s:
        if d[elm]:
            d[elm] += 1
        else:
            d[elm] = 1
    unique = list(d.keys())
    comb = list(combinations(unique, 2))
    
    for elem in comb:
        copy_s = s[:]
        for e in s:
            if e not in elem:
                copy_s = copy_s.replace(e,'')
        flag = False
        for i in range(len(copy_s)-1):
            if copy_s[i] == copy_s[i+1]:
                flag = True
        if flag == False:
            if len(copy_s) > maximum:
                maximum = len(copy_s)
    return maximum
                
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
