""" --- Algoritmo consulta ---
h_extra(h: ENTERO, sm: ENTERO): DECIMAL
    # h: Horas de la semana
    # sm: Salario mensual
    # Este algoritmo devuelve SOLAMENTE el importe de las horas extra a pagar en una semana

precondición
    h >= 8
    sm > 0

variables
    sh: DECIMAL <-- (sm * 12) / (52 * 35)  # Salario por hora

realización
    si h <= 35
        Resultado <-- 0
    si no
        si h <= 43
            Resultado <-- (sh * 1.25) * (h - 35)
        si no  # h > 43
            Resultado <-- (sh * 1.50) * (h - 43) + (sh * 1.25) * 8

poscondición
    si h <= 35
        Resultado = 0
    si no
        Resultado > 0

fin h_extra
"""

def h_extra(h: int, sm: int):
    if h < 8:
        raise ValueError("Working hours must be equal or above 8.")
    elif sm <= 0:
        raise ValueError("Salary must be greater than cero.")


    sh = (sm * 12) / (52 * 35)

    if h <= 35:
        return 0
    else:
        if h <= 43:
            return (sh * 1.25) * (h - 35)
        else:
            return (sh * 1.50) * (h - 43) + (sh * 1.25) * 8

