import unittest
from suma import suma

class TestSuma(unittest.TestCase):
    def test_suma(self):
        resultado = suma(3, 5)
        self.assertEqual(resultado, 8)

if __name__ == '__main__':
    unittest.main()