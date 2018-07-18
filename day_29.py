#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    max=-1
    for i in range(1,n):
        for j in range(i+1,n+1):
            v=i&j
            if max<v and v<k:
                max=v
            if v==i:
                break
    print(max)
        
