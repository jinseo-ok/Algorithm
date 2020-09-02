# -*- coding: utf-8 -*-
# 2179_미로 탐색

import sys
N, M = map(int, sys.stdin.readline().split())
mat =[]
for _ in range(N):
    v = list(map(int, sys.stdin.readline().strip()))
    mat.append(v)

que = []
dic = {}
visited = [[False] * M for _ in range(N)]
que.append([0, 0])
i = 0
j = 0
dic[str(i) + str(j)] = 0
dx = [-1,0,1,0]
dy = [0,-1,0,1]
while que:
    x, y = que.pop(0)
    if [x, y] == [N-1, M-1]:
        answer = dic[str(x) + str(y)]
        break
    for a,b in zip(dx, dy):
        nx = x + a
        ny = y + b
        if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]):
            if not visited[nx][ny]:
                if mat[nx][ny] == 1:
                    visited[nx][ny] = True
                    dic[str(nx) + str(ny)] = dic[str(x) + str(y)] + 1
                    que.append([nx,ny])
print(answer + 1)