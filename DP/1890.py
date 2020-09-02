# -*- coding: utf-8 -*-]
# 1890_점프
import sys
n = int(sys.stdin.readline())

board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            break
        nx = j + board[i][j]
        ny = i + board[i][j]
        if 0 <= nx < n:
            dp[i][nx] += dp[i][j]
        if 0 <= ny < n:
            dp[ny][j] += dp[i][j]


print(dp[-1][-1])
    

