"""Aporte individual: validaciones, excepciones y registro de eventos."""

import logging
import math
from pathlib import Path

from excepciones import DatoInvalido, ReservaInvalida, ServicioNoDisponible, ErrorSistema


class ControlErrores:
    """Permite validar datos y ejecutar operaciones sin detener el programa."""

    def __init__(self, archivo_log=None):
        # Por defecto, el archivo se guarda junto al proyecto.
        if archivo_log is None:
            archivo_log = Path(__file__).resolve().parent / "registros" / "sistema.log"

        ruta = Path(archivo_log).resolve()
        ruta.parent.mkdir(parents=True, exist_ok=True)

        # Se utiliza el mismo registrador para un mismo archivo.
        self.registrador = logging.getLogger(f"software_fj.{ruta}")
        self.registrador.setLevel(logging.INFO)
        self.registrador.propagate = False

        # Evita que se registre el mismo evento varias veces.
        if not self.registrador.handlers:
            manejador = logging.FileHandler(ruta, encoding="utf-8")
            formato = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
            manejador.setFormatter(formato)
            self.registrador.addHandler(manejador)

    def validar_texto(self, valor, nombre_campo):
        """Comprueba que un texto obligatorio no esté vacío."""
        if not isinstance(valor, str) or not valor.strip():
            raise DatoInvalido(f"{nombre_campo} debe ser un texto no vacío")
        return valor.strip()

    def validar_entero_positivo(self, valor, nombre_campo):
        """Comprueba que un valor represente un entero mayor que cero."""
        if isinstance(valor, bool) or not isinstance(valor, (str, int)):
            raise DatoInvalido(f"{nombre_campo} debe ser un número entero")

        try:
            numero = int(valor)
        except ValueError as error:
            # El error original se conserva con 'from'.
            raise DatoInvalido(f"{nombre_campo} debe ser un número entero") from error
        else:
            if numero <= 0:
                raise DatoInvalido(f"{nombre_campo} debe ser mayor que cero")
            return numero

    def validar_precio(self, valor):
        """Comprueba que el precio sea numérico, finito y positivo."""
        if isinstance(valor, bool) or not isinstance(valor, (str, int, float)):
            raise DatoInvalido("El precio debe ser numérico")

        try:
            precio = float(valor)
        except ValueError as error:
            raise DatoInvalido("El precio debe ser numérico") from error

        if not math.isfinite(precio) or precio <= 0:
            raise DatoInvalido("El precio debe ser mayor que cero y válido")
        return precio

    def validar_disponibilidad(self, disponible):
        """Comprueba si un servicio se puede reservar."""
        if not isinstance(disponible, bool):
            raise DatoInvalido("La disponibilidad debe ser verdadera o falsa")
        if not disponible:
            raise ServicioNoDisponible("El servicio no se encuentra disponible")
        return True

    def validar_estado_reserva(self, estado):
        """Solo permite procesar una reserva en estado pendiente."""
        if not isinstance(estado, str) or estado.strip().lower() != "pendiente":
            raise ReservaInvalida("Solo se pueden procesar reservas pendientes")
        return True

    def ejecutar_operacion(self, descripcion, funcion, *args, **kwargs):
        """Ejecuta una función, registra el resultado y devuelve (éxito, dato)."""
        try:
            if not callable(funcion):
                raise DatoInvalido("Se debe proporcionar una función")
            resultado = funcion(*args, **kwargs)
        except ErrorSistema as error:
            # Errores esperados: datos, servicios o reservas inválidas.
            self.registrador.error("%s | %s", descripcion, error)
            return False, str(error)
        except Exception:
            # Los errores imprevistos también se registran con su detalle.
            self.registrador.exception("%s | Error inesperado", descripcion)
            return False, "Ocurrió un error inesperado. Revisar el log"
        else:
            self.registrador.info("%s | Operación exitosa", descripcion)
            return True, resultado
        finally:
            # Se ejecuta tanto si la operación tiene éxito como si falla.
            self.registrador.info("%s | Operación finalizada", descripcion)
