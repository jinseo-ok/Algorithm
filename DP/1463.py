# -*- coding: utf-8 -*-
# 1463_1로 만들기
import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
memo = []
n = 0

def fibo(x, n):
    n += 1
    if x == 1: return n
    elif x == 2: return 1

    if x % 3 == 0:
        return fibo(x%3, n)
    elif x % 2 == 0:
        return fibo(x%2, n)
    else:
        return fibo(x-1, n)
n = fibo(N, n)
print(n)