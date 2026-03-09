# Ejercicio 1: Análisis básico de ventas
# Objetivo: Practicar variables, operadores y condicionales

# Datos
enero = 4500
febrero = 5200
marzo = 4800
# ... completa los demás meses
abril = 6200
mayo = 5900
junio = 4900
julio = 3900
agosto = 7900
septiembre = 5900
octubre = 3800
noviembre = 4600
diciembre = 7000

# Tu código aquí

total = enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre + octubre + noviembre + diciembre
promedio = total // 12

mayor_venta = enero
mes_nombre = "enero"


if febrero > mayor_venta:
    mayor_venta = febrero
    mes_nombre = "Febrero"
if marzo > mayor_venta:
    mayor_venta = marzo
    mes_nombre = "Marzo"
if abril > mayor_venta:
    mayor_venta = abril
    mes_nombre = "Abril"
if mayo >  mayor_venta:
    mayor_venta = mayo
    mes_nombre = "mayo"
if junio >  mayor_venta:
    mayor_venta = junio
    mes_nombre = "junio"
if julio >  mayor_venta:
    mayor_venta = julio
    mes_nombre = "julio"
if agosto >  mayor_venta:
    mayor_venta = agosto
    mes_nombre = "agosto"
if septiembre >  mayor_venta:
    mayor_venta = septiembre
    mes_nombre = "septiembre"
if octubre >  mayor_venta:
    mayor_venta = octubre
    mes_nombre = "octubre"
if noviembre>  mayor_venta:
    mayor_venta = noviembre
    mes_nombre = "noviembre"
if diciembre >  mayor_venta:
    mayor_venta = diciembre
    mes_nombre = "diciembre"


print("Total: ", total)
print("Promedio: ", promedio)
print("Mes con más ventas:", mes_nombre, "con", mayor_venta)