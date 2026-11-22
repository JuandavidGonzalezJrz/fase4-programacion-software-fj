"""Pruebas del componente individual con unittest (incluido en Python)."""

import unittest
from pathlib import Path

from control_errores import ControlErrores
from excepciones import DatoInvalido, ReservaInvalida, ServicioNoDisponible
from simulacion_individual import (
    ClienteTemporal,
    ServicioTemporal,
    simular_cliente,
    simular_servicio,
    simular_reserva,
    simular_error_imprevisto,
)


class PruebasControlErrores(unittest.TestCase):
    def setUp(self):
        self.log = Path(__file__).resolve().parent.parent / "registros" / "pruebas.log"
        self.control = ControlErrores(self.log)

    def test_01_texto_valido(self):
        self.assertEqual(self.control.validar_texto(" Ana ", "Nombre"), "Ana")

    def test_02_texto_vacio(self):
        with self.assertRaises(DatoInvalido):
            self.control.validar_texto("  ", "Nombre")

    def test_03_texto_tipo_incorrecto(self):
        with self.assertRaises(DatoInvalido):
            self.control.validar_texto(100, "Nombre")

    def test_04_entero_valido(self):
        self.assertEqual(self.control.validar_entero_positivo("3", "Horas"), 3)

    def test_05_entero_cero(self):
        with self.assertRaises(DatoInvalido):
            self.control.validar_entero_positivo(0, "Horas")

    def test_06_entero_decimal_invalido(self):
        with self.assertRaises(DatoInvalido):
            self.control.validar_entero_positivo(2.5, "Horas")

    def test_07_encadenamiento_excepciones(self):
        with self.assertRaises(DatoInvalido) as error:
            self.control.validar_entero_positivo("dos", "Horas")
        self.assertIsInstance(error.exception.__cause__, ValueError)

    def test_08_precio_valido(self):
        self.assertEqual(self.control.validar_precio("25000"), 25000.0)

    def test_09_precio_infinito(self):
        with self.assertRaises(DatoInvalido):
            self.control.validar_precio(float("inf"))

    def test_10_precio_no_numerico(self):
        with self.assertRaises(DatoInvalido):
            self.control.validar_precio("caro")

    def test_11_servicio_disponible(self):
        self.assertTrue(self.control.validar_disponibilidad(True))

    def test_12_servicio_no_disponible(self):
        with self.assertRaises(ServicioNoDisponible):
            self.control.validar_disponibilidad(False)

    def test_13_reserva_estado_incorrecto(self):
        with self.assertRaises(ReservaInvalida):
            self.control.validar_estado_reserva("cancelada")

    def test_14_operacion_valida(self):
        exito, valor = self.control.ejecutar_operacion("Prueba válida", sum, [1, 2, 3])
        self.assertTrue(exito)
        self.assertEqual(valor, 6)

    def test_15_operacion_con_error_y_continuidad(self):
        fallo, _ = self.control.ejecutar_operacion(
            "Prueba inválida", self.control.validar_texto, "", "Nombre"
        )
        exito, valor = self.control.ejecutar_operacion(
            "Prueba posterior válida", self.control.validar_texto, "Ana", "Nombre"
        )
        self.assertFalse(fallo)
        self.assertTrue(exito)
        self.assertEqual(valor, "Ana")

    def test_16_error_imprevisto_controlado(self):
        exito, mensaje = self.control.ejecutar_operacion(
            "Prueba de error imprevisto", simular_error_imprevisto
        )
        self.assertFalse(exito)
        self.assertIn("log", mensaje)

    def test_17_log_registra_eventos(self):
        self.control.ejecutar_operacion("Verificar log correcto", simular_cliente, self.control, "Ana")
        self.control.ejecutar_operacion("Verificar log error", simular_cliente, self.control, "")
        contenido = self.log.read_text(encoding="utf-8")
        self.assertIn("Verificar log correcto | Operación exitosa", contenido)
        self.assertIn("Verificar log error |", contenido)
        self.assertIn("Operación finalizada", contenido)

    def test_18_simulacion_servicio(self):
        servicio = simular_servicio(self.control, "Sala", 20000)
        self.assertEqual(servicio.precio_hora, 20000.0)

    def test_19_simulacion_reserva_valida(self):
        cliente = ClienteTemporal("Ana")
        servicio = ServicioTemporal("Sala", 50000)
        resultado = simular_reserva(self.control, cliente, servicio, 2)
        self.assertIn("100000", resultado)

    def test_20_simulacion_reserva_no_disponible(self):
        cliente = ClienteTemporal("Ana")
        servicio = ServicioTemporal("Sala", 50000, False)
        with self.assertRaises(ServicioNoDisponible):
            simular_reserva(self.control, cliente, servicio, 2)

    def test_21_parametro_faltante(self):
        exito, mensaje = self.control.ejecutar_operacion(
            "Prueba con parámetro faltante", simular_cliente, self.control
        )
        self.assertFalse(exito)
        self.assertIn("log", mensaje)


if __name__ == "__main__":
    unittest.main()
