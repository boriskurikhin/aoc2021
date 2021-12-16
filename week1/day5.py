#!/usr/bin/env Python3
# _delim = '\n'

from collections import defaultdict
with open('day5.txt', 'r') as f:
    lines, field = f.readlines(), defaultdict(int)

    for line in lines:
        a, b = line.split(' -> ')
        x,y = tuple(map(int, a.split(',')))
        x2,y2 = tuple(map(int, b.split(',')))
        if x == x2:
            for j in range(min(y, y2), max(y, y2) + 1):
                field[f'{x}|{j}'] += 1
        elif y == y2:
            for j in range(min(x, x2), max(x, x2) + 1):
                field[f'{j}|{y}'] += 1
        else:
            sy = min(y, y2)
            bottom = y == sy
            for _ in range(min(x, x2), max(x, x2) + 1):
                field[f'{x}|{y}' if bottom else f'{x2}|{y2}'] += 1
                if bottom:  y += 1; x = x - 1 if x >= x2 else x + 1
                else: y2 += 1; x2 = x2 - 1 if x2 >= x else x2 + 1

    ans = len(list(filter(lambda x: field[x] >= 2, field.keys())))
    print(ans)
