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