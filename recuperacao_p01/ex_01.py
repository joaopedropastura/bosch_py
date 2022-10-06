# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 08:13:49 2022

@author: DISRCT
"""

times = ["1_palmeiras", "2_coritiba", "1_corinthians", "3_juventude", "2_fluminense", "3_bahia", "1_cuiaba", "2_cascavel", "3_ponte preta", "2_parana clube", "3_voltaredonda"]
times = [x.split("_") for x in times]

primeira_divisao = [z for z in times if z[0] == '1']
segunda_divisao = [y for y in times if y[0] == '2']
terceira_divisao = [w for w in times if w[0] == '3']
# pd = primiera_divisao.remove("1")
primeira_divisao = [primeira_divisao[i][1:] for i in range(len(primeira_divisao))]
segunda_divisao = [segunda_divisao[j][1:] for j in range(len(segunda_divisao))]
terceira_divisao = [terceira_divisao[k][1:] for k in range(len(terceira_divisao))]
aux = []
for m in primeira_divisao:
    aux.append(m)

print(f"Primeira divisão: {primeira_divisao}")
print(f"Segunda divisão: {segunda_divisao}")
print(f"Terceira divisão: {terceira_divisao}")