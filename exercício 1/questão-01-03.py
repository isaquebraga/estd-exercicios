horas = float(input("Quantas horas você trabalha por mês? "))
salarioPorHora = float(input("E quanto você ganha por hora? R$"))

salarioMensal = horas * salarioPorHora

string = f"Seu salário mensal é de R${salarioMensal:.2f}"
novaString = string.replace(".", ",")
print(novaString+".")