# Ejercicio 3: Análisis de categorías
# Objetivo: Practicar listas, diccionarios y bucles

# Enunciado
# Tienes una lista de libros prestados con su categoría y días de préstamo:

prestamos = [
    {"titulo": "1984", "categoria": "Ficción", "dias": 15},
    {"titulo": "Sapiens", "categoria": "Ensayo", "dias": 22},
    {"titulo": "Watchmen", "categoria": "Cómic", "dias": 18},
    {"titulo": "El Quijote", "categoria": "Ficción", "dias": 30},
    {"titulo": "Breve historia", "categoria": "Ensayo", "dias": 25},
    {"titulo": "Batman", "categoria": "Cómic", "dias": 12}
]
# Escribe un programa que:

# Agrupe los préstamos por categoría
# Calcule el promedio de días por categoría
# Identifique la categoría más prestada
# Muestre libros con más de 20 días
# Pistas:
#   Crea un diccionario para agrupar por categoría
#   Usa un bucle para iterar sobre los préstamos
#   Para cada categoría, guarda una lista de días
#   Calcula promedios usando sum() y len()

# 1. Agrupar por categoría
categorias = {}

for prestamo in prestamos:
    categoria = prestamo["categoria"]
    dias = prestamo["dias"]
    
    if categoria not in categorias:
        categorias[categoria] = []
    
    categorias[categoria].append(dias)

# 2. Calcular promedio de días por categoría
print("--- Promedio por categoría ---")
promedios = {}

for categoria, lista_dias in categorias.items():
    promedio = sum(lista_dias) / len(lista_dias)
    promedios[categoria] = promedio
    print(f"{categoria}: {promedio:.2f} días")

# 3. Identificar la categoría más prestada
categoria_mas_prestada = max(categorias, key=lambda c: len(categorias[c]))

print("\nCategoría más prestada:", categoria_mas_prestada)

# 4. Mostrar libros con más de 20 días
print("\n--- Libros con más de 20 días ---")

for prestamo in prestamos:
    if prestamo["dias"] > 20:
        print(f"{prestamo['titulo']} ({prestamo['dias']} días)")