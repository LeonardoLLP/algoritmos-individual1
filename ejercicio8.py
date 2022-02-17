""" --- Algoritmo_1. Consulta ---
precio_iva(p: DECIMAL, iva: ENTERO): DECIMAL
    # p: precio
    # iva: impuesto (en porcentaje)

precondición
    p, iva >= 0

poscondición
    Resultado = p + (p * iva / 100)

fin precio_iva
"""

def precio_iva(p: float, iva: int):
    return p + (p * iva / 100)


""" --- Algoritmo_2 ---
interes_generado(c: DECIMAL, i: ENTERO, t: ENTERO)
    # c: capital inicial
    # i: interes (en porcentaje por mes)
    # t: tiempo (en meses)

variables
    cx: DECIMAL # Capital en momento







"""