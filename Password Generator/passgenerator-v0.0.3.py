# Inicio

# Importando Módulos

import PySimpleGUI as sg
import string
from random import choice

# declarando as variaveis

sg.theme('Black')
tamanho = 24
valores = string.ascii_letters + string.digits + string.punctuation
senha = ''

# loop para gerar as senhas

for i in range(tamanho):
    senha+= choice(valores)

tamanho2 = 6
valores2 = string.ascii_letters + string.digits
conf = ''

# manipulando arquivo

o = open('senhas.txt', 'r+')
b = o.read()
c = b
for i in range(tamanho2):
    conf+=choice(valores2)

#   classes e funções

class JanelaOp:
    def __init__(self):
        #layout
        jam_layout = [
            [sg.Text('Bem vindo')],
            [sg.Text("Escolha uma opção para continuar")],
            [sg.Checkbox('Gerar Senha', key='gerar')],
            [sg.Checkbox('Ver Senhas Armazenadas', key='senhas')],
            [sg.Button('Confirmar')],
        ] 
        # janela
        janela1 = sg.Window('Inicio').layout(jam_layout)

        # Extrair os dados da tela
        self.Checkbox, self.values = janela1.Read()

        # Fechar a janela inicial

        janela1.close()

    # Iniciar a nova janela
    def Jam_Iniciar(self):
        gerar = self.values['gerar']
        senhas = self.values['senhas']

        if gerar == True:
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
                    janela = sg.Window('Generator', size=(600, 600)).layout(layout)

                    # Extrair os dados da tela
                    self.Button, self.values = janela.Read()

                    janela.close()

                def Iniciar(self):
                    Confirmar = self.values['Confirmar']
                    Confirmacao = self.values['Confirmacao']

                    if(Confirmacao == conf and Confirmar == True ):
                        print(f'Password: {senha}')
                        a = open('senhas.txt', 'a') 
                        a.write(f'Password: {senha}\n')
                        print('Senha armazenada com sucesso!')
                    else:
                        print(f'Password {senha}')
                        print('Senha não armazenada.')

            tela = PassGenerator()
            tela.Iniciar()

        if senhas == True:
            class SenhasGeradas:
                def __init__(self):
                    # layout
                    ger_layout = [
                        [sg.Text("Senhas geradas")],
                        [sg.Text(c)],
                        [sg.Button("Sair")],
                    ]

                    # janela
                    janela3 = sg.Window("Geradas").layout(ger_layout)

                    # salvando valores
                    self.Button, self.values = janela3.Read()
                def GeradasIniciar(self):
                    a = 1
        ger = SenhasGeradas()
        ger.GeradasIniciar()


jam = JanelaOp()
jam.Jam_Iniciar()

# Fim