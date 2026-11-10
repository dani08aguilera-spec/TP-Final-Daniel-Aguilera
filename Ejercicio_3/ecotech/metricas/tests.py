from django.test import TestCase

import unittest
from .funcs import calcular_emisiones_carbono
 
 
class TestCalculoEmisiones(unittest.TestCase):
 
    def test_factor_por_defecto(self):
        consumo_kwh = 100
        factor_por_defecto = 0.4
 
        resultado_esperado = consumo_kwh * factor_por_defecto
        self.assertEqual(calcular_emisiones_carbono(consumo_kwh), resultado_esperado)
 
    def test_factor_personalizado(self):
        consumo_kwh = 100
        factor_personalizado = 0.5
 
        resultado_esperado = consumo_kwh * factor_personalizado
        self.assertEqual(
            calcular_emisiones_carbono(consumo_kwh, factor_personalizado),
            resultado_esperado
        )
 
    def test_caso_limite(self):
        resultado_esperado = 0
 
        self.assertEqual(calcular_emisiones_carbono(0, 300000), resultado_esperado)
 
    def test_decimales(self):
        resultado_esperado_aproximado = 4.12
 
        self.assertAlmostEqual(calcular_emisiones_carbono(10.3), resultado_esperado_aproximado, 5)
 
    def test_value_error(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-2000)
