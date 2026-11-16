entrada = float(input("digite el primero numero: "))
sobrante = entrada % 2
if sobrante == 0:
    print("el numero", entrada, "es par")
else:
    print("el numero", entrada, "es impar")
