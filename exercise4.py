categories = {
    'A': 'Salario: 1000000',
    'B': 'Salario: 800000'
}

category1 = input("Ingrese la categoria (A,B) del empleado 1: ")
category2 = input("Ingrese la categoria (A,B) del empleado 2: ")
category3 = input("Ingrese la categoria (A,B) del empleado 3: ")
category4 = input("Ingrese la categoria (A,B) del empleado 4: ")
category5 = input("Ingrese la categoria (A,B) del empleado 5: ")

if categories.get(category1):
    print("El empleado 1 tiene la categoría " + category1 + " y su salario es: " + categories[category1])
else:
    print("Categoría no válida")

if categories.get(category2):
    print("El empleado 2 tiene la categoría " + category2 + " y su salario es: " + categories[category2])
else:
    print("Categoría no válida")

if categories.get(category3):
    print("El empleado 3 tiene la categoría " + category3 + " y su salario es: " + categories[category3])
else:
    print("Categoría no válida")

if categories.get(category4):
    print("El empleado 4 tiene la categoría " + category4 + " y su salario es: " + categories[category4])
else:
    print("Categoría no válida")

if categories.get(category5):
    print("El empleado 5 tiene la categoría " + category5 + " y su salario es: " + categories[category5])
else:
    print("Categoría no válida")
