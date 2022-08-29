# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 09:28:33 2022

@author: DISRCT
"""

class casa():
    def __init__(self, area:float, rua:str, cor:str, nome = 'joao'):
        self.area = area
        self.rua = rua
        self.cor = cor 
        self.nome = nome
    
    def mostrar_dados(self):
        print(f'''
              Area: {self.area}
              Rua: {self.rua}
              Cor da casa: {self.cor}
              Proprietario: {self.nome}
              ''')

        

area = float(input("Dgiite a area da casa: "))
rua = input("Dgiite a rua da casa: ")
cor = input("Dgiite a cor da casa: ")
nome = input("Dgiite o nome do proprietario casa: ")

casa_user = casa(area, rua, cor, nome)

casa_user.mostrar_dados()                  