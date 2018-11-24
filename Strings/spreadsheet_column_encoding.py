# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 14:27:36 2018

@author: rajar
"""

st = "AA"
charac = list(st)
num = 0

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11,12,13,14,15,16,17,18,19,20,
           21,22,23,24,25,26]

"""for i in range(len(numbers)):
    print (numbers[i], type(numbers[i]))"""
    
#print(charac)

for i in charac:
    num += numbers[letters.index(i)]
    

