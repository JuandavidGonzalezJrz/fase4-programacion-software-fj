"""Simulación de prueba; las clases temporales NO son el proyecto grupal."""

from control_errores import ControlErrores
from excepciones import DatoInvalido


# Estos objetos mínimos solo permiten probar el módulo individual.
class ClienteTemporal:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Cliente temporal: {self.nombre}"


class ServicioTemporal:
    def __init__(self, nombre, precio_hora, disponible=True):
        self.nombre = nombre
        self.precio_hora = precio_hora
        self.disponible = disponible

    def __str__(self):
        return f"Servicio temporal: {self.nombre}"


# No se guardan datos ni se sustituyen las clases del equipo.
def simular_cliente(control, nombre):
    nombre = control.validar_texto(nombre, "El nombre del cliente")
    return ClienteTemporal(nombre)


def simular_servicio(control, nombre, precio_hora):
    nombre = control.validar_texto(nombre, "El nombre del servicio")
    precio = control.validar_precio(precio_hora)
    return ServicioTemporal(nombre, precio)


def simular_reserva(control, cliente, servicio, horas, estado="pendiente"):
    if not isinstance(cliente, ClienteTemporal):
        raise DatoInvalido("Debe indicar un cliente válido")
    if not isinstance(servicio, ServicioTemporal):
        raise DatoInvalido("Debe indicar un servicio válido")

    control.validar_estado_reserva(estado)
    control.validar_disponibilidad(servicio.disponible)
    duracion = control.validar_entero_positivo(horas, "La duración")

    # Resultado simple para comprobar las validaciones, no una reserva real.
    costo = servicio.precio_hora * duracion
    return f"Reserva simulada de {cliente.nombre}: {duracion} h, costo {costo:.0f}"


def simular_error_imprevisto():
    # Un fallo intencional para revisar el registro y la continuidad.
    return 10 / 0


def ejecutar_simulaciones():
    control = ControlErrores()
    cliente = ClienteTemporal("María")
    servicio = ServicioTemporal("Sala de reuniones", 50000)
    servicio_ocupado = ServicioTemporal("Equipo", 30000, False)

    # Cada caso se ejecuta por separado: un error no detiene el siguiente.
    casos = [
        ("01 Cliente válido", simular_cliente, (control, "Ana")),
        ("02 Cliente sin nombre", simular_cliente, (control, "")),
        ("03 Nombre de cliente incorrecto", simular_cliente, (control, 123)),
        ("04 Servicio válido", simular_servicio, (control, "Sala", 50000)),
        ("05 Servicio con precio negativo", simular_servicio, (control, "Equipo", -10)),
        ("06 Servicio con precio en letras", simular_servicio, (control, "Asesoría", "caro")),
        ("07 Servicio con precio infinito", simular_servicio, (control, "Sala", float("inf"))),
        ("08 Reserva válida", simular_reserva, (control, cliente, servicio, 2)),
        ("09 Reserva con duración cero", simular_reserva, (control, cliente, servicio, 0)),
        ("10 Servicio no disponible", simular_reserva, (control, cliente, servicio_ocupado, 2)),
        ("11 Reserva ya cancelada", simular_reserva, (control, cliente, servicio, 2, "cancelada")),
        ("12 Reserva sin cliente", simular_reserva, (control, None, servicio, 2)),
        ("13 Duración no numérica", simular_reserva, (control, cliente, servicio, "dos")),
        ("14 Error imprevisto", simular_error_imprevisto, ()),
        ("15 Cliente sin parámetro obligatorio", simular_cliente, (control,)),
        ("16 Otra reserva válida después de errores", simular_reserva, (control, cliente, servicio, 1)),
    ]

    exitos = 0
    for descripcion, funcion, argumentos in casos:
        funciona, resultado = control.ejecutar_operacion(descripcion, funcion, *argumentos)
        if funciona:
            exitos += 1
        print(f"{descripcion}: {'CORRECTO' if funciona else 'CONTROLADO'} | {resultado}")

    print(f"\nSe ejecutaron {len(casos)} simulaciones: {exitos} exitosas y {len(casos) - exitos} con errores controlados.")
    print("Archivo de registro: registros/sistema.log")


if __name__ == "__main__":
    ejecutar_simulaciones()
