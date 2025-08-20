string = input("Digite um texto:")

cont = 0

for letra in string:
    if letra == " ":
        cont += 1

if cont == 0:
    print(f"Número de palavras: {cont} palavras.")
else:
    print(f"Número de palavras: {cont+1} palavras.")