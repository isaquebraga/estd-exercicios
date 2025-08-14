nomeUsuario = input("Informe o nome de usuário: ")
senhaUsuario = input("Informe o senha de usuário: ")

while nomeUsuario == senhaUsuario:
    print("Nome e senha iguais não são permitidos, tente novamente.")
    nomeUsuario = input("Informe o nome de usuário: ")
    senhaUsuario = input("Informe o senha de usuário: ")
