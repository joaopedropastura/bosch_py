import numpy as np
import pandas as pd

colunas = 6
linhas = 7
player1 = 'X'
player2 = 'O'
player = 1
matriz = np.full((linhas, colunas), ' ')

print("\n            bem vindo ao LIG-4")
print(" ------------------------------------------")

def update_matrix(jogada):
    global player
    for i in range(linhas-1, -1, -1):
        if matriz[i][jogada] == ' ':
            if player == 1:
                player = 0
                matriz[i][jogada] = player1
                break
            else:
                player = 1
                matriz[i][jogada] = player2
                break

def check_jogada(jogada):
    if matriz[0][jogada] == ' ':
        update_matrix(jogada)
    else:
        return 1
def check_win(matriz):
    df = pd.DataFrame(matriz)
    


def print_matrix(matriz):
    for i in range(colunas):
        print(f" |{i+1:^5}", end="")
    print("|\n ------------------------------------------")
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            print(f" |{matriz[l][c]:^5}", end='')
        print("|")
    print(" ------------------------------------------")

print_matrix(matriz)
check_win(matriz)
# while 1:
#     print(f"Vez do jogador: {player}")
#     jogada = int(input("Digite qual a coluna que deseja jogar: "))-1
#     if check_jogada(jogada) == 1:
#         print("Jogada invalida, tente jogar em outra coluna...")
#     print_matrix(matriz)
    