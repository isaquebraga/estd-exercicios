def retornaTitulo(string):
    stringFormatada = ""
    
    for char in string:
        stringFormatada += f"{char.upper()} "
        
    return stringFormatada

string = input("Digite o títuto: ")
    
print(retornaTitulo(string))