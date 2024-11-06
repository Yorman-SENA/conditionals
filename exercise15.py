import math

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

if a == 0:
    print("El valor de a no puede ser 0")
else:
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print("La ecuación no tiene soluciones reales")
    elif discriminant == 0:
        x = -b / (2 * a)
        print("La ecuación tiene una solución: ", x)
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Las soluciones de la ecuación son: ", x1, " y ", x2)
