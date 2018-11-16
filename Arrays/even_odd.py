# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 11:41:40 2018

@author: rajar
"""
# Given a string of even or odd integers, arrange all the entries
# such that all the even entries appear first in the string, 
# without using additional storage

def evenodd(A):
    #A = [1,2,3,4,5,6,7,8,9]
    n_even = 0
    n_odd = len(A) - 1
    while (n_even < n_odd):
        if (A[n_even] % 2 != 0):
            n_even += 1
        else:
            A[n_even], A[n_odd] = A[n_odd], A[n_even]
            n_odd -= 1
    return A

B = [1,2,3,4,5,6,7,8,9]
print (evenodd(B))
