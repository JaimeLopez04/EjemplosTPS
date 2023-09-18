# test_integracion.py
import unittest
from calculadora import Calculadora
from registro import Registro

class TestIntegracion(unittest.TestCase):
    def test_calculadora_con_registro(self):
        calculadora = Calculadora()
        registro = Registro()
        
        resultado = calculadora.suma(3, 5)
        registro.guardar_resultado(resultado)

        # Verificamos si el resultado se guardó correctamente
        # En este ejemplo, asumimos que el método guardar_resultado siempre devuelve True
        self.assertTrue(registro.guardar_resultado(resultado))

if __name__ == '__main__':
    unittest.main()
