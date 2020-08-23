# -*- coding: utf-8 -*-

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

adj = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[b].append(a)
    adj[a].append(b)
    
total = []
for idx in adj[1]:
    total.append(idx)
    for t in adj[idx]:
        total.append(t)

print(len(set(total)) - 1)
    

