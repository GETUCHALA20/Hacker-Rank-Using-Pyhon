#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
# Complete the acmTeam function below.
def acmTeam(topic):
    all = combinations(topic,2)
    maximum = 0
    for pair in all:
        count = bin(int(pair[0], 2) | int(pair[1], 2)).count('1')
        if maximum < count:
            maximum = count
            c =0
        if count == maximum:
            c+=1
    return [maximum,c]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
