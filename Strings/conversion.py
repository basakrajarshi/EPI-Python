# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 12:54:52 2018

@author: rajar
"""

import functools
import string

def integertostring(x):
    is_neg = False
    
    if (x < 0):
        x = -x
        is_neg = True
        
    s = []
    
    while True:
        s.append(chr(ord('0') + x % 10))
        x = x // 10
        if (x == 0):
            break
    
    return ('-' if is_neg else '') + ''.join(reversed(s))

def stringtointeger(s):
    return functools.reduce(
            lambda running_sum, c: running_sum * 10 + string.digits.index(c),
            s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)
    
    
x = 123
s = "123"
print(type(stringtointeger(s)))
