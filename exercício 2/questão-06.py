def maior_de_3(num1, num2, num3):
    maior = num1
    
    if num2 > maior:
        maior = num2
        
    if num3 > maior:
        maior = num3
    
    if num1 == num2 and num1 == num3:
        return "Os números são iguais."
    else:
        return maior


primeiroNumero = int(input("Digite um número: "))
segundoNumero = int(input("Digite um outro número: "))
terceiroNumero = int(input("Digite um terceiro número: "))

if primeiroNumero!= segundoNumero and primeiroNumero != terceiroNumero:
    print(f"Entre {primeiroNumero}, {segundoNumero} e {terceiroNumero} o maior é {maior_de_3(primeiroNumero, segundoNumero, terceiroNumero)}.")
else:
    print(maior_de_3(primeiroNumero, segundoNumero, terceiroNumero))