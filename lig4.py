import numpy as np 

linhas = 7
colunas = 6
matriz = np.full([colunas,linhas], " ")

print("\n        bem vindo ao LIG-4")
print(" -------------------------------------")

jogador1 = "X"
jogador2 = "O"


def update_matriz(jogada, player):
    for i in range(linhas, -1, -1):
        if matriz[i][jogada] == " ":
            if player == 0:    
                player = 1
                matriz[i][jogada] = jogador1
                return (print_matriz(matriz))
            else:
                player = 0
                matriz[i][jogada] = jogador2
                return (print_matriz(matriz))


def check_column(jogada, player):
    if matriz[jogada][0] != " ":
        return False
    update_matriz(jogada, player)        


def print_matriz(matriz): 
    for i in range(colunas):
        print(f"    {i+1} ", end = '')
    print("\n -------------------------------------")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f" |  {matriz[i][j]} ", end = '')
        print("")


print_matriz(matriz)

while 1:
    player = 1
    print(f"Vez do jogador: {player}")
    jogada = int(input("digite a coluna: "))
    check_column(jogada, player)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    