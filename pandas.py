# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 10:48:24 2022

@author: disrct
"""

import pandas as pd

titanic = pd.read_csv("titanic.csv")
titanic.head()

#seprando o data frame de acordo com as colunas.
lista_nova = titanic.columns[:-1]
nome = titanic[lista_nova]
print(lista_nova)
print(nome)

lista_nova_01 = titanic.iloc[:, :-1]
print(lista_nova_01)
lista_nova_02 = titanic.loc[:,["Pclass","Age"]]
print(lista_nova_02)
#informando ao meu data frame que quero usar uma columna como o index
test = lista_nova_02.describe()
print("")
test2 = titanic[["Pclass", "Age"]].describe()
print("")
print(test2)
print("lalalal")
print(test)