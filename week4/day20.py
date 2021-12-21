#!/usr/bin/env Python3
from copy import deepcopy
from heapq import heappush, heappop
from collections import Counter, defaultdict, deque
from functools import reduce, lru_cache
import math as m
import numpy as np
import time
''' end of imports '''
image = list(map(lambda x:x.strip(), open('day20.txt').readlines()))

algo = image[0]
image = image[2:]

N = len(image)
M = len(image[0])

assert N==M, 'N is not M'

for i in range(N):
    image[i] = list(image[i])

''' functions '''
def find_pixel(r, c, arr, fill='0'):
    value = ''
    for i in [r-1, r ,r+1]:
        for j in [c-1, c, c+1]:
            try: value += '0' if arr[i][j] == '.' else '1'
            except: value += fill
    return algo[int(value, 2)]

''' end of functions '''
padding = 200

picture = [['.' for _ in range(padding * 2 + M)] for __ in range(padding * 2 + N)]
for i in range(N):
    for j in range(M):
        picture[padding+i][padding+j] = image[i][j]

for step in range(50):
    print(step)
    new_picture = [['.' for _ in range(padding * 2 + M)] for __ in range(padding * 2 + N)]
    for i in range(len(picture)):
        for j in range(len(picture[i])):
            new_picture[i][j] = find_pixel(i, j, picture)
    picture = new_picture

print(sum(r[100:-100].count('#') for r in picture[100:-100]))
