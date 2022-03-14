from PySimpleGUI import PySimpleGUI as sg


sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha  '), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox("Salvar login e senha? ")],
    [sg.Button('Entrar'), sg.Button('Novo login'), sg.Button('Fechar')]
]

janela = sg.Window('Login', layout)


dbLogin = []
dbSenha = []
while True:
    eventos, valores = janela.read()
    if eventos in [sg.WINDOW_CLOSED, 'Fechar']:
        break

    if eventos == 'Novo login':
        dbLogin.append(valores['usuario'])
        dbSenha.append(valores['senha'])
        print(dbLogin, dbSenha)

    if eventos == 'Entrar':
        if valores['usuario'] in dbLogin:
            if valores['senha'] in dbSenha:
                print("Logado com sucesso")
            else:
                print("Senha incorreta!")
        else:
            print("Login incorreto!")