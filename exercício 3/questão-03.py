string = input("Digite um texto: ")

numeroDeEspacos = 0

for char in string:
    if char == " ":
        numeroDeEspacos += 1

cont = 0

for i in range(len(string)):
    if string[i] == " ":
        cont += 1
        if cont == numeroDeEspacos:
            print(string[i+1:])
