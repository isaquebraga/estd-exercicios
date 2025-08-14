soma = 0

for i in range(5):
    soma += int(input(f"Digite o {i+1}º número: "))
    
media = soma / 5

print(f"A soma dos números digitados é {soma} e a média é {media:.2f}.")