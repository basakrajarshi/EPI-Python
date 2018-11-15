# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 14:34:45 2018

@author: rajar
"""

def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    # First pass, group elements smaller than pivot
    for i in range(len(A)):
        # Look for a smaller element.
        print ("Reached here - 1")
        for j in range(i + 1, len(A)):
            if (A[j] < pivot):
                A[i], A[j] = A[j], A[i]
                print ("Reached Here - 2")
                break
            
    # Second pass, group elements larger than pivot
    for i in reversed(range(len(A))):
        # Look for a larger element, Stop when we reach an element less 
        # than pivot, since firet pass has moved them to the start of A.
        print ("Reached here - 3")
        for j in reversed(range(i)):
            if (A[j] > pivot):
                A[i], A[j] = A[j], A[i]
                print ("Reached Here - 4")
                break
    return A
            
B = [1,2,3,4,5,6,7,8,9]
print (dutch_flag_partition(4,B))