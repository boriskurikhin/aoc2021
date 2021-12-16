#!/usr/bin/env Python3

file = open('day9.txt')
lines = list(map(lambda x: x.strip(), file.readlines()))

N = len(lines)
M = len(lines[0])
SEEN = set()

def count_basin(x, y):
    if x < 0 or y < 0 or x >= N or y >= M:
        return 0
    in_basin = 1
    for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        xx = x + a
        yy = y + b
        if (xx, yy) not in SEEN and xx >= 0 and yy >= 0 and xx < N and yy < M \
            and int(lines[x][y]) < int(lines[xx][yy]) and int(lines[xx][yy]) < 9 :
            SEEN.add((xx, yy))
            in_basin += count_basin(xx, yy)
    return in_basin

BASINS = []

ans = 0
for i in range(N):
    for j in range(M):
        found = 0
        better = 0
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            xx = i + x
            yy = j + y
            if 0 <= xx < N and 0 <= yy < M:
                found += 1
                if int(lines[i][j]) < int(lines[xx][yy]):
                    better += 1
        if found == better and int(lines[i][j]) != 9:
            SEEN.add((i, j))
            BASINS.append(count_basin(i, j))
        ans += int(lines[i][j]) + 1

BASINS.sort()
print(BASINS[-3:])
print(BASINS[-1] * BASINS[-2] * BASINS[-3])