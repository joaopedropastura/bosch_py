# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 09:02:21 2022

@author: disrct
"""

import math

def calculadora(num):
    sqrt =      math.sqrt(num)
    quadrado =  math.pow(num,2) 
    inverso =   1/num
    factorial = math.factorial(num)
    print("Raiz quadrada: ", sqrt)
    print("Quadrado: ", quadrado)
    print("Inverso: ", inverso)
    print("Fatorial: ", factorial)


while(1):
    num = float(input("Digite um valor ou zero para sair: "))
    if num == 0:
        break
    calculadora(num)    