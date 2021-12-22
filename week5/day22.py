#!/usr/bin/env Python3
from copy import deepcopy
from heapq import heappush, heappop
from collections import Counter, defaultdict, deque
from functools import reduce, lru_cache
import math
''' end of imports '''

class Cube:
    def __init__(self, xa, xb, ya, yb, za, zb):
        self.xa = xa
        self.xb = xb
        self.ya = ya
        self.yb = yb
        self.za = za
        self.zb = zb

    def __repr__(self):
        return f'x=({self.xa}, {self.xb}), y=({self.ya}, {self.yb}), z=({self.za}, {self.zb})'

    def volume(self):
        return (self.xb - self.xa) * (self.yb - self.ya) * (self.zb - self.za)

    def intersect(self, other):
        return max(self.xa, other.xa) < min(self.xb, other.xb) and max(self.ya, other.ya) < min(self.yb, other.yb) \
            and max(self.za, other.za) < min(self.zb, other.zb)

    def __hash__(self):
        return hash((self.xa, self.xb, self.ya, self.yb, self.za, self.zb))

    def __eq__(self, other):
        return all([self.xa==other.xa,self.xb==other.xb,self.ya==other.ya,
                    self.yb==other.yb, self.za==other.za, self.zb==other.zb])

lines = list(map(lambda x: x.strip(), open('day22.txt').readlines()))
cubes = set()

for j, line in enumerate(lines):
    turn_on = 'on' in line
    l = line.split('=')[1:]
    xa,xb = l[0].split('..')
    ya,yb = l[1].split('..')
    za,zb = l[2].split('..')
    xb = xb[:-2]
    yb = yb[:-2]

    xa,xb,ya,yb,za,zb = int(xa),int(xb),int(ya),int(yb),int(za),int(zb)

    ''' 1 pixel padding '''
    if xa > xb: xa += 1
    else: xb += 1

    if ya > yb: ya += 1
    else: yb += 1

    if za > zb: za += 1
    else: zb += 1
    ''' ''' 

    new_cube = Cube(xa, xb, ya, yb, za, zb)
    new_cubes = set()

    for cube in cubes:
        if not new_cube.intersect(cube): new_cubes.add(cube)
        else:
            xs = sorted([cube.xa, cube.xb, new_cube.xa, new_cube.xb])
            ys = sorted([cube.ya, cube.yb, new_cube.ya, new_cube.yb])
            zs = sorted([cube.za, cube.zb, new_cube.za, new_cube.zb])

            for x1, x2 in zip(xs, xs[1:]):
                for y1, y2 in zip(ys, ys[1:]):
                    for z1, z2 in zip(zs, zs[1:]):
                        cube_slice = Cube(x1, x2, y1, y2, z1, z2)
                        if cube_slice.intersect(cube) and not cube_slice.intersect(new_cube):
                            new_cubes.add(cube_slice)

    if turn_on: new_cubes.add(new_cube)
    cubes = new_cubes

print(sum(c.volume() for c in cubes))





