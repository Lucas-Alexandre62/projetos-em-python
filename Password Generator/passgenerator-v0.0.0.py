import string
from random import choice

tamanho = 24
valores = string.ascii_letters + string.digits + string.punctuation
senha = ''
for i in range(tamanho):
    senha+= choice(valores)

print(f'Password: {senha}')
a = open('senhas.txt', 'a') 
a.write(f'Password: {senha}\n')
print('Senha armazenada com sucesso!')