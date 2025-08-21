def contaNumeros(numero):
    if numero == 0:
        print(numero)
    else:
        print(numero)
        contaNumeros(numero - 1)
    
numero = int(input("Digite um número: "))

contaNumeros(numero)