#!/bin/python

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    n1,n2,c=len(a),len(b),0
    a,b=list(a),list(b)
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j] and a[i]!='-':
                c+=1
                a[i]=b[j]='-'
    return ((n1-c)+(n2-c))
                
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = raw_input()

    b = raw_input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
