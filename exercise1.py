number = float(input("Ingrese un número: "))

if number < 0:
    print("El número ingresado es negativo: ", number)
    print("El número positivo correspondiente es: ", number * -1)
else:
    print("El número ingresado es positivo: ", number)
    print("El número negativo correspondiente es: ", number * -1)