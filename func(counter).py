# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 08:05:06 2022

@author: disrct
"""

def counter(init, end, step):
    print("CONTADOR DE PASSOS: ", step, "INICIO: ", init, "FIM: ", end)
    if end < init:
        step = step*-1
        while init >= end:
            print(init)
            init += step
    else:
        while init <= end:
            print(init)
            init += step

user_init = int(input("Digite o incio do contador: "))
user_end = int(input("Digite o final do contador: "))
user_step = int(input("Digite o passo do contador: "))
counter(user_init, user_end, user_step)

