def contaLetras(letra, palavra):
    if palavra == "":
        return 0
    
    if palavra[0] == letra:
        return 1 + contaLetras(palavra[1:], letra)
    else:
        return 0 + contaLetras(palavra[1:], letra)

palavra = input("Digite uma palavra: ")
letra = input("Digite qual é a letra que você deseja procurar: ")

print(contaLetras(letra, palavra))