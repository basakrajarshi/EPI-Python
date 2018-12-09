# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 01:44:31 2018

@author: rajar
"""

# Reverse a single sublist

def reverse_sublist(L, start, finish):
    dummy_head = sublist_head = ListNode(0, L)
    
    for _ in range(1, start):
        sublist_head = sublist_head.next
        
    # Reverses sublist
    sublist_iter = sublist_head.next
    
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (temp.next, 
                                                           sublist_head.next,
                                                           temp)
    
    return dummy_head.next
