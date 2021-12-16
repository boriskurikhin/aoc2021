#!/usr/bin/env Python3
from copy import deepcopy
from heapq import heappush, heappop
from collections import Counter, defaultdict, deque
from functools import reduce
import operator
''' end of imports '''

file = open('day16.txt')

line = file.read().strip()
binary = ''.join(bin(int(hx, 16))[2:].zfill(4) for hx in line)

crunch = {
    0: sum,
    1: lambda lst: reduce(operator.mul, lst, 1),
    2: min,
    3: max,
    5: lambda x: 1 if x[0] > x[1] else 0,
    6: lambda x: 1 if x[0] < x[1] else 0,
    7: lambda x: 1 if x[0] == x[1] else 0 }

def calculate(i):
    if i >= len(binary):
        return len(binary), []

    version = int(binary[i:i+3], 2)
    id = int(binary[i+3:i+3+3], 2)
    i += 6
    
    og_id = id

    if id == 4:
        number = ''
        while i < len(binary) and binary[i] == '1':
            number += binary[i+1:i+5]
            i += 5
        number += binary[i+1:i+5]
        i += 5
        padding = 0
        while i < len(binary):
            if (len(number) + padding) % 4 == 0:
                break
            padding += 1
            i += 1
        return i, [int(number, 2)]
    else:
        id = int(binary[i], 2)
        i += 1
        if id == 0:
            packet_size = int(binary[i:i+15], 2); i += 15
            end_index = i + packet_size
            operands = []
            while i < end_index:
                i, op = calculate(i)
                operands += op
            return end_index, [crunch[og_id] (operands)]
        elif id == 1:
            num_packet = int(binary[i:i+11], 2); i += 11
            operands = []
            for j in range(num_packet):
                i, op = calculate(i)
                operands += op
            return i, [crunch[og_id] (operands)]
        else:
            raise Exception('dank!')

print(calculate(0)[1].pop())