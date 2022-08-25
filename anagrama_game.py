# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 08:11:19 2022

@author: DISRCT
"""
from random import sample
import random

# user decide a qunat de pontos
# init com 100 pontos
# icluir dificuldade (tam da palavra)
# output caso user erre/acerte

file = open("poema.txt", "r", encoding=("utf8"))

facil = []
normal = []
dificil = []

for i in file:
    line = i.split()
    for j in range(len(line)):
        if len(line[j]) == 4:
            facil.append(line[j])
        elif len(line[j]) > 4 and len(line[j]) <= 6:
            normal.append(line[j])
        elif len(line[j]) > 6 and line[j]:
            dificil.append(line[j])

def embaralha(nome):
     a = sample(nome,len(nome))
     d = ''.join(a)
     return d


while(1):
    ptsAtuais = 100
    dificuldade = input("Escolha qual dificuldade voce deseja (Facil - Normal - Dificil): ").lower()
    pontos = int(input("Escolha quantos pontos deseja perder: (20~100) "))
    print("Seus pontos: ", ptsAtuais)
    if dificuldade == "facil":
        palavraEscolhida = random.choice(facil)
        print("A palavra escolhida foi:", embaralha(palavraEscolhida))
    tentativa = input("Digite a palavra na sequncia certa: ")
    
    
    if tentativa == palavraEscolhida:
        print("Parabensssss!!! Você acertoou :)")
        break
    else:
        ptsAtuais -= pontos
        print("Errouu, tente mais uma vez")
    
