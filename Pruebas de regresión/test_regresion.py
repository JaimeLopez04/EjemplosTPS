# test_regresion.py
import unittest
from multiplicacion import multiplicacion

class TestRegresion(unittest.TestCase):
    def test_multiplicacion(self):
        resultado = multiplicacion(3, 5)
        self.assertEqual(resultado, 15)

if __name__ == '__main__':
    unittest.main()
