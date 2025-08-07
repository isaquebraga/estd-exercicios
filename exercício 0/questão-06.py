def verificaNumero(numero):
    if numero % 2 == 0:
        numero /= 2
    else:
        numero = (3 * numero) + 1
    return int(numero)
    
entrada = int(input("Digite um número: "))
resultado = verificaNumero(entrada)
saida = f"{resultado}"

while resultado != 1:
    resultado = verificaNumero(resultado)
    saida += f" -> {resultado}"

print(saida)