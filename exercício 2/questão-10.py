def eh_data_valida(dia, mes, ano):
    if ano % 4 == 0:
        if mes == 1 and dia > 0 and dia < 32:
            return True
        elif mes == 2 and dia > 0 and dia < 30:
            return True
        elif mes == 3 and dia > 0 and dia < 32:
            return True
        elif mes == 4 and dia > 0 and dia < 31:
            return True
        elif mes == 5 and dia > 0 and dia < 32:
            return True
        elif mes == 6 and dia > 0 and dia < 31:
            return True
        elif mes == 7 and dia > 0 and dia < 32:
            return True
        elif mes == 8 and dia > 0 and dia < 32:
            return True
        elif mes == 9 and dia > 0 and dia < 31:
            return True
        elif mes == 10 and dia > 0 and dia < 32:
            return True
        elif mes == 11 and dia > 0 and dia < 31:
            return True
        elif mes == 12 and dia > 0 and dia < 32:
            return True
        else:
            return False
    elif ano % 4 != 0:
        if mes == 1 and dia > 0 and dia < 32:
            return True
        elif mes == 2 and dia > 0 and dia < 29:
            return True
        elif mes == 3 and dia > 0 and dia < 32:
            return True
        elif mes == 4 and dia > 0 and dia < 31:
            return True
        elif mes == 5 and dia > 0 and dia < 32:
            return True
        elif mes == 6 and dia > 0 and dia < 31:
            return True
        elif mes == 7 and dia > 0 and dia < 32:
            return True
        elif mes == 8 and dia > 0 and dia < 32:
            return True
        elif mes == 9 and dia > 0 and dia < 31:
            return True
        elif mes == 10 and dia > 0 and dia < 32:
            return True
        elif mes == 11 and dia > 0 and dia < 31:
            return True
        elif mes == 12 and dia > 0 and dia < 32:
            return True
        else:
            return False
        
data = input("Digite uma data: ")

dataSeparada = data.split("/")

for i in range(0, 3):
    dataSeparada[i] = int(dataSeparada[i])
    
print(eh_data_valida(dataSeparada[0], dataSeparada[1], dataSeparada[2]))