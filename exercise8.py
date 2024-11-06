number1 = float(input("Ingrese el primer número: "))
number2 = float(input("Ingrese el segundo número: "))
number3 = float(input("Ingrese el tercer número: "))

if number1 > number2 and number1 > number3:
    if number2 > number3:
        print("El número medio es: ", number2)
    else:
        print("El número medio es: ", number3)

elif number2 > number1 and number2 > number3:
    if number1 > number3:
        print("El número medio es: ", number1)
    else:
        print("El número medio es: ", number3)

else:
    if number1 > number2:
        print("El número medio es: ", number1)
    else:
        print("El número medio es: ", number2)
