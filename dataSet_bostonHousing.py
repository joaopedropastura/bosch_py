# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 08:48:38 2022

@author: DISRCT
"""

import pandas as pd

boston = pd.read_csv("BostonHousing.csv")
boston.head()


lista = boston[["crim", "medv"]]

print(lista.head(14))

lista2 = boston.loc[:13,["crim", "medv"]]
print("")
print(lista2)
print("")
lista3 = boston["age"].unique
print(lista3)
print("")
lista4 = boston["age"]
# func para excluir inteiramente todas as linhas que possuem um indice com o valor: "nan" .dropna() 
# sobrescrevendo a propria variavel que esta armazenando o DataFrame
#  func para trocar os valores "nan" .fillna(valor que deseja substituir)
#https://medium.com/data-hackers/uma-introdu%C3%A7%C3%A3o-simples-ao-pandas-1e15eea37fa1