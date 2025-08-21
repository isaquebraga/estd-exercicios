def geraNomeUsuario(string):
    iniciais = []

    for i in range(len(nome)):
        if i == 0:
            iniciais.append(nome[i])
        elif nome[i] == " ":
            iniciais.append(nome[i+1])
            
    stringFormatada = ""

    for inicial in iniciais:
        stringFormatada += f"{inicial.lower()}"
    
    stringFormatada += "@dominio.com"
    
    return stringFormatada

nome = input("Informe o nome completo do usuário: ")

print(geraNomeUsuario(nome))