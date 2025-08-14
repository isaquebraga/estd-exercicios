numeros = []

for i in range(5):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))
    
for i in range(5):
    if i == 0:
        maior = numeros[i]
    elif numeros[i] > maior:
        maior = numeros[i]
        
print(f"O maior número digitado foi {maior}.")
        