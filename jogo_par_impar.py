# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 09:54:25 2022

@author: disrct
"""
import random

record = 0
vitorias = 0

print("---------------------NOVO-JOGO---------------------")

while(1):
    player = int(input("Digite um numero: "))
    rodada = input("PAR OU IMPAR? ").lower()

    pc = random.randrange(0, 11)
    result = player + pc

    print("O computador jogou: ", pc)
    print("RESULTADO = ", result, "\n")
    if rodada == "par" and result % 2 != 0:
        print("Você perdeu!")
        vitorias = 0
    else:
        vitorias += 1
        print("Você Ganhou!!! :)")
    if record < vitorias:
        record = vitorias
    print("VITORIAS: ", vitorias)
    print("RECORD: ", record)
    if int(input("Digite 0 para sair ou 1 para continuar: ")) == 0:
        break