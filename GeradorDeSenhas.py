a = open("senhas.txt" ,"r+")
b = []
c = a.read()
d = int(input("[1] Inserir nova senha   [2] Exibir senhas armazenadas   [3] Sair\n"))
f = True

while f:
	while d == 1:
		senha = input("Digite a senha: ")
		if not senha in c:
			a = open("senhas.txt", "a")
			e = a.write(f'Password: {senha}\n')
			print("Senha armazenada com sucesso!")
		else:
			print("Senha ja existente.")
		d = int(input("[1] Inserir nova senha   [2] Exibir senhas armazenadas   [3] Sair\n"))

	while d == 2:
		a = open("senhas.txt", "r")
		c = a.read()
		print(c)
		d = int(input("[1] Inserir nova senha   [2] Exibir senhas armazenadas   [3] Sair\n"))

	while d ==  3:
		exit("Saindo...")
		f = False
