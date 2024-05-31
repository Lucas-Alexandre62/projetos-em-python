import PySimpleGUI as sg
import string
from random import choice

sg.theme('Black')
tamanho = 24
valores = string.ascii_letters + string.digits + string.punctuation
senha = ''
for i in range(tamanho):
    senha+= choice(valores)

tamanho2 = 6
valores2 = string.ascii_letters + string.digits
conf = ''
for i in range(tamanho2):
    conf+=choice(valores2)

class PassGenerator:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Senha')],
            [sg.Text(senha) ],
            [sg.Text('Digite o texto da tela para confirmar: ')],
            [sg.Text(conf)],
            [sg.Input(key='Confirmacao')],
            [sg.Checkbox('Confirmar', key='Confirmar')],
            [sg.Button('Enviar'), sg.Button('Sair')],
            [sg.Text('Desenvolvido por  Lucas Alexandre')],
            ]
         # Janela
        janela = sg.Window('Password Generator').layout(layout)

        # Extrair os dados da tela
        self.Button, self.values = janela.Read()
    def Iniciar(self):
        Confirmar = self.values['Confirmar']
        Confirmacao = self.values['Confirmacao']
        if(Confirmacao == conf and Confirmar == True ):
            print(f'Password: {senha}')
            a = open('senhas.txt', 'r+') 
            a.write(f'Password: {senha}\n')
            print('Senha armazenada com sucesso!')
        else:
            print(f'Password {senha}')
            print('Senha não armazenada.')
tela = PassGenerator()
tela.Iniciar()
