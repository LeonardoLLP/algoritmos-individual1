""" --- Clase 1.1 - Comando ---
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

class CUENTA:
    def __init__(self, c: int):
        self.c = c

    def retirar(self, r):
        if self.c > 0:
            self.c -= r
        else:
            raise ValueError("Capital must be greater than cero.")


""" --- Clase 1.2 - Comando ---
tipo CUENTA_AVANZADA

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

class CUENTA_AVANZADA:
    def __init__(self, c: int):
        self.c = c

    def retirar(self, r):
        self.c -= r