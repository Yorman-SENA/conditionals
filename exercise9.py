a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

if a > b and a > c:
    if b > c:
        print("Los números ordenados de mayor a menor son: ", a, b, c)
    else:
        print("Los números ordenados de mayor a menor son: ", a, c, b)

elif b > a and b > c:
    if a > c:
        print("Los números ordenados de mayor a menor son: ", b, a, c)
    else:
        print("Los números ordenados de mayor a menor son: ", b, c, a)

else:
    if a > b:
        print("Los números ordenados de mayor a menor son: ", c, a, b)
    else:
        print("Los números ordenados de mayor a menor son: ", c, b, a)