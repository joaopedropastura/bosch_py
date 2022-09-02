# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:15:20 2022

@author: disrct
"""

import pandas as pd 

titanic = pd.read_csv("titanic.csv")

p_cabin = titanic.groupby("Sex")["Age"].mean()
print(p_cabin.male)
def preenche_idade(linha):
    
    if linha["Age"].isnull():
        if linha["Sex"] == "male":
            linha["Age"] = p_cabin.male
        else:
            linha["Age"] = p_cabin.female

titanic["lala"] = titanic.apply(preenche_idade, axis = 1)