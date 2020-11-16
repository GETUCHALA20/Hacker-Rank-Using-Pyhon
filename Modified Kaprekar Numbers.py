#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    res = ""
    for i in range(p,q+1):
        d = len(str(i))
        elSquare = i**2
        el_str = str(elSquare)
        if int(el_str[-d:]) + int(el_str[:-d] if len(el_str[:-d]) > 0 else 0) == i:
            res += " "
            res += str(i)
    if res == '':
        print("INVALID RANGE")
    else:
        print(res.strip())

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
