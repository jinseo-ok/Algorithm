# -*- coding: utf-8 -*-
# 11066_파일 합치기
import sys
T = int(sys.stdin.readline())

for _ in range(T):
    K = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))
    
    print(files)