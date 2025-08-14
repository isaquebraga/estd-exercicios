def fatorial(numero):
    if numero == 0:
        return 1
    else:
        fatorial = numero

        for i in range(1, numero):
            fatorial *= numero - i
        
        return fatorial

numero = int(input("Digite um número: "))
print(fatorial(numero))