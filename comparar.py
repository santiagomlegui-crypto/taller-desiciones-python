m = float(input("Digite el primer numero: "))
n = float(input("Digite el segundo numero: "))
if m >= n:
    if m == n:
        print(m, "es igual a", n)
    else:
        print(m, "es mayor que", n)
else:
    print(n, "es mayor que", m)
