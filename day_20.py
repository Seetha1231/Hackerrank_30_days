#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
nswap=0
for i in range(n):
    for j in range(n-1):
        if (a[j] > a[j+1]):
            nswap+=1
            a[j],a[j+1]=a[j+1],a[j]
print('Array is sorted in '+str(nswap)+' swaps.')
print('First Element: '+str(a[0]))
print('Last Element: '+str(a[n-1]))


