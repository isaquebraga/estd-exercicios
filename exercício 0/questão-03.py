numero = int(input("Digite um número para saber o seu fatorial: "))
cont = numero
fatorial = 1

if numero > 0:
    for i in range(1, numero):
        fatorial *= cont
        cont -= 1
        
print(f"O fatorial de {numero} é {fatorial}.")