# test_humo.py
import unittest
from verificar_archivo import verificar_archivo

class TestHumo(unittest.TestCase):
    def test_verificar_archivo_existente(self):
        resultado = verificar_archivo("archivo_existente.txt")
        self.assertTrue(resultado)

    def test_verificar_archivo_inexistente(self):
        resultado = verificar_archivo("archivo_inexistente.txt")
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()
