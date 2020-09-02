# -*- coding: utf-8 -*-
# 9465_스티커
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())

    board = []
    for _ in range(2):
        board.append(list(map(int, sys.stdin.readline().split())))
    
    board[0][1] += board[1][0]
    board[1][1] += board[0][0]

    for i in range(2, n):
        board[0][i] += max(board[1][i-1], board[1][i-2])
        board[1][i] += max(board[0][i-1], board[0][i-2])

    print(max(board[0][-1], board[1][-1]))
