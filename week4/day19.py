#!/usr/bin/env Python3
from copy import deepcopy
from heapq import heappush, heappop
from collections import Counter, defaultdict, deque
from functools import reduce, lru_cache
import math as m
import numpy as np
''' end of imports '''

REMPAS = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
INVERSE = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]

def rotate_points(points, remap, inverse):
    new_points = set()
    for point in points:
        new_points.add((
            point[remap[0]]*inverse[0],
            point[remap[1]]*inverse[1],
            point[remap[2]]*inverse[2]))
    return new_points

def translate_points(points, offset):
    new_points = set()
    for point in points:
        x,y,z = point
        xd,yd,zd = offset
        new_points.add((x+xd, y+yd, z+zd))
    return new_points

''' end of functions'''

file = open('day19.txt')
lines = list(map(lambda x: x[:-1], file.readlines()))

relative_points = defaultdict(set)
final_points = dict()
scanner_names = [lines[0]]

current = lines[0]
for i in range(1, len(lines)):
    if 'scanner' in lines[i]:
        current = lines[i]
        scanner_names.append(current)
    elif len(lines[i]) == 0: continue
    else: relative_points[current].add(tuple(map(int, lines[i].split(','))))

final_points[scanner_names[0]] = relative_points[scanner_names[0]]
checked = set([scanner_names[0]]) # assume these are good
offsets = set([(0, 0, 0)])

def loop(known_points, scan):
    for rm in REMPAS:
        for iv in INVERSE:
            rotated_points = rotate_points(
                relative_points[scan], rm, iv)
            for kp in known_points:
                for rp in rotated_points:
                    offset = (kp[0] - rp[0], kp[1] - rp[1], kp[2] - rp[2])
                    translated_points = translate_points(rotated_points, offset)
                    if len(translated_points & known_points) >= 12:
                        offsets.add(offset)
                        return translated_points
    return None

while len(final_points.keys()) < len(relative_points.keys()):
    for scan in scanner_names:
        if scan in final_points: continue
        known_points = set()
        for x, y in final_points.items():
            known_points |= y
        discovered = loop(known_points, scan)
        if discovered is not None:
            final_points[scan] = discovered
        
known_points = set()
for x, y in final_points.items():
    known_points |= y

offsets = list(offsets)
largest = float('-inf')
N = len(offsets)

for i in range(N):
    for j in range(i + 1, N):
        x,y,z = offsets[i]
        a,b,c, = offsets[j]
        largest = max(largest, abs(x-a) + abs(y-b) + abs(z-c))

print(largest)

