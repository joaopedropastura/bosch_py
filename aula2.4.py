# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 10:53:14 2022

@author: disrct
"""

import pandas as pd 

titanic = pd.read_csv("titanic.csv")
tam = titanic.Age.count()
soma = titanic.Age.sum()
titanic = titanic.fillna(round(soma/tam, 2))