lados = []

for lado in range(3):
    lados.append(int(input("Digite um dos lados do triângulo: ")))

if lados[0] + lados[1] > lados[2] and lados[1] + lados[2] > lados[0] and lados[0] + lados[2] > lados[1]:
    quantidadeLadosIguais = 0
    cont = 0

    for i in range(0, 2):
        if cont < 3:
            if lados[i] == lados[cont + 1]:
                quantidadeLadosIguais += 1
        else:
            cont = 0
        cont += 1
    
    if quantidadeLadosIguais == 0:
        print("É um triângulo escaleno.")
    elif quantidadeLadosIguais == 1:
        print("É um triângulo isóceles.")
    else:
        print("É um triângulo equilátero.")
else:
    print("Não é um triângulo.")