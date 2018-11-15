# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 21:44:09 2018

@author: rajar
"""

cit = input("Enter the citations of the researcher.")
cita = cit.split(',')
num = len(cita)
h = 0
hlist = []
entries = 1
count = 0
i = 0
n = 0
while(i < num):
    for j in range(i+1, num):
        if (cita[j] >= cita[i]):
            entries += 1
    if (n != cita[i]):
        print (entries, cita[i])
        if (entries == int(cita[i])):
            h = entries
            hlist.append(h)
        if (entries < h):
            break
    n = cita[i]
    entries = 1
    i = i + 1
            
print (hlist)
