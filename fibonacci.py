# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 09:05:42 2022

@author: disrct
"""

tam = int(input("Digite o numero de fatores: "))
anterior = 1
atual = 1
result = 0
print("0\n1\n1")
for i in range(tam - 3):
    result = anterior + atual
    print(result)
    anterior = atual
    atual = result

# fibonacci = [0,1]
# for i in range(tam - 2):
#     fibonacci.append(fibonacci[len(fibonacci) - 1] + fibonacci[len(fibonacci) - 2])
# print(fibonacci)