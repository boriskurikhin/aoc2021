#!/usr/bin/env Python3


''' end of imports '''

file = open('day11.txt')
from copy import deepcopy
lines = []

for l in file.readlines():
    l = l.strip()
    lines.append(list(map(int, list(l))))

N = len(lines)
M = len(lines[0])
flash = 0

for _ in range(99999999):
    flashing = set()
    flipped = set()

    for i in range(N):
        for j in range(M):
            lines[i][j] += 1
            if lines[i][j] > 9:
                flashing.add((i, j))

    while True:
        to_extend = set()
        for entry in flashing:
            if entry in flipped:
                continue
            flipped.add(entry)
            x, y = entry

            for xd, yd in [(-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1)]:
                i = x + xd
                j = y + yd
                if i < 0 or j < 0 or i >= N or j >= M:
                    continue
                lines[i][j] += 1
                if lines[i][j] > 9:
                    to_extend.add((i, j))

        if not len(to_extend):
            break

        [flashing.add(entry) for entry in to_extend]

    if len(flashing) == N * M:
        print('step', _)
        break

    for entry in flashing:
        x, y = entry
        if lines[x][y] > 9:
            lines[x][y] = 0
            flash += 1

print(flash)
