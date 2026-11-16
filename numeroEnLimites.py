desde = int(input("Ingrese el valor minimo: "))
hasta = int(input("Ingrese el valor maximo: "))
dato = int(input("Ingrese el numero a evaluar: "))
if dato >= desde and dato <= hasta:
    print("El numero esta dentro del intervalo")
else:
    print("El numero esta fuera del intervalo")
