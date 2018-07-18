import math
n=int(input())
for i in range(n):
    a=int(input())
    f=0
    if a<=1:
        f=1
    for j in range(2,int(math.sqrt(a))+1):
        if a%j==0:
            f=1
            break
    if f==1:
        print('Not prime')
    else :
        print('Prime')
