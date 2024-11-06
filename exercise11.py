length = float(input("Ingrese la longitud de la varilla: "))

if length > 7.5 and length <= 9:
    diameter = float(input("Ingrese el diámetro de la varilla: "))
    if diameter >= 0.5 and diameter <= 1.3:
        density = 3.5
        mass = diameter * length / density
        if mass <= 5.8:
            print("La varilla es aceptada")
        else:
            print("La varilla es rechazada por exceder la masa máxima")
    else:
        print("La varilla es rechazada por exceder el diámetro permitido")
else:
    print("La varilla es rechazada por exceder la longitud permitida")