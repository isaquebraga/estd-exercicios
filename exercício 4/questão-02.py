def invertePalavra(string):
    if len(string) == 1:
        return string
    else:
        return string[-1] + invertePalavra(string[:-1])
        
string = input("Digite uma palavra: ")

print(invertePalavra(string))