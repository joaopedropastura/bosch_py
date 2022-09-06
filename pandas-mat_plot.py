# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 10:48:13 2022

@author: DISRCT
"""

import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("titanic.csv")
legend = ["Survived", "Not Survived"]
sobreviventes = titanic.Survived[titanic["Survived"] == 1]
morridos = titanic.Survived[titanic["Survived"] == 0]

plt.bar(legend[0], sobreviventes.count(), edgecolor="black")
plt.bar(legend[1], morridos.count(), edgecolor="black")
plt.title("Quantidade de pessoas que sobreviveream ou não")
plt.xticks(rotation="90")

