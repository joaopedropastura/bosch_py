# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 10:49:20 2022

@author: DISRCT
"""

import pandas as pd

titanic = pd.read_csv("titanic.csv")
titanic["Cabin"]=titanic["Cabin"].fillna("Desconhecido")
southampton = titanic[titanic["Embarked"] == "S"]
sex = southampton[southampton["Sex"] == "female"]
age = sex[sex["Age"] == 29]
name = age["Name"].str.find("Anne")
result = pd.concat([age["Name"], name.rename('dex')], axis=1)
result1 = result[result["dex"] > 0]
print(result1["Name"])
#print(result)
#titanic = titanic.fillna()