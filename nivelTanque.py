capacidad = int(input("Ingrese la cantidad de litros del tanque: "))
if capacidad < 250:
    print("Abrir la llave")
else:
    if capacidad > 450:
        print("Cerrar la llave")
    else:
        print("Mantener la llave cerrada")
