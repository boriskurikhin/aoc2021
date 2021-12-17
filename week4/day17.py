#!/usr/bin/env Python3
from copy import deepcopy
from heapq import heappush, heappop
from collections import Counter, defaultdict, deque
from functools import reduce
''' end of imports '''

# the box
top, bottom, left, right = -78, -102, 135, 155

def check_hit(Y, X):
    return top >= Y >= bottom and left <= X <= right

def alter(Y, X, dy, dx):
    return Y + dy, X + dx, dy - 1, (dx - 1 if dx > 0 else dx + 1 if dx < 0 else 0)

def simulate(Y, X, dy, dx):
    while Y > top and X < left:
        Y, X, dy, dx = alter(Y, X, dy, dx)
    while Y >= bottom and X <= right:
        if check_hit(Y, X): return True
        Y, X, dy, dx = alter(Y, X, dy, dx)
    return False

ans, dist, N = 0, set(), 1000
[dist.add((yd, xd)) if simulate(0, 0, yd, xd) else None for yd in range(-N, N) 
                                                        for xd in range(0, N)]
print(len(dist))