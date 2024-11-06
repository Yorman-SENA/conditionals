sales = 50

totalSales = 0

salesUnder2000 = 0
salesOver2000 = 0

for i in range(sales):

    price = float(input("Ingrese el precio del artículo: "))

    if price < 2000:
        commission = price * 0.03
        salesUnder2000 += 1
    else:
        commission = price * 0.05
        salesOver2000 += 1

    totalSales += commission

print("La comisión total del vendedor es: ", totalSales)
print("El número de ventas menores a 2000 es: ", salesUnder2000)
print("El número de ventas mayores o iguales a 2000 es: ", salesOver2000)
