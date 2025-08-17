def fibonacci(termo):
    termos = [0, 1]
    resultado = 0
    
    if termo == 0:
        resultado = 0
    elif termo == 1:
        resultado = 1
    else:
        for i in range(termo-2):
            termos.append(termos[-2]+termos[-1])
        
        for numero in termos:
            resultado += numero
        
    return resultado
    
numero = int(input("Digite um número: "))

print(f"A soma dos termos da sequência de Fibonacci de {numero} é {fibonacci(numero)}.")