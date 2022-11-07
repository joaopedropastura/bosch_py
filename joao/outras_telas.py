from typing import final
import PySimpleGUI as sg

def tela_login():
    sg.theme('Black')
    layout = [
        [sg.Text("Usuario: "), sg.Input(key='user')],
        [sg.Text("Senha: "), sg.Input(key='pass', password_char='*')],
        [sg.Button("Entrar")]
    ]

    return sg.Window("Tela Login", layout=layout, finalize=True)

def tela_pedido():
    sg.theme("Black")
    layout = [
        [sg.Text('Faca seu pedido')],
        [sg.Checkbox("Big Mc", key='pedido1'), sg.Checkbox('Duplo Quarteirao', key='pedido2')],
        [sg.Checkbox("Mc Chicken", key="pedido3"), sg.Checkbox("Cheddar McMelt", key="pedido4")]
    ]
    return sg.Window("Tela Pedido", layout=layout, finalize=True)


janela1, janela2 = tela_login(), None

while True:
    janela, evento, valores = sg.read_all_windows()
    #fechar janela
    if janela == janela1 and evento == sg.WINDOW_CLOSED:
        break
    if janela == janela2 and evento == sg.WINDOW_CLOSED:
        break
    if valores['user'] == 'joaozinho avassalador' and valores['pass'] == 'joaocasado':
        janela1.hide()
        janela2 = tela_pedido()
    else:
        print("Usuario ou senha invalido")