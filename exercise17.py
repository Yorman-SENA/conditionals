number1 = float(input("Ingrese el primer número: "))
number2 = float(input("Ingrese el segundo número: "))
number3 = float(input("Ingrese el tercer número: "))

if number1 % number2 == 0:
    print("El primer número es divisible por el segundo número.")
elif number1 % number3 == 0:
    print("El primer número es divisible por el tercer número.")
elif number2 % number1 == 0:
    print("El segundo número es divisible por el primer número.")
elif number2 % number3 == 0:
    print("El segundo número es divisible por el tercer número.")
elif number3 % number1 == 0:
    print("El tercer número es divisible por el primer número.")
elif number3 % number2 == 0:
    print("El tercer número es divisible por el segundo número.")
else:
    print("Ningún número es divisible por otro número.")


