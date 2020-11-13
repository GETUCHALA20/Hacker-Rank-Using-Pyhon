#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s = s.strip()
    s = "".join([word for word in s.split(" ")])
    L = len(s)
    fl = math.floor(L**0.5)
    cl = math.ceil(L**0.5)
    if cl*fl < L:
        fl = fl+1
    formed_column = [s[cl*j:cl*(j+1)] for j in range(fl)]
    res = ""
    for i in range(cl):
        res+="".join([elem[i] if len(elem)-1>=i else "" for elem in formed_column])+" "
    return res.rstrip()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
