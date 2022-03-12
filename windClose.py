from PySimpleGUI import PySimpleGUI as sg



class WindowClose:
    sg.theme('Reddit')
    layoutclose = [
        [sg.Text('Fechando')]
    ]
    janelaclose = sg.Window('Closing', layoutclose)
    while True:
        espera = janelaclose.read()