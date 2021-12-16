#!/usr/bin/env Python3
from copy import deepcopy
from heapq import heappush, heappop
from collections import Counter, defaultdict, deque
''' end of imports '''

file = open('day15.txt')

small_map = list(map(lambda x: x.strip(), file.readlines()))
N = len(small_map)
M = len(small_map[0])

for i in range(N):
    small_map[i] = list(map(int, small_map[i]))

full_map = [[0 for _ in range(M * 5)] for __ in range(N * 5)]

''' GO STUPID AHH GO CRAZY AHH '''
# copy the shit over since (0, 0) is the og
for y in range(N):
    for x in range(M):
        full_map[y][x] = small_map[y][x]

# go right, and set values to left + 1
for X in range(1, 5):
    for y in range(N):
        for x in range(M):
            full_map[y][X * M + x] = full_map[y][(X-1) * M + x] + 1
            if full_map[y][X * M + x] > 9:
                full_map[y][X * M + x] -= 9

# look up, and set values to up + 1
for Y in range(1, 5):
    for X in range(5):
        for y in range(N):
            for x in range(M):
                full_map[N * Y + y][M * X + x] = full_map[N * (Y-1) + y][M * X + x] + 1
                if full_map[N * Y + y][M * X + x] > 9:
                    full_map[N * Y + y][M * X + x] -= 9

N *= 5
M *= 5

Q = [(0, 0, 0)]
DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dist = defaultdict(lambda: float('inf'))

while Q:
    d, y, x = heappop(Q)
    if y == N - 1 and x == M - 1:
        print(d)
        break
    for yd, xd in DIRS:
        yy, xx = y + yd, x + xd
        if yy < 0 or xx < 0 or yy >= N or xx >= M:
            continue
        if d + full_map[yy][xx] < dist[(yy, xx)]:
            dist[(yy, xx)] = d + full_map[yy][xx]
            heappush(Q, (d + full_map[yy][xx], yy, xx,))