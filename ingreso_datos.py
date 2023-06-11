"""Contiene funciones que permite validar el ingreso de los datos"""


def validar_ingreso_numero_entero(msg:str= 'Ingrese un número entero: ')-> int:
    """Realiza las validaciones para el ingreso de un número"""
    try:
        n = int(input(msg))
        return n
    except:
        print('No es un número, vuelva a intentar....')
        return validar_ingreso_numero_entero(msg)
    
def validar_ingreso_numero_decimal(msg:str= 'Ingrese un número decimal: ')->float:
    """Realiza las validaciones para el ingreso de un número"""
    try:
        n = float(input(msg))
        return n
    except:
        print('No es un número, vuelva a intentar....')
        return validar_ingreso_numero_decimal(msg)
    

def ingreso_entero_positivo(msg:str = 'Ingrese un numero entero positivo: ', num_base:int=1)->int:
    """Valida el ingreso de un entero positivo"""

    x = validar_ingreso_numero_entero(msg=msg)
    if x>=num_base:
        return x
    
    print(f'El número ingresado debe ser mayor o igual a {num_base}')
    return ingreso_entero_positivo(msg,num_base)


if __name__ == '__main__':

    x = ingreso_entero_positivo()
    print(x, type(x))


