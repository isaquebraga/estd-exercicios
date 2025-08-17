def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

numero = int(input("Digite um número: "))

print(f"O número {numero} é {par_ou_impar(numero)}.")