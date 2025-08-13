numeros = []

for i in range(3):
    numeros.append(int(input("Digite um número: ")))

cont = 0

for numero in numeros:
    if cont == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    
    cont += 1

print(f"O maior número é o {maior} e o menor número é o {menor}.")