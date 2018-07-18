#!/bin/python3

import sys

l=[]
N = int(input().strip())
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    try:
        s=emailID.split('@gmail.com')
        if(len(s)==2):
            l.append(firstName)
    except:
        pass
l.sort()
for i in l:
    print(i)
