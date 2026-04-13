# Ejercicio 2: Clasificador de préstamos
# Objetivo: Practicar funciones, condicionales y listas

# Enunciado
# Crea una función que clasifique préstamos según días transcurridos:

# 0-21 días: "A tiempo"
# 22-30 días: "Retraso leve" (penalización: 0.50€/día extra)
# Más de 30 días: "Retraso grave" (penalización: 1.00€/día extra)
# Luego procesa una lista de préstamos y muestra estadísticas.


def clasificar_prestamo(dias):
    if dias <= 21:
        return "A tiempo", 0
    elif dias <= 30:
        penalizacion = (dias - 21) * 0.50
        return "Retraso leve", penalizacion
    else:
        penalizacion = (dias - 30) * 1.00
        return "Retraso grave", penalizacion 
    

# Datos de prueba
prestamos_dias = [15, 22, 18, 35, 25, 12, 40, 19, 28, 33]

# Variables para estadísticas
conteo = {
    "A tiempo": 0,
    "Retraso leve": 0,
    "Retraso grave": 0
}

total_penalizaciones = 0

# Procesar préstamos
for dias in prestamos_dias:
    estado, penalizacion = clasificar_prestamo(dias)
    
    conteo[estado] += 1
    total_penalizaciones += penalizacion
    
    print(f"Días: {dias} → {estado} | Penalización: {penalizacion:.2f}€")

# Mostrar estadísticas
print("\n--- Estadísticas ---")
print(f"A tiempo: {conteo['A tiempo']}")
print(f"Retraso leve: {conteo['Retraso leve']}")
print(f"Retraso grave: {conteo['Retraso grave']}")
print(f"Total penalizaciones: {total_penalizaciones:.2f}€")