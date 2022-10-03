gabarito = ['a','a','a','a','a','a','a','a','a','a']
respostas = []
erradas = []
result = 0
for i in range(10):
    temp = input(f"Qual a sua resposta para a questao {i+1}?")
    respostas.append(temp)
    if gabarito[i] == respostas[i]:
        result +=1 
    else:
        aux = i+1
        erradas.append(aux)

print(f"Sua nota foi {result}.")
print(f"Voce errou as respostas: {erradas}")

