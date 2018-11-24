# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 12:10:01 2018

@author: rajar
"""

def is_palindrome(s):
    return all(s[i] == s[~i] for i in range(len(s) // 2))

s = "malayalami"
print(is_palindrome(s))