# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:30:28 2018

@author: rajar
"""

def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    # Keep the follwing invariants during partitioning
    # bottom group: A[:smaller]
    # middle group: A[smaller:equal]
    # unclassified group: A[equal:larger]
    # top group: A[larger:]
    
    smaller, equal, larger = 0,0, len(A)
    
    while (equal < larger):
        if (A[equal] < pivot):
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif (A[equal] == pivot):
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
    return A

B = [2,1,4,3,6,5,8,7,9]
print(dutch_flag_partition(4,B))