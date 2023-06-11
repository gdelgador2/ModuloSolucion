"""
Genera un menu de opciones que te permita realizar las siguientes tareas.
1. Realizar la suma de 2 números
2. Calcular el factorial de un número
3. Mostrar un triángulo de altura h
4. A partir de una fecha de tipo MM/DD/YYYY retornar en formato de YYYY-MM-DD
"""

# 1. Importacion de librerias
import math
import os
import sys

# import <nombre_script.py> as <alias>
import ingreso_datos as p

#  from <nombre_carpeta> import <nombre_script.py> as alias

from maths import calculos_basicos as math_basic
from maths import calculos_avanzados 

from funcionalidades import formato_fecha, triangulo

# 2. Definicion de constantes
MENSAJE_PRINCIPAL = 'Bienvenido al menú interactivo'
MENU_OPCIONES = """
¿Qué quieres hacer? Escribe una opción
    1) Calcular la suma de 2 números
    2) Calcular el factorial de un número
    3) Mostrar un triángulo de altura h
    4) A partir de una fecha de tipo MM/DD/YYYY retornar en formato de YYYY-MM-DD
    5) Salir
"""

# 3. Definicion de funciones y/o clases

def opcion_1():
    # sum 2 num
    n1 = p.validar_ingreso_numero_decimal("Introduce el primer número: ") 
    n2 = p.validar_ingreso_numero_decimal("Introduce el segundo número: ") 

    resultado_suma = math_basic.sumar_numeros(n1, n2)
    print(f"{n1} + {n2} = {resultado_suma}")
    pass

def opcion_2():
    n = p.ingreso_entero_positivo('Ingrese un número entero positivo: ')

    factorial = calculos_avanzados.calcular_factorial(n) 
    print(f'{n}! = {factorial}')
    pass

def opcion_3():
    # triangulo altura h
    h = p.ingreso_entero_positivo('Ingrese la altura del triangulo: ', num_base=2) 
    triangulo.imprimir_triangulo(h)
    pass

def opcion_4():
    fecha_inicial = input('Date: ').strip()
    formato_final = formato_fecha.brindar_formato_fecha(fecha_inicial)
    print(formato_final)
    pass

def main():
    print(MENSAJE_PRINCIPAL)
    while True:
        opcion = input(MENU_OPCIONES)

        if opcion == '1':
            # suma dos numeros
            opcion_1()
        elif opcion == '2':
            #  factorial
            opcion_2()
        elif opcion == '3':
            # mostrar triangulo altura h
            opcion_3()
        elif opcion == '4':
            # dar formato a fecha
            opcion_4()
        elif opcion =='5':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")
    pass

# 4. mi programa

# Llamo a funcion principal
if __name__ == '__main__':
    main()