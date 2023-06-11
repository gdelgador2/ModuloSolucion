"""
Genera un menu de opciones que te permita realizar las siguientes tareas.
1. Realizar la suma de 2 números
2. Calcular el factorial de un número
3. Mostrar un triángulo de altura h
4. A partir de una fecha de tipo MM/DD/YYYY retornar en formato de YYYY-MM-DD
"""

MENSAJE_PRINCIPAL = 'Bienvenido al menú interactivo'
MENU_OPCIONES = """
¿Qué quieres hacer? Escribe una opción
    1) Calcular la suma de 2 números
    2) Calcular el factorial de un número
    3) Mostrar un triángulo de altura h
    4) A partir de una fecha de tipo MM/DD/YYYY retornar en formato de YYYY-MM-DD
    5) Salir
"""

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

def sumar_numeros(x: float,y: float)->float:
    """Retorna la suma de x + y"""
    return x + y

def calcular_factorial(numero:int):
    """Calcula el factorial de un número"""
    if numero==1:
        return 1
    else:
        return numero * calcular_factorial(numero-1)
    
def imprimir_triangulo(h:int):
    """Imprime un triangulo de altura h"""
    for i in range(1,h+1):
        print('*'*i)

def brindar_formato_fecha(fecha_inicial: str)->str:
    """Solicita el ingreso de una fecha y brinda el formato correspondiente"""

    MONTHS = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    
    if '/' in fecha_inicial:
        # fechas tipo: mm/dd/yyyy
        m,d,y = fecha_inicial.split('/')
    else:
        # fechas tipo 'Septiembre 8, 1636'
        m,d,y = fecha_inicial.replace(',','').split(' ')
        m = m.title()
        # buscamos mes en lista meses
        if m in MONTHS:
            m = MONTHS.index(m) + 1

    try:
        # retornamos fecha en formato correcto 'yyyy-mm-dd'
        y = int(y)
        m= int(m)
        d=int(d)

        return f'{y}-{m:02}-{d:02}'
    except:
        print('formato incorrecto')
        return brindar_formato_fecha(input('Date: ').strip())
    pass

# Menu
def main():
    print(MENSAJE_PRINCIPAL)
    while True:
        opcion = input(MENU_OPCIONES)

        if opcion == '1':
            # sum 2 num
            n1 = validar_ingreso_numero_decimal("Introduce el primer número: ") 
            n2 = validar_ingreso_numero_decimal("Introduce el segundo número: ") 

            resultado_suma = sumar_numeros(n1, n2)
            print(f"{n1} + {n2} = {resultado_suma}")
        elif opcion == '2':
            #  factorial
            n = validar_ingreso_numero_entero('Ingrese un número entero positivo: ')

            factorial = calcular_factorial(n) 
            print(f'{n}! = {factorial}')
        elif opcion == '3':
            # triangulo altura h
            h = validar_ingreso_numero_entero('Ingrese la altura del triangulo: ') 
            imprimir_triangulo(h)

        elif opcion == '4':
            fecha_inicial = input('Date: ').strip()
            formato_fecha = brindar_formato_fecha(fecha_inicial)
            print(formato_fecha)
        elif opcion =='5':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")
    pass

# Llamo a funcion principal
main()