clase = input("Ingrese el tipo de articulo: ")
monto = float(input("Ingrese el precio del articulo: "))

if clase == "Textil" or clase == "textil":
    ahorro = monto * 0
elif clase == "Electrodomestico" or clase == "electrodomestico":
    ahorro = monto * 0.037
elif clase == "Elementos de cocina" or clase == "elementos de cocina":
    ahorro = monto * 0.042
elif clase == "Videojuego" or clase == "videojuego":
    ahorro = monto * 0.078
else:
    print("Tipo de articulo no valido")
    exit()

print("Valor del descuento es: $", ahorro)
print("Precio final: $", monto - ahorro)
