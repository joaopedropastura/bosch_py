# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 10:53:29 2022

@author: DISRCT
"""

matriz =  [['', '', '', '', '', '', ''], 
           ['', '', '', '', '', '', ''], 
           ['', '', '', '', '', '', ''], 
           ['', '', '', '', '', '', ''],
           ['', '', '', '', '', '', ''],
           ['', '', '', '', '', '', '']]


print("        bem vindo ao LIG-4")
print("----------------------------------")

def print_matriz(matriz):
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                print(" |   ", end = '')
            print("")


# def play_game()

print_matriz(matriz)
    