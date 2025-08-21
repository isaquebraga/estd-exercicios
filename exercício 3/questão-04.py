string = input("Informe o nome do passageiro: ")

numeroDeEspacos = 0

for char in string:
    if char == " ":
        numeroDeEspacos += 1

cont = 0

for i in range(len(string)):
    if string[i] == " ":
        cont += 1
        if cont == 1:
            primeiroNome = string[:i]
        if cont == numeroDeEspacos:
            ultimoNome = string[i+1:]

print(f"Passageiro: {ultimoNome}/{primeiroNome}.")