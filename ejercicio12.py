""" --- Clase 1. Comando. ---
tipo CUENTA

variables
    c: ENTERO  # Capital en la cuenta

algoritmo retirar (comando)

    Entrada:
        r: ENTERO  # Dinero a retirar

    Salida:
        c: ENTERO  # Dinero restante en la cuenta

    precondición
        c > 0

    poscondición
        c = antiguo(c) - r

fin CUENTA
"""