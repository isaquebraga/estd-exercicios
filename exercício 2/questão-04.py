def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else: 
        return -1

primeiroNumero = int(input("Digite um número: "))
segundoNumero = int(input("Digite um outro número: "))
print(compare(primeiroNumero, segundoNumero))