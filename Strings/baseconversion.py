# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 00:06:48 2018

@author: rajar
"""
def baseconverter(number, oldbase, newbase):
    n1 = number
    b1 = oldbase
    
    # Store all the digits in an array
    array_of_digits = []
    while True:
        a = n1 % 10
        array_of_digits.append(a)
        n1 //= 10
        if (n1 == 0):
            break
    #array_of_digits = list(reversed(array_of_digits))    
    #print(array_of_digits)
    
    # Converting into base 10
    num_b_10 = 0
    
    for i in range(0,len(array_of_digits)):
        #print(i)
        num_b_10 += array_of_digits[i] * (b1 ** i)
        
    #print (num_b_10)
    
    # Converting into base 3
    new_base = newbase
    array_new_base = []
    num_b_new = 0
    while True:
        b = num_b_10 % new_base
        array_new_base.append(b)
        num_b_10 //=3
        if (num_b_10 == 0):
            break
        
    #print(array_new_base)
    
    # Convert array to number
    for j in range(0,len(array_new_base)):
        #print(array_new_base[j])
        num_b_new += array_new_base[j] * (10 ** j)
    
    #print (num_b_new)
    return num_b_new

n = 615
ob = 7
nb = 3
print(baseconverter(n,ob,nb))