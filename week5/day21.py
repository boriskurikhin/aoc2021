#!/usr/bin/env Python3
from copy import deepcopy
from heapq import heappush, heappop
from collections import Counter, defaultdict, deque
from functools import reduce, lru_cache
import math
''' end of imports '''

WAYS = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

@lru_cache(None)
def play1(score_a, score_b, pos, other_pos, a_turn = True):
    if score_a >= 21: return [1, 0]
    if score_b >= 21: return [0, 1]
    out = [0, 0]
    for roll, times in WAYS.items():
        if a_turn:
            p = pos + roll if pos + roll <= 10 else pos + roll - 10
            x, y = play1(score_a + p, score_b, p, other_pos, False)
            out[0] += x * times
            out[1] += y * times
        else:
            p = other_pos + roll if other_pos + roll <= 10 else other_pos + roll - 10
            x, y = play1(score_a, score_b + p, pos, p, True)
            out[0] += x * times
            out[1] += y * times
    return out
            
print(max(play1(0, 0, 4, 9, True)))