def hipotenusa(cateto1, cateto2):
    hipotenusa = ((cateto1 ** 2) + (cateto2 ** 2)) ** 0.5
    
    return hipotenusa

primeiroCateto = float(input("Digite o valor do primeiro cateto: "))
segundoCateto = float(input("Digite o valor do segundo cateto: "))

print(f"O valor da hipotenusa para os catetos informados ({primeiroCateto:.2f}, {segundoCateto:.2f}) é {hipotenusa(primeiroCateto, segundoCateto):.2f}.")