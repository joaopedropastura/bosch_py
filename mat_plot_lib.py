# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 08:44:25 2022

@author: DISRCT
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("respiradores.csv")
df = df.drop(["LIBANO", "PERU", "HAITI"], axis=1)
df["NORTE"] = df[["ACRE", "AMAZONAS", "AMAPA","PARA", "RONDONIA", "RORAIMA", "TOCANTINS"]].sum(axis=1)
df["SUL"] = df[["RIO GRANDE DO SUL", "PARANA", "SANTA CATARINA"]].sum(axis=1)
df["SUDESTE"] =df[["RIO DE JANEIRO", "ESPIRITO SANTO", "MINAS GERAIS", "SÃO PAULO"]].sum(axis=1)
df["CENTRO-OESTE"] = df[["GOIAS","MATO GROSSO", "MATO GROSSO DO SUL", "DISTRITO FEDERAL"]].sum(axis=1)
df["NORDESTE"] = df[["MARANHÃO", "PIAUI", "RIO GRANDE DO NORTE", "CEARA", "PARAIBA", "BAHIA", "PERNAMBUCO", "ALAGOAS", "SERGIPE"]].sum(axis=1)



fig, eixo = plt.subplots(nrows=1, ncols=2, figsize=(30,10))
eixo[0].plot(df.MES, df.SUL, marker='o', label = "Sul")
eixo[0].plot(df.MES, df.NORTE, marker='o', label = "Norte")
eixo[0].plot(df.MES, df.SUDESTE, marker='o', label = "Sudeste")
eixo[0].plot(df.MES, df["CENTRO-OESTE"], marker='o', label = "Centro-Oeste")
eixo[0].plot(df.MES, df.NORDESTE, marker='o', label = "Nordeste")
eixo[0].grid(linestyle=':')
eixo[0].legend(fontsize=18)
eixo[0].tick_params(axis='x', labelrotation=45)


eixo[1].bar([a for a in range(df.NORDESTE.shape[0])], df.NORDESTE, width=0.1, label = "Nordeste")
eixo[1].bar([a-0.125 for a in range(df.NORTE.shape[0])], df.NORTE, width=0.1, label = "Norte")
eixo[1].bar([a+0.125 for a in range(df.SUDESTE.shape[0])], df.SUDESTE, width=0.1, label = "Sudeste")
eixo[1].bar([a-0.25 for a in range(df.SUL.shape[0])], df.SUL, width=0.1, label = "Sul")
eixo[1].bar([a+0.25 for a in range(df["CENTRO-OESTE"].shape[0])], df["CENTRO-OESTE"], width=0.1, label = "Centro-Oeste")
eixo[1].legend(fontsize=18)
plt.xticks(np.arange(11), df.MES, rotation=45)

lalalal