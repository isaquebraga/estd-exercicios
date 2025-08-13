altura = float(input("Informe sua altura em metros: "))
sexo = input("Informe seu sexo: [M/F] ").upper()

pesoIdeal = 0

if sexo == "M":
    pesoIdeal = (62.1 * altura) - 44.7
else: 
    pesoIdeal = (72.7 * altura) - 58

print(f"Com base nos dados que você me forneceu, seu peso ideal é {pesoIdeal:.2f}Kg.")