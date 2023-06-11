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
