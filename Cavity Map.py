#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    points = []
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid)-1):
            val = int(grid[i][j])
            if int(grid[i-1][j]) < val  and int(grid[i+1][j]) < val and int(grid[i][j-1]) < val and int(grid[i][j+1]) < val:
                points.append((i,j))
    for point in points:
        p = list(grid[point[0]])
        p[point[1]]="X"
        k = "".join([e for e in p])
        grid[point[0]] = k
    return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
