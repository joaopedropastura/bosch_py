# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 10:57:28 2022

@author: DISRCT
"""

import pandas as pd 

titanic = pd.read_csv("titanic.csv")
titanic["Cabin"]=titanic["Cabin"].fillna("Desconhecido")
classe = titanic[(titanic["Pclass"] == 3) | (titanic["Pclass"] == 1)]
survivedp1 = classe[((classe["Pclass"] == 3) & (classe["Survived"] == 0)) | ((classe["Pclass"] == 1) & (classe["Survived"] == 1))]