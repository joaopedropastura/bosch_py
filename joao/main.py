from turtle import window_width
import PySimpleGUI as sg

sg.theme('Reddit')
#layout
layout = [[sg.Text("Usuario: "), sg.Input(key='user')], [sg.Text("Senha: "), sg.Input(key='pass', password_char='*')],[sg.Button("Entrar")]]


#criar janela


window = sg.Window("Tela da mamada", layout)

#ler eventos

while True:
    eventos, valores = window.read()

    #fechar janela
    if eventos == sg.WINDOW_CLOSED:
        break
    if valores['user'] == 'flavinDaSaveiroRebaixada' and valores['pass'] == 'somBolado':
        print("Bem vindo, flavin avassalador")

    else:
        print("user errado")

