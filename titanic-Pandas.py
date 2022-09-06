# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 11:29:49 2022

@author: DISRCT
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic = pd.read_csv("titanic.csv")
quantParentes = np.zeros(10)

titanic["Parentes"] = titanic["SibSp"] + titanic["Parch"]
maxParentes = titanic.Parentes.max()
maxPessoas = len(titanic.PassengerId)

for i in range(len(titanic.PassengerId)):
    
    

# plt.plot(maxParentes, maxPessoas)