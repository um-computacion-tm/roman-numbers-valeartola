import unittest

from decimaltoroman import decimal_to_roman
class TestDecimalToRoman(unittest.TestCase):
    def test_uno(self):
        #pre condicion
        ### NO HAY ###
        #proceso
        resultado = decimal_to_roman(1)
        #verificacion
        self.assertEqual(resultado, "I")
    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, "X")
    def test_cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, "V")
    def test_dos(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, "II")
    def test_tres(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, "III")
    def test_cien(self):
        resultado = decimal_to_roman(100)
        self.assertEqual(resultado, "C")
    def test_ciento_uno(self):
        resultado = decimal_to_roman(101)
        self.assertEqual(resultado, "CI")
    def test_ciento_tres(self):
        resultado = decimal_to_roman(103)
        self.assertEqual(resultado, "CIII")
    def test_ciento_cinco(self):
        resultado = decimal_to_roman(105)
        self.assertEqual(resultado, "CV")
    def test_ciento_diez(self):
        resultado = decimal_to_roman(110)
        self.assertEqual(resultado, "CX")
    def test_docientos_tres(self):
        resultado = decimal_to_roman(203)
        self.assertEqual(resultado, "CCIII")
    
     
import unittest

from romantodecimal import roman_to_decimal

class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        resultado = roman_to_decimal("I")
        self.assertEqual(resultado, 1)
    def test_II(self):
        resultado = roman_to_decimal("II")
        self.assertEqual(resultado, 2)
    def test_III(self):
        resultado = roman_to_decimal("III")
        self.assertEqual(resultado, 3)
    def test_V(self):
        resultado = roman_to_decimal("V")
        self.assertEqual(resultado, 5)
    def test_X(self):
        resultado = roman_to_decimal("X")
        self.assertEqual(resultado, 10)
    def test_VI(self):
        resultado = roman_to_decimal("VI")
        self.assertEqual(resultado, 6)
    def test_VII(self):
        resultado = roman_to_decimal("VII")
        self.assertEqual(resultado, 7)
    def test_IV(self):
        resultado = roman_to_decimal("IV")
        self.assertEqual(resultado, 4)
    def test_IX(self):
        resultado = roman_to_decimal("IX")
        self.assertEqual(resultado, 9)

    

if __name__ == "__main__":
    unittest.main()