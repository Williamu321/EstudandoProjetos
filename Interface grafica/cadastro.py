from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char ='*', size=(20, 1))],
    [sg.Checkbox('Salvar o login²')],
    [sg.Button('Entrar')],
    [sg.Text('',key = 'Logado com sucesso')]
]
# Janela
janela = sg.Window('Tela de Login', layout)

# Ler os eventos

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Will' and valores['senha'] == '123321':
            janela['Logado com sucesso'].update(f'Voce agora esta logado')
        else:
            janela['Logado com sucesso'].update(f'Usuario ou Senha esta incorreto.')



