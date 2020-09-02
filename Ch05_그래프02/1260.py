# -*- coding: utf-8 -*-
# 1260_DFS와 BFS

import sys
from collections import deque
sys.setrecursionlimit(10**6)

def dfs(current):
    visited[current] = True
    dfs_list.append(current)
    for node in adj[current]:
        if not visited[node]:
            dfs(node)
        
def bfs(root):
    visited[root] = True
    que = deque([root]) # deque가 list보다 시간복잡도가 굉장히 빠름
    # que.append(root)
    while que:
        current = que.popleft()
        bfs_list.append(current)
        for node in adj[current]:
            if not visited[node]:
                que.append(node)
                visited[node] = True

N, M, V = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)
[node.sort() for node in adj]
    
dfs_list = []
bfs_list = []
                
visited = [False] * (N + 1)                
dfs(V)
print(dfs_list)
visited = [False] * (N + 1)
bfs(V)
print(bfs_list)
        