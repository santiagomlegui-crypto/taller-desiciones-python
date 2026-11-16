real = float(input("Ingrese un número real (x): "))
if real > 3.5 and real <= 7.8:
    print("El número", real, "se encuentra en el rango (3.5, 7.8]")
else:
    if real >= 4.5 and real < 9.3:
        print("El número", real, "se encuentra en el rango [9.3, 4.5)")
    else:
        if real >= 23.4 and real <= 45.3:
            print("El número", real, "se encuentra en el rango [23.4, 45.3]")
        else:
            print("El número", real, "NO se encuentra en ninguno de los rangos.")
