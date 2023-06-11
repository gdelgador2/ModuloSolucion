def calcular_factorial(numero:int):
    """Calcula el factorial de un número"""
    if numero==1:
        return 1
    else:
        return numero * calcular_factorial(numero-1)
    