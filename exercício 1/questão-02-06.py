data = input("Digite uma data: ")

dataSeparada = data.split("/")

for i in range(0, 3):
    dataSeparada[i] = int(dataSeparada[i])

if dataSeparada[2] % 4 == 0:
    if dataSeparada[1] == 1 and dataSeparada[0] > 0 and dataSeparada[0] < 32:
        print("É uma data válida.")
    elif dataSeparada[1] == 2 and dataSeparada[0] > 0 and dataSeparada[0] < 30:
        print("É uma data válida.")
    elif dataSeparada[1] == 3 and dataSeparada[0] > 0 and dataSeparada[0] < 32:
        print("É uma data válida.")
    elif dataSeparada[1] == 4 and dataSeparada[0] > 0 and dataSeparada[0] < 31:
        print("É uma data válida.")
    elif dataSeparada[1] == 5 and dataSeparada[0] > 0 and dataSeparada[0] < 32:
        print("É uma data válida.")
    elif dataSeparada[1] == 6 and dataSeparada[0] > 0 and dataSeparada[0] < 31:
        print("É uma data válida.")
    elif dataSeparada[1] == 7 and dataSeparada[0] > 0 and dataSeparada[0] < 32:
        print("É uma data válida.")
    elif dataSeparada[1] == 8 and dataSeparada[0] > 0 and dataSeparada[0] < 32:
        print("É uma data válida.")
    elif dataSeparada[1] == 9 and dataSeparada[0] > 0 and dataSeparada[0] < 31:
        print("É uma data válida.")
    elif dataSeparada[1] == 10 and dataSeparada[0] > 0 and dataSeparada[0] < 32:
        print("É uma data válida.")
    elif dataSeparada[1] == 11 and dataSeparada[0] > 0 and dataSeparada[0] < 31:
        print("É uma data válida.")
    elif dataSeparada[1] == 12 and dataSeparada[0] > 0 and dataSeparada[0] < 32:
        print("É uma data válida.")
    else:
        print(f"{dataSeparada[0]}/{dataSeparada[1]}/{dataSeparada[2]} não é uma data válida.")
elif dataSeparada[2] % 4 != 0:
    if dataSeparada[1] == 1 and dataSeparada[0] > 0 and dataSeparada[0] < 32:
        print("É uma data válida.")
    elif dataSeparada[1] == 2 and dataSeparada[0] > 0 and dataSeparada[0] < 29:
        print("É uma data válida.")
    elif dataSeparada[1] == 3 and dataSeparada[0] > 0 and dataSeparada[0] < 32:
        print("É uma data válida.")
    elif dataSeparada[1] == 4 and dataSeparada[0] > 0 and dataSeparada[0] < 31:
        print("É uma data válida.")
    elif dataSeparada[1] == 5 and dataSeparada[0] > 0 and dataSeparada[0] < 32:
        print("É uma data válida.")
    elif dataSeparada[1] == 6 and dataSeparada[0] > 0 and dataSeparada[0] < 31:
        print("É uma data válida.")
    elif dataSeparada[1] == 7 and dataSeparada[0] > 0 and dataSeparada[0] < 32:
        print("É uma data válida.")
    elif dataSeparada[1] == 8 and dataSeparada[0] > 0 and dataSeparada[0] < 32:
        print("É uma data válida.")
    elif dataSeparada[1] == 9 and dataSeparada[0] > 0 and dataSeparada[0] < 31:
        print("É uma data válida.")
    elif dataSeparada[1] == 10 and dataSeparada[0] > 0 and dataSeparada[0] < 32:
        print("É uma data válida.")
    elif dataSeparada[1] == 11 and dataSeparada[0] > 0 and dataSeparada[0] < 31:
        print("É uma data válida.")
    elif dataSeparada[1] == 12 and dataSeparada[0] > 0 and dataSeparada[0] < 32:
        print("É uma data válida.")
    else:
        print(f"{dataSeparada[0]}/{dataSeparada[1]}/{dataSeparada[2]} não é uma data válida.")