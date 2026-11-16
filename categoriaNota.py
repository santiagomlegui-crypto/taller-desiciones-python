resultado = float(input("Digite la nota del estudiante: "))
if resultado >= 0 and resultado < 3.0:
    print("insuficiente")
else:
    if resultado > 3.5 and resultado < 4.0:
        print("Sobresaliente")
    else:
        if resultado >= 4.0 and resultado < 5.0:
            print("Excelente")
        else:
            if resultado >= 3.0 and resultado <= 3.5:
                print("Aceptable")
            else:
                print("Valor no valido")
