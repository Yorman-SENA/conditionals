number = input("Ingrese un número: ")

if number.isnumeric():
    print("El número convertido a Kelvin es: " + str(float(number) + 273.15))
elif number.replace('.', '', 1).isdigit():
    number = float(number)
    if number > 10.5:
        print("El número ingresado es mayor a 10.5")
    else:
        print("El número ingresado es menor o igual a 10.5")
elif number.isalpha():
    name = input("Ingrese su nombre: ")
    print("Su nombre es: " + name)