# -*- coding: utf-8 -*-]
# 1890_점프
import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

board = []
for _ in range(N):
    v = list(map(int, sys.stdin.readline().split().strip()))
    board.append(v)

def fibo(locs):
    candidates = []
    for loc in locs:
        i = loc[0]; j = loc[1]
        x = board[i][j]
        if x == 0:
            break
        if i + x <= len(board):
            candidates.append([i+x, j])
        if j + x <= len(board[0]):
            candidates.append([i, j + x])
        fibo(candidates)


    candidates = []
    for v in x:
        if i + x <= len(board):
            candidates.append(board[i+x][j])
        if j + x <= len(board[0]):
            candidates.append(board[i][j + x])
    return candidates

for i in range(len(board)):
    for j in range(len(board[0])):
        fibo([[i,j]])
    

