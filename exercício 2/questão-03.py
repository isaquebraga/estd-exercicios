def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

numero = int(input("Digite um número: "))
print(par_ou_impar(numero))