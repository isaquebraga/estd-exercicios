nome = input("Informe o nome: ")

numeroDeEspacos = 0

for char in nome:
    if char == " ":
        numeroDeEspacos += 1

cont = 0

iniciais = []

for i in range(len(nome)):
    if i == 0:
        iniciais.append(nome[i])
    elif nome[i] == " ":
        cont += 1
        if cont == numeroDeEspacos:
            ultimoNome = nome[i+1:]
        else:
            iniciais.append(nome[i+1])

if numeroDeEspacos == 0:
    ultimoNome = nome

stringFormatada = f"{ultimoNome}, "

for inicial in iniciais:
    stringFormatada += f"{inicial.capitalize()}. "
    
print(stringFormatada)