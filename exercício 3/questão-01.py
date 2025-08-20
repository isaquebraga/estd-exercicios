palavra = input("Digite uma palavra: ")
palavraInvertida = ""

for i in range(1, len(palavra) + 1):
    palavraInvertida += palavra[-i]

if palavra == palavraInvertida:
    print(f"{palavra.capitalize()} é palíndroma.")
else:
    print(f"{palavra.capitalize()} não é palíndroma.")