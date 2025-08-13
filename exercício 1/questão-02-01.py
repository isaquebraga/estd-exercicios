primeiraNota = float(input("Digite a primeira nota: "))
segundaNota = float(input("Digite a segunda nota: "))

media = (primeiraNota + segundaNota) / 2

if media >= 7 and media < 10:
    print(f"Aprovado com média {media}.")
elif media < 7:
    print(f"Reprovado com média {media}.")
else:
    print(f"Aprovado com Distinção com média {media}.")