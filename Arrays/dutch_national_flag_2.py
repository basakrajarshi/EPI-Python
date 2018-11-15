# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:19:10 2018

@author: rajar
"""

def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    # First pass, group elements smaller than pivot
    smaller = 0
    for i in range(len(A)):
        # Look for a smaller element.
        #print ("Reached here - 1")
        if (A[i] < pivot):
            A[i], A[smaller] = A[smaller], A[i]
            #print ("Reached Here - 2")
            smaller += 1
        
            
    # Second pass, group elements larger than pivot
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        # Look for a larger element, Stop when we reach an element less 
        # than pivot, since firet pass has moved them to the start of A.
        #print ("Reached here - 3")
        if (A[i] > pivot):
            A[i], A[larger] = A[larger], A[i]
            #print ("Reached Here - 4")
            larger -= 1
    return A

B = [2,1,4,3,6,5,8,7,9]
print (dutch_flag_partition(4,B))