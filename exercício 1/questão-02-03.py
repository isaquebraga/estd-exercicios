dias = {
    1: "domingo",
    2: "segunda-feira",
    3: "terça-feira",
    4: "quarta-feira",
    5: "quinta-feira",
    6: "sexta-feira",
    7: "sábado"
}

numero = int(input("Digite um número de 1 a 7: "))

while numero < 1 or numero > 7:
    numero = int(input("Número inválido. Digite novamente: "))

print(f"O dia correspondente a {numero} é {dias[numero]}.")