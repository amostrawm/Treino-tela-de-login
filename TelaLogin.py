import layout2
from layout2 import sg
login = []
senha = []
while True:
    eventos, valores = layout2.janela.read()
    if eventos in [sg.WINDOW_CLOSED, 'Fechar']:
        print("Fechando")
        break
    if eventos == 'Criar login':
        eventos_2, valores_2 = layout2.janela_2.read()
        while True:
            if eventos_2 == 'Criar login':
                login.append(['novo_usuario'])
                senha.append(['nova_senha'])
                eventos_2 = sg.WINDOW_CLOSED


