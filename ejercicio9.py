""" --- Algoritmo 1. Consulta. ---
media(a: DECIMAL, b: DECIMAL, c: DECIMAL): DECIMAL
    # a, b, c --> números reales

poscondición
    Resultado = (a + b + c) / 3

fin media
"""

def media(a: float, b: float, c: float):
    return (a + b + c) / 3


""" --- Algoritmo 2. Consulta.
media_ponderada(a: DECIMAL, ap: DECIMAL, b: DECIMAL, bp: DECIMAL, c: DECIMAL, cp: DECIMAL): DECIMAL
    # a, b, c --> números reales
    # ap, bp, cp --> ponderaciones de dichos números

precondición
    ap, bp, cp >= 0

poscondición
    Resultado = (a*ap + b*bp + c*cp) / (ap+bp+cp)

fin media_ponderada
"""

def media_ponderada(a: float, ap: float, b: float, bp: float, c: float, cp: float):
    if ap >= 0 and bp >= 0 and cp >= 0:
        return (a*ap + b*bp + c*cp) / (ap+bp+cp)
    else:
        raise ValueError("Ponderations must be equal or above cero.")