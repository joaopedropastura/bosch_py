# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 09:13:59 2022

@author: DISRCT
"""

import numpy as np 
import matplotlib.pyplot as plt
import math

cidades = ["Araucária", "Campo Largo", "Colombo", "Fazenda Rio Grande", "Pinhais", "São José dos Pinhais"]
pop = [141410, 130091, 240840, 98368, 130789, 317476]
p, tx, autotexts = plt.pie(pop, labels=cidades, autopct="", shadow=True, startangle=45, radius=2)
for i, a in enumerate(autotexts):
    a.set_text("{} hab.".format(pop[i]))