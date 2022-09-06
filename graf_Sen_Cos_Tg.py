# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 08:17:49 2022

@author: DISRCT
"""

import numpy as np
import matplotlib.pyplot as plt
import math
scale = np.linspace(-3,3,100)
sinValue = []
cosValue = []
tanValue = []

for i in range(len(scale)):
    sen = math.sin(scale[i])
    cos = math.cos(scale[i])
    tan = math.tan(scale[i])
    tanValue.append(tan)
    sinValue.append(sen)
    cosValue.append(cos)
print(cos)

plt.plot(scale, tanValue, label = "Tangente")
plt.legend()
fig, eixo = plt.subplots(nrows=1, ncols=2, figsize=(30,12))

eixo[0].plot(scale, sinValue, label = "Seno")
eixo[1].plot(scale, cosValue, label = "Cosseno")

eixo[0].legend(fontsize=18)
eixo[1].legend(fontsize=18)
