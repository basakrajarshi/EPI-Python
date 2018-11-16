# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 23:06:55 2018

@author: rajar
"""

def plusone(A):
    A[-1] += 1
    for i in reversed(range(1,len(A))):
        print (i)
        if (A[i] != 10):
            break
        A[i] = 0
        A[i - 1] += 1
    
    if (A[0] == 10):
        A[0] = 1
        A.append(0)
    
    return A

B = [9,9,9]
print (plusone(B))