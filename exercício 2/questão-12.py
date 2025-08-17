def eh_primo(numero):
    cont = 0
    
    for i in range(1, numero + 1):
        if numero % i == 0:
            cont += 1
            
    if cont == 2:
        return True
    else: 
        return False

numero = int(input("Digite um número: "))

print(eh_primo(numero))