number1 = float(input("Ingrese el primer número: "))
number2 = float(input("Ingrese el segundo número: "))
number3 = float(input("Ingrese el tercer número: "))

if number1 > number2 and number1 > number3:
    print("El número mayor es: ", number1)
elif number2 > number1 and number2 > number3:
    print("El número mayor es: ", number2)
else:
    print("El número mayor es: ", number3)

if number1 < number2 and number1 < number3:
    print("El número menor es: ", number1)
elif number2 < number1 and number2 < number3:
    print("El número menor es: ", number2)
else:
    print("El número menor es: ", number3)

if number1 == number2:
        print("El primer y el segundo número son iguales")
elif number1 == number3:
    print("El primer y el tercer número son iguales")
elif number2 == number3:
    print("El segundo y el tercer número son iguales")

if number1 != number2 and number2 != number3 and number1 != number3:
    print("Los tres números son diferentes.")
