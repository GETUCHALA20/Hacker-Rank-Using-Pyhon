#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    rows = []
    for i in range(len(container)):
        rows.append(sum(container[i]) )

    columns = []
    for i in range(len(container)):
        n = 0
        for j in range(len(container)):
            n += container[j][i]
        columns.append(n)
    
    if sorted(rows) == sorted(columns):
        return 'Possible'
    else:
        return 'Impossible'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
