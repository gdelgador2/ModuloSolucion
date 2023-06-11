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

MONTHS = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

# Menu
print(MENSAJE_PRINCIPAL)
while True:
    opcion = input(MENU_OPCIONES)

    if opcion == '1':
        # sum 2 num
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print(f"El resultado de la suma es: {n1+n2}")
    elif opcion == '2':
        #  factorial
        n = int(input('Ingrese un número entero positivo: '))
        fact = 1
        for i in range(1,n+1):
            fact = fact*i
            pass
        print(f'{n}! = {fact}')
    elif opcion == '3':
        # triangulo altura h
        h = int(input('Ingrese un número entero positivo: '))

        for i in range(1,h+1):
            print('*'*i)
        pass
    elif opcion == '4':

        while True:
            cadena = input('Date: ').strip()
            
            if '/' in cadena:
                # fechas tipo: mm/dd/yyyy
                m,d,y = cadena.split('/')
            else:
                # fechas tipo 'Septiembre 8, 1636'
                m,d,y = cadena.replace(',','').split(' ')
                m = m.title()
                # buscamos mes en lista meses
                if m in MONTHS:
                    m = MONTHS.index(m) + 1
                    
            try:
                # retornamos fecha en formato correcto 'yyyy-mm-dd'
                y = int(y)
                m= int(m)
                d=int(d)
                print(f'{y}-{m:02}-{d:02}')
                break
            except:
                pass
        pass
    elif opcion =='5':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")