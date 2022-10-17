import random

animal = ["cachorro", "girafa", "elefante", "crocodilo", "baleia", "abelha", "hipopotamo"]
objeto = ["estante", "caderno", "televisao", "geladeira"]
fruta = ["banana", "creamberry", "strawberry", "watermelon", "pineapple"]
list_game = []
words_bank = [animal, objeto, fruta]

rand_idx = random.randrange(0, len(words_bank))
rand_list = words_bank[rand_idx]
rand_word = rand_list[random.randint(0, len(rand_list) -1)]

list_word = list(rand_word)
list_game = ["_" for x in list_word]

def check_word(word, tentativas, qt_letras):
	flag = 0
	words = 0
	for i in range(len(list_word)):
		if word == list_word[i]:
			list_game[i] = word
			flag = 1
			words += 1
	if flag == 0:
		return tentativas - 1, (qt_letras -(words*-1))
	else:
		return tentativas, (qt_letras -(words*-1)
)
# def fail_tempt():
# 	return tentativas -= 1

def print_jogo_atual():
	for i in list_game:
		print(i + "  ", end='')

def main_game():
	len_word = 0
	print()
	print(f"A dica é: {words_bank[rand_idx]} e possui {len(rand_word)} letras\n")
	tentativas = 6
	while tentativas != 0 and len_word < len(list_word):
		word = input("Digite uma letra: ")
		tentativas, len_word = check_word(word, tentativas, len_word)
		print_jogo_atual()
		print("\n\ntentativas restantes: ", tentativas)

	if tentativas > 0:
		print("PARABENNNSNSS!!! VOCE GANHOU")
	else:
		new_tempt = input("Poxa que pena :(\nDigite 1 para tentar novamente: ")
		if new_tempt == '1':
			main_game()
# print(rand_list)
# print(rand_idx)
# print(rand_word)
# print_jogo_atual()
main_game()
