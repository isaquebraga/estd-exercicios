def contaNumeros(numero):
    if numero == 0:
        print(numero)
    else:
        contaNumeros(numero - 1)
        print(numero)
    
numero = int(input("Digite um número: "))

contaNumeros(numero)