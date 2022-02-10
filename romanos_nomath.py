unidades = ["millares", "centenas", "decenas", "unidades"]

romanos = {
    'millares': {10: '', 5: '', 1: 'M'},
    'centenas': {10: 'M', 5: 'D', 1: 'C'},
    'decenas': {10: 'C', 5: 'L', 1: 'X'},
    'unidades': {10: 'X', 5:'V', 1: 'I'}
}

def descomponer (n):
    if not isinstance(n, int):
        raise TypeError(f"{n} debe ser de tipo int")

    cadena = f"{n:04d}"
    return {unidades[i]: int(cadena[i]) for i in range(len(cadena))}

def a_romano(valor, tipo):
    if valor == 9:
        return romanos[tipo][1]+romanos[tipo][10]
    elif valor >= 5:
        return romanos[tipo][5] + romanos[tipo][1]* (valor-5)
    elif valor == 4:
        return romanos[tipo][1]+romanos[tipo][5]
    else:
        return romanos[tipo][1]* valor    

def arabigo_a_romano(n):
    valores = descomponer(n)
    resultado = ''
    for tipo in unidades:
        resultado += a_romano(valores[tipo], tipo)

    return resultado