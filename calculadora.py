# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 08:08:13 2022

@author: disrct
"""

menu = ["Soma", "Multiplicação", "Subtração", "Divisão", "Sair"]
result = 0

while (1):
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    for i in menu:
        print(menu.index(i) + 1, "-", i)
    op = int(input("Digite a operação desejada: "))
    if op == 1:
        result = num1+num2
    elif op == 2:
        result = num1*num2
    elif op == 3:
        result = num1-num2
    elif op == 4:
        result = num1/num2
    else:
        break
    print("O resultado da operação é: ", result)

    