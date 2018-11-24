# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 15:11:37 2018

@author: rajar
"""
import functools
def ss_decode_col_id(col):
    return functools.reduce(
            lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)

print(ord(''))