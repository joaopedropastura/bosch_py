from tkinter import Button
import PySimpleGUI as sg

def tela_login():
    sg.theme("Reddit")
    layout = [
        [sg.Text("Usuario: "), sg.Input(key='user')],
        [sg.Text("Senha: "), sg.Input(key='pass', password_char='*')],
        [sg.Button("Entrar")]
    ]

    return sg.Window("Lista de compras", layout=layout, finalize=True)


def tela_addItem():
    sg.theme('Reddit')
    item = 0
    layout = [
        [sg.Input(key='item'), sg.Input(key='value')],        
        [sg.Button("Lista de compras", key="lista"),sg.Button("Adicionar item", key="addItem")]
    ]
    return sg.Window("Incluir item a lista", layout=layout, finalize=True)


def tela_listaComp():
    sg.theme('Reddit')
    item = 0
    layout = [
        [sg.Input(key='item'), sg.Input(key='value')],        
    ]
    return sg.Window("itens da lista", layout=layout, finalize=True)


janelaLogin, janelaAddItem, janelaLista = tela_login(), None, None
listaTotal = {}
while True:
    
    janela, evento, valores = sg.read_all_windows()
    
    if janela == janelaLogin and evento == sg.WINDOW_CLOSED:
        break
    if janela == janelaAddItem and evento == sg.WINDOW_CLOSED:
        break

    if evento == 'Entrar':
        if valores['user'] == 'jo' and valores['pass'] == 'j':
            janelaLogin.hide()
            janelaAddItem = tela_addItem()
    if valores == "lista":
        janelaAddItem.hide()
    if evento == "addItem":
        listaTotal.update((valores['item'], valores['value']))
        print(listaTotal)





    
