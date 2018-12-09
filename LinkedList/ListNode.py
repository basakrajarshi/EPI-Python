# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 13:54:48 2018

@author: rajar
"""

class ListNode:
    def __init__(self, data = 0, next_node = None):
        self.data = data
        self.next_node = next_node
        
    # Search for a key
    def search_list(L, key):
        while L and L.data != key:
            L = L.next
        # If key was not present in the list, L will have become null
        return L
    
    # Insert a new node after a spsecified node
    def insert_after(node, new_node):
        new_node.next = node.next
        node.next = new_node
    
    # Delete a node
    def delete_after(node):
        node.next = node.next.next
    
    