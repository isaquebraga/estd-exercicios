def dia_da_semana(dia):
    dias = {
        1: "domingo",
        2: "segunda-feira",
        3: "terça-feira",
        4: "quarta-feira",
        5: "quinta-feira",
        6: "sexta-feira",
        7: "sábado"
    }
    
    if dia > 0 and dia < 8:
        return dias[dia]
    else:
        return "Valor inválido."
    
numero = int(input("Digite um número: "))

if numero > 0 and numero < 8:
    print(f"O dia correspondente a {numero} é {dia_da_semana(numero)}.")
else:
    print(dia_da_semana(numero))