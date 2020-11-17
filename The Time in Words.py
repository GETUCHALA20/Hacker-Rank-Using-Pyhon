#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    d = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',
        7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve', 13:'thirteen',
        14:'fourthen',15:'quarter',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',21:'twenty one',22:'twenty two',23:'twenty three',24: 'twenty four',25:'twenty five', 26:'twenty six',27:'twenty seven', 28: 'twenty eight', 29: 'twenty nine',30:'half'}
        
    if m == 0:
        return d[h]+' o\' clock'
    elif m == 15 or m == 30:
        return d[m]+' past '+d[h]
    elif m == 1:
        return d[m]+' minute past '+d[h]
    elif m < 30:
        return d[m]+' minutes past '+d[h]
    else:
        k = 60-m
        h = h+1
        if k == 15 or k == 30:
            return d[k]+' to '+d[h]
        elif k == 1:
            return d[k]+' minute to '+d[h]
        elif k < 30:
            return d[k]+' minutes to '+d[h]
    
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
