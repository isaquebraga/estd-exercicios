numeroDeLinhas = int(input("Digite o número de linhas que você deseja: "))
linha = ""
soma = 0

for i in range(1, numeroDeLinhas+1):
    if i == 1:
        linha = "1"
        print(linha)
    else:
        for n in range(i):
            soma += i
            linha = f"{i}"
            for m in range(n):
                soma += i
                linha += f" {soma}"
            soma = 0
    print(linha)