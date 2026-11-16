p = float(input("Ingrese a: "))
q = float(input("Ingrese b: "))
r = float(input("Ingrese c: "))
delta = q**2 - 4*p*r
if p == 0:
    print("La ecuacion no tiene solucion porque a debe ser diferente de 0")
else:
    if p != 0 and delta >= 0:
        print("La ecuacion tiene solucion")
        print("El discriminante es:", delta)
    else:
        print("La ecuacion no tiene solucion")
        print("El discriminante es:", delta)
