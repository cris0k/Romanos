valores_romanos = {
    1 : 'I',
    5 : 'V',
    10 : 'X',
    50 : 'L',
    100 : 'C',
    500 : 'D',
    1000 : 'M'
}
valores_romanosT = [
    (1000 , 'M')
    (900, 'CM')
    (500 , 'D')
    (400, 'CD'),
    (100 , 'C'),
    (90, 'XC')
    (50 , 'L'),
    (40, 'XL')
    (10 , 'X')
    (9, 'IX'),
    (5 , 'V'),
    (4, 'IV')
    (1 , 'I'),
]
def arabigo_a_romano(n):
    romano = ''
    resto = None

    while resto != 0:
        for valor, simbolo in valores_romanosT:
            if n >= valor:
                break

        cociente = n // valor
        resto = n % valor
        romano += cociente * simbolo
        n = resto

    return romano  