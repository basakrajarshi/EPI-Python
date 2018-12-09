# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 19:00:40 2018

@author: rajar
"""

def merge_two_sorted_lists(L1, L2):
    # Creates a placeholder for the result.
    dummy_head = tail = ListNode()
    
    while L1 and L2:
        if (L1.data < L2.data):
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
        
    # Appends the remaining nodes of L1 and L2
    tail.next = L1 or L2
    return dummy_head.next

