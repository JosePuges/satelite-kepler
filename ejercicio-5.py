""" Ejercicio 5: Mini proyecto integrador
Objetivo: Crear un análisis completo desde cero

Enunciado
Crea un programa que simule el análisis de una biblioteca durante un mes.

Datos a generar aleatoriamente (o puedes usar datos fijos):

100 préstamos
Categorías: Ficción, Ensayo, Cómic, Poesía
Días de préstamo: entre 5 y 45 días
Análisis a realizar:

Por categoría:

Cuántos préstamos
Promedio de días
Porcentaje del total
Por estado:

A tiempo (≤ 21 días)
Retraso leve (22-30 días)
Retraso grave (> 30 días)
Penalizaciones:

Total recaudado en penalizaciones
Promedio por préstamo con retraso
Top 5:

Préstamos más largos
Estructura sugerida """

import random

def generar_datos(n=100):
    """Genera n préstamos aleatorios"""
    categorias = ["Ficción", "Ensayo", "Cómic", "Poesía"]
    prestamos = []

    for i in range(1, n + 1):
        prestamo = {
            "id": i,
            "categoria": random.choice(categorias),
            "dias": random.randint(5, 45)
        }
        prestamos.append(prestamo)

    return prestamos


def clasificar_estado(dias):
    """Clasifica un préstamo según los días transcurridos"""
    if dias <= 21:
        return "A tiempo"
    elif dias <= 30:
        return "Retraso leve"
    else:
        return "Retraso grave"


def calcular_penalizacion(dias):
    """Calcula la penalización de un préstamo"""
    if dias <= 21:
        return 0
    elif dias <= 30:
        return (dias - 21) * 0.50
    else:
        return (30 - 21) * 0.50 + (dias - 30) * 1.00


def analizar_por_categoria(prestamos):
    """Análisis por categoría"""
    resultado = {}
    total_prestamos = len(prestamos)

    for prestamo in prestamos:
        categoria = prestamo["categoria"]
        dias = prestamo["dias"]

        if categoria not in resultado:
            resultado[categoria] = {
                "cantidad": 0,
                "dias_totales": 0
            }

        resultado[categoria]["cantidad"] += 1
        resultado[categoria]["dias_totales"] += dias

    for categoria in resultado:
        cantidad = resultado[categoria]["cantidad"]
        dias_totales = resultado[categoria]["dias_totales"]
        promedio = dias_totales / cantidad
        porcentaje = (cantidad / total_prestamos) * 100

        resultado[categoria]["promedio_dias"] = promedio
        resultado[categoria]["porcentaje"] = porcentaje

    return resultado


def analizar_por_estado(prestamos):
    """Análisis por estado"""
    estados = {
        "A tiempo": 0,
        "Retraso leve": 0,
        "Retraso grave": 0
    }

    for prestamo in prestamos:
        estado = clasificar_estado(prestamo["dias"])
        estados[estado] += 1

    return estados


def calcular_penalizaciones(prestamos):
    """Calcula penalizaciones"""
    total_penalizaciones = 0
    penalizaciones_con_retraso = []

    for prestamo in prestamos:
        penalizacion = calcular_penalizacion(prestamo["dias"])
        total_penalizaciones += penalizacion

        if penalizacion > 0:
            penalizaciones_con_retraso.append(penalizacion)

    if len(penalizaciones_con_retraso) > 0:
        promedio_retraso = total_penalizaciones / len(penalizaciones_con_retraso)
    else:
        promedio_retraso = 0

    return {
        "total_recaudado": total_penalizaciones,
        "promedio_por_retraso": promedio_retraso,
        "cantidad_con_retraso": len(penalizaciones_con_retraso)
    }


def top_5_prestamos_mas_largos(prestamos):
    """Devuelve los 5 préstamos con más días"""
    return sorted(prestamos, key=lambda x: x["dias"], reverse=True)[:5]


def main():
    """Función principal que coordina todo"""
    datos = generar_datos(100)

    print("=== ANÁLISIS DE BIBLIOTECA ===\n")

    # Análisis por categoría
    analisis_categoria = analizar_por_categoria(datos)
    print("Por categoría:")
    for categoria, info in analisis_categoria.items():
        print(f"  {categoria}:")
        print(f"    Préstamos: {info['cantidad']}")
        print(f"    Promedio de días: {info['promedio_dias']:.2f}")
        print(f"    Porcentaje del total: {info['porcentaje']:.1f}%")
    print()

    # Análisis por estado
    analisis_estado = analizar_por_estado(datos)
    print("Por estado:")
    for estado, cantidad in analisis_estado.items():
        porcentaje = (cantidad / len(datos)) * 100
        print(f"  {estado}: {cantidad} ({porcentaje:.1f}%)")
    print()

    # Penalizaciones
    penalizaciones = calcular_penalizaciones(datos)
    print("Penalizaciones:")
    print(f"  Total recaudado: {penalizaciones['total_recaudado']:.2f}€")
    print(f"  Promedio por préstamo con retraso: {penalizaciones['promedio_por_retraso']:.2f}€")
    print(f"  Préstamos con retraso: {penalizaciones['cantidad_con_retraso']}")
    print()

    # Top 5 préstamos más largos
    top5 = top_5_prestamos_mas_largos(datos)
    print("Top 5 préstamos más largos:")
    for prestamo in top5:
        estado = clasificar_estado(prestamo["dias"])
        penalizacion = calcular_penalizacion(prestamo["dias"])
        print(
            f"  ID {prestamo['id']} | "
            f"{prestamo['categoria']} | "
            f"{prestamo['dias']} días | "
            f"{estado} | "
            f"Penalización: {penalizacion:.2f}€"
        )


if __name__ == "__main__":
    main()