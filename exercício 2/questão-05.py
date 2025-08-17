def maior_de_2(num1, num2):
    if num1 > num2:
        return num1
    elif num1 == num2:
        return "Os números são iguais."
    else: 
        return num2
    
primeiroNumero = int(input("Digite um número: "))
segundoNumero = int(input("Digite um outro número: "))

if primeiroNumero!= segundoNumero:
    print(f"Entre {primeiroNumero} e {segundoNumero} o maior é {maior_de_2(primeiroNumero, segundoNumero)}.")
else:
    print(maior_de_2(primeiroNumero, segundoNumero))