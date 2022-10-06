# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 08:57:05 2022

@author: DISRCT
"""

import numpy as np


txt = open("registros.txt", 'a')

matriz = np.random.randint(10, size=(25))
count = 0
for i in matriz:
    if i %2 == 0:
        count +=1
        
check = (matriz%2 == 0)
matriz[check] = matriz[check]**2
txt.write(str(count) + "\n")
txt.close


txt = open("registros.txt", 'r')
result = 0
for x in txt:
    result += int(x)

print(f"A array orignal:\n{matriz.reshape(5,5)}\n")
print(f"A array substituindo os números ímpares:\n{matriz.reshape(5,5)}\n")
print(f"Existem {result} registros.")
