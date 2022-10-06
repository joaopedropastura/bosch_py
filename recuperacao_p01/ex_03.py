# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 09:24:31 2022

@author: DISRCT
"""
frases = []
palindromo = []
qt_frases = int(input("Quantas frases deseja verificar? "))
for i in range(qt_frases):
   aux = input(f"insira a {i+1} frase\n").lower()
   frases.append(aux)


def check_palindromo():
    for i in frases:
        temp = list(i.replace(" ",""))
        reverso = temp[::-1]
        if temp == reverso:
            palindromo.append(i)
check_palindromo()
print("São palindromos: \n")
for j in palindromo:    
    print(j)