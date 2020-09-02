# -*- coding: utf-8 -*-
# 2667_단지번호붙이기
import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().strip())))

total = []

visited = [[False] * len(board[0]) for _ in board]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
ans = 0
def bfs(i, j, land):
    q = []
    q.append([i,j])
    while q:
        x, y = q.pop(0)
        for a,b in zip(dx, dy):
            nx = x + a
            ny = y + b
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                if not visited[nx][ny]:
                    if board[nx][ny] == 1:
                        land += 1
                        visited[nx][ny] = True
                        q.append([nx,ny])
    return land

for i, _ in enumerate(board):
    for j, _ in enumerate(board[0]):
        land = 0
        if board[i][j] == 1:
            if not visited[i][j]:
                land = bfs(i, j, land)
                ans += 1
                total.append(land)

print(ans)
total.sort()
[print(t+1) if t == 0 else print(t) for t in total]