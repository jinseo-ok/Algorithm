# -*- coding: utf-8 -*-
# 11724_연결 요소의 개수

import sys
sys.setrecursionlimit(10**7)

N, M = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)
    
def dfs(src):
    visited[src] = 1
    for node in adj[src]:
        if visited[node] == 0:
            dfs(node)
        
ans = 0
visited = [0] * (N + 1)
for i in range(1, N + 1):
    if visited[i] == 0:
        dfs(i)
        ans += 1
        
print(ans)