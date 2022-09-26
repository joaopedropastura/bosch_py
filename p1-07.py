txt = open("notas.txt", 'a')
result = {}
tam = int(input("Digite a quantidade de alunos: "))
notastds = int(input("Digite a quantidade de notas para cada aluno: "))
for i in range(tam):
    nome = input("Digite o nome do aluno: ")
    txt.write(nome)
    nota = 0
    for notas in range(notastds):
        nota += float(input(f"Digite a nota {notas+1} do aluno {nome}: "))
        txt.write(',' + str(nota))
    txt.write('\n')
    temp = nota/notastds
    result.update({nome : temp})
txt.close

while(1):
    aluno = input("Digite o nome do aluno que deseja consultar a nota: ")
    print("Ou digite \"sair\" para parar a pesquisa!")
    if aluno == "sair":
        break
    print(result.get(aluno, "Aluno nao encontrado, digite novamente..."))

test = open("notas.txt", 'r')
tempt = {}
for linhas in test:
    aux = linhas[:-1].split(',')
    totalAux = len(aux)
    soma = 0
    for index in range(1,totalAux):
        soma += float(aux[index])
    media = soma/(totalAux-1)
    tempt.update({aux[0]:media})
for key in tempt.keys():
    print(key, "{:.2f}".format(tempt[key]))

while 1:
    aluno = input("Digite o nome do aluno que deseja consultar a nota \nOu digite \"sair\" para parar a pesquisa: ")
    if aluno == "sair":
        break
    print(tempt.get(aluno, "Aluno nao encontrado, digite novamente..."))

