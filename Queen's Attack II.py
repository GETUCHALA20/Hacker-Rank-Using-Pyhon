#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    obs = {}
    total = 0
    
    for i, j in obstacles:
        if i in obs:
            obs[i][j] = 1
        else:
            obs[i] = {j:1}
    def limit(x,y):
        return True if 1<=x<=n and 1<=y<=n else False
    def check(x,y,xi,yi):
        count = 0
        x+= xi
        y+= yi
        while limit(x,y) and obs.get(x,{}).get(y,0) == 0:
            count+= 1
            x+= xi
            y+= yi
        return count
    r = [0,0,-1,1,-1,1,-1,1]
    c = [1,-1,0,0,-1,1,1,-1]
    
    for i,j in zip(r,c):
        total+= check(r_q,c_q,i,j)

    return total
                
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
