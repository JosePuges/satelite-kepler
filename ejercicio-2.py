# Ejercicio 2: Clasificador de préstamos
# Objetivo: Practicar funciones, condicionales y listas

# Enunciado
# Crea una función que clasifique préstamos según días transcurridos:

# 0-21 días: "A tiempo"
# 22-30 días: "Retraso leve" (penalización: 0.50€/día extra)
# Más de 30 días: "Retraso grave" (penalización: 1.00€/día extra)
# Luego procesa una lista de préstamos y muestra estadísticas.


def clasificar_prestamo(dias):
    # Tu código aquí
    estado = ""
    penalizacion = 0.0

    if dias < 21:
        estado = " A "
    pass

# Datos de prueba
prestamos_dias = [15, 22, 18, 35, 25, 12, 40, 19, 28, 33]

# Procesar y mostrar estadísticas