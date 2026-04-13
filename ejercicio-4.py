# Ejercicio 4: Procesador de datos
# Objetivo: Integrar todo (funciones, estructuras, validación)

# Enunciado
# Crea un sistema que procese datos de ventas con las siguientes funciones:

def limpiar_datos(ventas):
    """Elimina valores negativos o None"""
    ventas_limpias = []

    for venta in ventas:
        if venta is not None and venta > 0:
            ventas_limpias.append(venta)

    return ventas_limpias
    pass

def calcular_estadisticas(ventas):
    """Devuelve dict con total, promedio, max, min"""
    if len(ventas) == 0:
        return {
            "total": 0,
            "promedio": 0,
            "max": None,
            "min": None
        }

    return {
        "total": sum(ventas),
        "promedio": sum(ventas) / len(ventas),
        "max": max(ventas),
        "min": min(ventas)
    }
    pass

def clasificar_ventas(ventas, umbral_bajo, umbral_alto):
    """Devuelve dict con ventas bajas, medias, altas"""
    clasificacion = {
        "bajas": [],
        "medias": [],
        "altas": []
    }

    for venta in ventas:
        if venta < umbral_bajo:
            clasificacion["bajas"].append(venta)
        elif venta >= umbral_alto:
            clasificacion["altas"].append(venta)
        else:
            clasificacion["medias"].append(venta)

    return clasificacion
    pass

def generar_reporte(ventas):
    """Usa las funciones anteriores y muestra reporte completo"""
    ventas_limpias = limpiar_datos(ventas)
    estadisticas = calcular_estadisticas(ventas_limpias)
    clasificacion = clasificar_ventas(ventas_limpias, 2000, 4000)

    total_original = len(ventas)
    total_validas = len(ventas_limpias)
    total_invalidas = total_original - total_validas

    bajas = len(clasificacion["bajas"])
    medias = len(clasificacion["medias"])
    altas = len(clasificacion["altas"])

    if total_validas > 0:
        porcentaje_bajas = (bajas / total_validas) * 100
        porcentaje_medias = (medias / total_validas) * 100
        porcentaje_altas = (altas / total_validas) * 100
    else:
        porcentaje_bajas = porcentaje_medias = porcentaje_altas = 0

    print("=== REPORTE DE VENTAS ===\n")
    print(f"Datos procesados: {total_validas} ventas válidas ({total_invalidas} inválidas eliminadas)\n")

    print("Estadísticas:")
    print(f"  Total: {estadisticas['total']}")
    print(f"  Promedio: {estadisticas['promedio']:.2f}")
    print(f"  Máximo: {estadisticas['max']}")
    print(f"  Mínimo: {estadisticas['min']}\n")

    print("Clasificación:")
    print(f"  Ventas bajas (< 2000): {bajas} ({porcentaje_bajas:.1f}%)")
    print(f"  Ventas medias: {medias} ({porcentaje_medias:.1f}%)")
    print(f"  Ventas altas (>= 4000): {altas} ({porcentaje_altas:.1f}%)")
    pass

# Datos de prueba (con valores inválidos):

ventas_brutas = [1500, -200, 2500, None, 3000, 0, 4500, -100, 2800, 5000]

# Requerimientos
# limpiar_datos: Filtrar valores válidos (> 0 y no None)
# calcular_estadisticas: Total, promedio, máximo, mínimo
# clasificar_ventas:
# Baja: < umbral_bajo
# Media: entre umbrales
# Alta: >= umbral_alto
# generar_reporte: Llamar todas las funciones y mostrar resultados formateados

generar_reporte(ventas_brutas)