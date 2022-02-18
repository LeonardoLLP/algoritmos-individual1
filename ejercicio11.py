""" --- Algoritmo consulta ---
h_extra(h: ENTERO, sm: ENTERO): DECIMAL
    # h: Horas de la semana
    # sm: Salario mensual
    # Este algoritmo devuelve el importe de las horas extra a pagar en una semana

precondición
    h >= 8
    s > 0

variables
    sh: DECIMAL <-- (s * 12) / (52 * 35)  # Salario por hora

realización
    si h <= 35
        nada
    si no
        si h <= 43
            Resultado <-- sh * (h - 35)
        si no  # h > 43
            Resultado <--

poscondición


"""