# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 09:55:17 2022

@author: DISRCT
"""
cliente = int(input("Insira qual valor deseja sacar: (minímo R$10,00) \n"))
while cliente <= 10:
    print("Valor não correspondente")
    cliente = int(input("Insira qual valor deseja sacar: (minímo R$10,00) \n"))
n100 = 0
n50 = 0 
n10 = 0
n5 = 0
n1 = 0
while(cliente != 0):
    if cliente >= 100:
        cliente -= 100
        n100 += 1
    elif cliente >= 50:
        cliente -= 50
        n50 += 1
    elif cliente >= 10:
        cliente -= 10
        n10 += 1
    elif cliente >= 5:
        cliente -= 5
        n5 += 1
    else:
        cliente -=1
        n1 +=1

print("Notas para saque:")
print(f"{n100} notas de R$100,00")
print(f"{n50} notas de R$50,00")
print(f"{n10} notas de R$10,00")
print(f"{n5} notas de R$5,00")
print(f"{n1} notas de R$1,00")