parcial1 = float(input("Ingrese la nota 1: "))
parcial2 = float(input("Ingrese la nota 2: "))
parcial3 = float(input("Ingrese la nota 3: "))
parcial4 = float(input("Ingrese la nota 4: "))
parcial5 = float(input("Ingrese la nota 5: "))

nota_final = (parcial1 + parcial2 + parcial3 + parcial4 + parcial5) / 5

if nota_final > 5:
    print("Error: notas invalidas, formato entre 0.0 y 5.0")
else:
    if nota_final > 3.5:
        print("Gano el curso")
        print("Su nota es:", nota_final)
    else:
        print("Perdio el curso")
        print("Su nota es:", nota_final)
