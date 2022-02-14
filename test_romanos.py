import unittest
from romanos import RomanError, arabigo_a_romano, romano_a_arabigo

class RomanosFuncionesTest(unittest.TestCase):
    def test_arabigo_a_romano_sin_restas(self):
        self.assertEqual(arabigo_a_romano(36), 'XXXVI')

    def test_atabigo_a_romano_sin_restas(self):
        self.assertEqual(arabigo_a_romano(464), 'CDLXIV')

    def test_arabigo_a_romano_solo_admite_enteros(self):
        with self.assertRaises(TypeError):
            arabigo_a_romano('lolailo') #aqui como se espera un error,va a dar la prueba bien
#si en vez de 'lolailo' ponemor un numero, dara error porque el test se espera un error.
    def test_arabigo_a_romano_solo_admite_enteros_positivos(self):
        with self.assertRaises(ValueError):
            arabigo_a_romano(0)

class RomanosFuncionesAromanoTest(unittest.TestCase):
    def test_romano_a_arabigo_tres_repeticiones_OK(self):
        self.assertEqual(romano_a_arabigo('III'), 3)

    def test_romano_a_arabigo_cuatro_repeticiones_ERROR(self):
        with self.assertRaises(RomanError):
            romano_a_arabigo('IIII')

    def test_romano_a_arabigo_dos_repeticiones_de_VLD_error(self):
        with self.assertRaises(RomanError):
            romano_a_arabigo('VV')
        with self.assertRaises(RomanError):
            romano_a_arabigo('LL')
        with self.assertRaises(RomanError):
            romano_a_arabigo('DD')

    def test_romano_a_arabigo_VLD_no_resta(self):
        with self.assertRaises(RomanError):
            romano_a_arabigo('VX')
        with self.assertRaises(RomanError):
            romano_a_arabigo('LC')
        with self.assertRaises(RomanError):
            romano_a_arabigo('DM')

    def test_romano_a_arabigo_tras_repeticion_no_se_resta(self):
        with self.assertRaises(RomanError):
            romano_a_arabigo('XXL')
            
            self.assertEqual(romano_a_arabigo('XXIII', 23))
        
    def test_romano_a_arabigo_restas_prohibidas_si_separacion_alta(self):
        with self.assertRaises(RomanError):
            romano_a_arabigo('XM')

    def test_romano_a_arabigo_simbolos_incorrectos(self):
        with self.assertRaises(RomanError):
            romano_a_arabigo('IK')
        with self.assertRaises(RomanError):
            romano_a_arabigo('KI')
        with self.assertRaises(RomanError):
            romano_a_arabigo('K')

"""
from romanos import arabigo_a_romano, romano_a_arabigo

print(romano_a_arabigo('M'))
"""