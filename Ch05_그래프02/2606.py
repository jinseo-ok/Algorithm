# -*- coding: utf-8 -*-
# 2606_바이러스

import sys
sys.setrecursionlimit(10**6)

N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v) 
    adj[v].append(u) 
    
dfs_list = []
def dfs(current):
    visited[current] = 1
    dfs_list.append(current)
    for node in adj[current]:
        if visited[node] == 0:
            dfs(node)

visited = [0] * (N + 1)                
dfs(1)
print(sum(visited) - 1)