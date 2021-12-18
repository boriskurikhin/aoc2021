#!/usr/bin/env Python3
from copy import deepcopy
from heapq import heappush, heappop
from collections import Counter, defaultdict, deque
from functools import reduce
from math import ceil
''' end of imports '''

class Node:
    def __init__(self, parent, val=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
    def __repr__(self):
        if isinstance(self.val, int): return str(self.val)
        else: return f'[{self.left},{self.right}]'

def build_tree(segment, parent: Node) -> Node:
    if isinstance(segment, int):
        return Node(parent, segment)
    new_node = Node(parent)
    new_node.left = build_tree(segment[0], new_node)
    new_node.right = build_tree(segment[1], new_node)
    return new_node

def increase_left(node: Node, to_add: int):
    if not node.parent: return
    if node.parent.left is node:
        increase_left(node.parent, to_add)
        return
    outer = node.parent.left
    while outer and outer.val is None:
        outer = outer.right
    assert outer and outer.val is not None, 'Found a weird leaf'
    outer.val += to_add

def increase_right(node: Node, to_add: int):
    if not node.parent: return
    if node.parent.right is node:
        increase_right(node.parent, to_add)
        return
    outer = node.parent.right
    while outer and outer.val is None:
        outer = outer.left
    assert outer and outer.val is not None, 'Found a weird leaf'
    outer.val += to_add

def split(node: Node):
    if node.val is not None and node.val >= 10:
        l = node.val // 2
        r = node.val - l
        node.val = None
        new_left = Node(node, l)
        new_right = Node(node, r)
        node.left = new_left
        node.right = new_right
        return True
    if node.left and split(node.left): return True
    if node.right and split(node.right): return True

def magnitude(node: Node):
    if node.val is not None:
        return node.val
    return 3 * magnitude(node.left) + 2 * magnitude(node.right)

def explode(node: Node, depth: int):
    if node.val is None and node.left.val is not None and node.right.val is not None and depth >= 4:
        increase_left(node, node.left.val)
        increase_right(node, node.right.val)

        node.left = None
        node.right = None
        node.val = 0
        return True
    if node.left and explode(node.left, depth + 1): return True
    if node.right and explode(node.right, depth + 1): return True
    return False


''' start of program'''
lines = list(map(lambda x: eval(x.strip()), open('day18.txt').readlines()))
best = 0

def _reduce(left_segment: list, right_segment: list):
    left = build_tree(left_segment, None)
    right = build_tree(right_segment, None)
    root = Node(None, None, left, right)
    left.parent = root
    right.parent = root
    while True:
        if explode(root, 0): continue
        if not split(root): break
    return magnitude(root)

best = 0
for i, first in enumerate(lines):
    for second in lines[i + 1:]:
        best = max(best, _reduce(first, second), _reduce(second, first))
print(best)
