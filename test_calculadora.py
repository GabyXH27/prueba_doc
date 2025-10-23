import unittest
import time
from calculadora import calculadora_basica

class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada prueba"""
        self.calc = calculadora_basica()
    
    # PRUEBAS UNITARIAS
    
    def test_suma_positiva(self):
        """Prueba unitaria: suma de números positivos"""
        resultado = self.calc.sumar(5, 3)
        self.assertEqual(resultado, 8)
    
    def test_suma_negativa(self):
        """Prueba unitaria: suma con números negativos"""
        resultado = self.calc.sumar(-2, -3)
        self.assertEqual(resultado, -5)
    
    def test_resta(self):
        """Prueba unitaria: resta básica"""
        resultado = self.calc.restar(10, 4)
        self.assertEqual(resultado, 6)
    
    def test_multiplicacion(self):
        """Prueba unitaria: multiplicación"""
        resultado = self.calc.multiplicar(7, 6)
        self.assertEqual(resultado, 42)
    
    def test_division(self):
        """Prueba unitaria: división normal"""
        resultado = self.calc.dividir(15, 3)
        self.assertEqual(resultado, 5)
    
    def test_division_por_cero(self):
        """Prueba unitaria: división por cero debe lanzar excepción"""
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)
    
    # PRUEBAS DE INTEGRACIÓN
    
    def test_operaciones_encadenadas(self):
        """Prueba de integración: operaciones encadenadas"""
        operaciones = [
            ('suma', 10),
            ('resta', 3),
            ('multiplica', 2),
            ('divide', 2)
        ]
        resultado = self.calc.operacion_compleja(operaciones)
        self.assertEqual(resultado, 7)  # ((0+10)-3)*2/2 = 7
    
    def test_operaciones_complejas(self):
        """Prueba de integración: secuencia compleja de operaciones"""
        operaciones = [
            ('suma', 5),
            ('multiplica', 3),
            ('resta', 10),
            ('divide', 5)
        ]
        resultado = self.calc.operacion_compleja(operaciones)
        self.assertEqual(resultado, 1)  # (((0+5)*3)-10)/5 = 1
    
    # PRUEBA DE RENDIMIENTO
    def test_rendimiento_suma_masiva(self):
        """Prueba de rendimiento: suma repetida miles de veces"""
        inicio = time.time()
        
        # Realizar 100,000 sumas
        for i in range(100000):
            self.calc.sumar(i, i+1)
        
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        
        # Verificar que el tiempo de ejecución sea razonable (menos de 1 segundo)
        self.assertLess(tiempo_ejecucion, 1.0, 
                       f"La prueba de rendimiento tomó {tiempo_ejecucion:.4f} segundos")
        
        print(f"\nPrueba de rendimiento: {tiempo_ejecucion:.4f} segundos para 100,000 operaciones")

if __name__ == '__main__':
    unittest.main(verbosity=2)