import time

from PySimpleGUI import PySimpleGUI as sg


sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha  '), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox("Salvar login e senha? ")],
    [sg.Button('Entrar'), sg.Button('Novo login'), sg.Button('Fechar')]
]

janela = sg.Window('Login', layout)

while True:
    eventos, valores = janela.read()
    if eventos in [sg.WINDOW_CLOSED, 'Fechar']:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'attom' and valores['senha'] == '123':
            break
