# -*- coding: utf-8 -*-
# 1697_숨박꼭질
import sys
N, K = map(int, sys.stdin.readline().split())

que = []
que.append(N)
dic = {}
dic[N] = 0
while que:
    cur = que.pop(0)
    if cur == K:
        res = dic[cur]
        break
    for x in (cur+1, cur-1, 2*cur):
        if x < 100001 and x not in dic.keys():
            dic[x] = dic[cur] + 1
            que.append(x)

print(res)