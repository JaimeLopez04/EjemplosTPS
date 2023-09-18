#Se prueban los componentes de la calculadora
import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora()  # Crear una instancia de la calculadora antes de cada prueba

    def test_suma(self):
        resultado = self.calculadora.suma(3, 5)
        self.assertEqual(resultado, 8)

    def test_resta(self):
        resultado = self.calculadora.resta(10, 4)
        self.assertEqual(resultado, 6)

if __name__ == '__main__':
    unittest.main()
