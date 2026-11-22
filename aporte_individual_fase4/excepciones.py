"""Excepciones personalizadas para el sistema Software FJ."""


class ErrorSistema(Exception):
    """Error general de las operaciones del sistema."""


class DatoInvalido(ErrorSistema):
    """Un dato obligatorio tiene un valor incorrecto."""


class ServicioNoDisponible(ErrorSistema):
    """El servicio solicitado no se encuentra disponible."""


class ReservaInvalida(ErrorSistema):
    """La reserva no puede continuar con el estado indicado."""
