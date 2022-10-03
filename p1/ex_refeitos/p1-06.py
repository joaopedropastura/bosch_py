def change_to_num(phrase):
    encrypt = ''
    for i in phrase:
        encrypt += str((ord(i)-97))
    return encrypt

def change_to_bin(encrypt):
    count = 0
    for i in encrypt:
        binario = str(bin(int(i)))
        binario = binario[2:]
        binario = '0'*(4-len(binario)) + binario
        count += 1
        print(binario, end='_' if count != (len(encrypt)) else None)


def encrypt():
    phrase = input("Digite a frase a ser criptografada: ").lower()
    return phrase

num = change_to_num(encrypt())
change_to_bin(num)