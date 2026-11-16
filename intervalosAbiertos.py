a1 = int(input("Ingrese el minimo del intervalo 1: "))
b1 = int(input("Ingrese el maximo del intervalo 1: "))
a2 = int(input("Ingrese el minimo del intervalo 2: "))
b2 = int(input("Ingrese el maximo del intervalo 2: "))
a3 = int(input("Ingrese el minimo del intervalo 3: "))
b3 = int(input("Ingrese el maximo del intervalo 3: "))
evaluado = int(input("Ingrese el numero a evaluar: "))

if (a1 < evaluado < b1) or (a2 < evaluado < b2) or (a3 < evaluado < b3):
    print("El numero esta dentro de un intervalo")
else:
    print("El numero esta fuera de los intervalos")
