def fatorialDuplo(numero):
    if numero % 2 == 0:
        return "Não é um número ímpar."
    elif numero == 1:
        return 1
    else:
        return numero * fatorialDuplo(numero - 2)

numero = int(input("Digite um número ímpar: "))

print(fatorialDuplo(numero))