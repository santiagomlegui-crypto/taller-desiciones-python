primero = float(input("Ingrese el primer número: "))
segundo = float(input("Ingrese el segundo número: "))
tercero = float(input("Ingrese el tercer número: "))
cuarto = float(input("Ingrese el cuarto número: "))

grande = primero
if segundo > grande:
    grande = segundo
if tercero > grande:
    grande = tercero
if cuarto > grande:
    grande = cuarto

print("El número mayor es:", grande)
