value1 = float(input("Ingrese la primera calificación: "))
value2 = float(input("Ingrese la segunda calificación: "))
value3 = float(input("Ingrese la tercera calificación: "))

if value1 > value2 and value1 > value3:
    if value2 > value3:
        print("La calificación final es: ", (value1 + value2) / 2)
    else:
        print("La calificación final es: ", (value1 + value3) / 2)
elif value2 > value1 and value2 > value3:
    print("La calificación más alta es: ", value2)
    if value1 > value3:
        print("La calificación final es: ", (value2 + value1) / 2)
    else:
        print("La calificación final es: ", (value2 + value3) / 2)
else:
    if value1 > value2:
        print("La calificación final es: ", (value3 + value1) / 2)
    else:
        print("La calificación final es: ", (value3 + value2) / 2)

