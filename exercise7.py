name = str(input("Ingrese su nombre: "))
age = int(input("Ingrese su edad: "))
gender = str(input("Ingrese su sexo (Hombre, Mujer): "))
marital_status = str(input("Ingrese su estado civil (Casado, Soltero): "))

print("Nombre: ", name)

if gender == "Hombre" and marital_status == "Casado" and age > 40:
    print("Corresponde a un hombre casado mayor de 40 años.")

elif gender == "Mujer" and marital_status == "Soltera" and age < 50:
    print("Corresponde a una mujer soltera menor de 50 años.")

