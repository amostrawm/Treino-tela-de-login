from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha  '), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox("Salvar login e senha? ")],
    [sg.Button('Entrar'), sg.Button('Criar login'), sg.Button('Fechar')]
]

janela = sg.Window('Login', layout)

layout_2 = [
    [sg.Text('Novo usuário'), sg.Input(key='novo_usuario', size=(20, 1))],
    [sg.Text('Nova senha  '), sg.Input(key='nova_senha', password_char='*', size=(20, 1))],
    [sg.Button('Criar login'), sg.Button('Fechar')]
]

janela_2 = sg.Window('Criar login', layout_2)