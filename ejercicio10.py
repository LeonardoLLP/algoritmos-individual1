""" --- Algoritmo. Consulta. ---
def area_tri(l: DECIMAL, h: DECIMAL): DECIMAL

precondición
    l, a > 0

poscondición
    Resultado = l * a / 2

fin area_tri
"""

def area_tri(l: float, h: float):
    return l * h / 2

""" ¿Se puede utilizar este algoritmo para un triángulo rectángulo si se dan las medidas de sus dos lados perpendiculares?
La respuesta es si. Siendo ambos lados perpendiculares, uno puede interpretarse como la altura del otro.
"""