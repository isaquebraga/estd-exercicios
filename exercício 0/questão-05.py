def verificaNumero(numero):
    if numero % 2 == 0:
        numero /= 2
    else:
        numero = (3 * numero) + 1
    print(int(numero))
    
numero = int(input("Digite um número: "))
verificaNumero(numero)