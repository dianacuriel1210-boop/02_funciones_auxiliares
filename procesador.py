"""
Nombre: Valdez Curiel Diana
Matrícula: 2403230163
Asignatura: Ciencia de Datos
Fecha: 21/09/2026
"""

import re  # Analizar el texto de la función


def extraer_parametros(expresion):
    # Quitar espacios
    expresion = expresion.replace(" ", "").lower()

    # Buscar la función
    patron = r"^([+-]?\d*\.?\d*)x([+-]?\d*\.?\d*)$"
    resultado = re.match(patron, expresion)

    if not resultado:
        raise ValueError("Función no válida.")

    parte_m = resultado.group(1)
    parte_b = resultado.group(2)

    # Obtener m
    if parte_m in ("", "+"):
        m = 1.0
    elif parte_m == "-":
        m = -1.0
    else:
        m = float(parte_m)

    # Obtener b
    if parte_b == "":
        b = 0.0
    else:
        b = float(parte_b)

    return m, b