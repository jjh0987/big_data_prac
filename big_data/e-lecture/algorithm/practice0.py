from collections import deque

queue = deque()
queue.append(1)
queue.popleft()
# ---------------------------------------------------------

import sys
import heapq
# nlogn sort method
input = sys.stdin.readline

def heapsort(iter):
    h = []
    result = []

    for value in iter:
        heapq.heappush(h,value) # min heap 자료구조 생성
    for i in range(len(h)):
        result.append(heapq.heappop(h)) # heap 에서 최상위 노드 반환 min heap 구조이므로 가장 작은값부터 출력
    return result

n = int(input()) # 자료길이
arr = [] # raw data
for i in range(n):
    arr.append(int(input()))
res = heapsort(arr)

for i in range(n):
    print(res[i])

# ---------------------------------------------------------

input = sys.stdin.readline
def heapsort(iter):
    h = []
    result = []

    for value in iter:
        heapq.heappush(h,-value) # max heap 자료구조 생성 # 후처리 - 해주어야 한다.
    for i in range(len(h)):
        result.append(heapq.heappop(h)) # heap 에서 최상위 노드 반환 min heap 구조이므로 가장 작은값부터 출력
    return result

n = int(input()) # 자료길이
arr = [] # raw data
for i in range(n):
    arr.append(int(input()))
res = heapsort(arr)

for i in range(n):
    print(-res[i])

h = []
result = []
heapq.heappush(h, 5)  # min heap 자료구조 생성
result.append(heapq.heappop(h))
h
result

# ---------------------------------------------------------
class Node:
    def __init__(self,data,left,right):
        self.data = data
        self.left_node = left
        self.right_node = right

def pre_order(node):
    print(node.data, end=' ')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])

def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end=' ')
    if node.right_node != None:
        in_order(tree[node.right_node])

def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end=' ')

n = int(input())
tree = {}
for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == 'None':
        left_node = None
    if right_node == 'None':
        right_node = None
    tree[data] = Node(data,left_node,right_node)

# test set
# 7
# A B C
# B D E
# C F G
# D Npne None
# E Npne None
# F Npne None
# G Npne None
pre_order(tree['A'])
in_order(tree['A'])
post_order(tree['A'])