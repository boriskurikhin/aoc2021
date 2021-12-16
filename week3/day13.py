#!/usr/bin/env Python3
from copy import deepcopy
''' end of imports '''

file = open('day13.txt')
lines = list(map(lambda x: x.strip(), file.readlines()))

right = float('-inf')
bottom = float('-inf')

for line in lines:
    if line == '': break
    x, y = list(map(int, line.split(',')))
    right = max(right, x + 1)
    bottom = max(bottom, y + 1)

grid = [['.' for _ in range(right)] for __ in range(bottom)]
idx = 0

for i, line in enumerate(lines):
    if line == '': 
        idx = i
        break
    x, y = list(map(int, line.split(',')))
    grid[y][x] = '#'


inst = lines[i+1:]

N = len(grid)
M = len(grid[0])

for line in inst:
    i, n = list(map(str, line.split('=')))
    n = int(n)
    if 'x' in i:
        MM = n
        ng = [['.' for _ in range(MM + 1)] for __ in range(N)]
        for y in range(N):
            for x in range(MM):
                ng[y][x] = grid[y][x]

        for y in range(N):
            for x in range(MM + 1, M):
                if grid[y][x] == '#':
                    ng[y][MM - (x - MM)] = '#'
        M = MM
        grid = ng
    else:
        NN = n
        ng = [['.' for _ in range(M)] for __ in range(NN + 1)]
        for y in range(NN):
            for x in range(M):
                ng[y][x] = grid[y][x]
        for y in range(NN + 1, N):
            for x in range(M):
                if grid[y][x] == '#':
                    ng[NN - (y - NN)][x] = '#'
        N = NN
        grid = ng

write = open('out.txt', 'w')
for r in grid:
    write.write(''.join(r).replace('#', '█').replace('.', ' ') + '\n')



# # close file
file.close()