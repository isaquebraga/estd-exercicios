string = input("Digite um texto: ").lower()
antigaPalavra = input("Digite a palavra a ser substituída: ").lower().strip()

if antigaPalavra not in string:
    print("Palavra não encontrada no texto digitado.")
else: 
    novaPalavra = input("Digite a nova palavra: ").lower().strip()

    if " " not in string:
        novaString = novaPalavra

    listaCaracteres = []
    listaPalavrasString = []
    novaString = ""

    for char in string:
        listaCaracteres.append(char)
        
    listaCaracteres.append(" ")

    palavra = ""

    for i in listaCaracteres:
        if i != " ":
            palavra += i
        else:
            listaPalavrasString.append(palavra)
            palavra = ""    
            
    for i in range(len(listaPalavrasString)):
        if listaPalavrasString[i] == antigaPalavra:
            listaPalavrasString[i] = novaPalavra
        elif listaPalavrasString[i] == f"{antigaPalavra}.":
            listaPalavrasString[i] = f"{novaPalavra}."
        elif listaPalavrasString[i] == f"{antigaPalavra},":
            listaPalavrasString[i] = f"{novaPalavra},"
        elif listaPalavrasString[i] == f"{antigaPalavra}!":
            listaPalavrasString[i] = f"{novaPalavra}!"
        elif listaPalavrasString[i] == f"{antigaPalavra}?":
            listaPalavrasString[i] = f"{novaPalavra}?"
            
    for palavra in listaPalavrasString:
        novaString += f"{palavra} "

    print(novaString.capitalize())