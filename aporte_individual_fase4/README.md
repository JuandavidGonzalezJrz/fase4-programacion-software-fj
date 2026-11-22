# Fase 4 - Aporte individual: control de errores (Software FJ)

**Curso:** Programación 213023, UNAD  
**Actividad:** Fase 4 - Componente práctico, prácticas simuladas  
**Integrante:** Juan David Gonzalez Jerez  
**Grupo:** 261



## ¿Qué hace mi aporte?

Este componente valida datos comunes y permite ejecutar operaciones del sistema controlando sus errores. Incluye excepciones propias, `try/except`, `try/except/else`, `try/finally`, encadenamiento con `raise ... from ...` y `logging`. Cuando ocurre un error, devuelve `(False, mensaje)` y registra lo sucedido. Una operación correcta devuelve `(True, resultado)`.

No contiene el sistema completo de clientes, servicios y reservas. Las clases `ClienteTemporal` y `ServicioTemporal`, dentro de `simulacion\_individual.py`, **son únicamente objetos de ejemplo para probar mi componente**. Deben reemplazarse por las clases reales creadas en el proyecto grupal.



## Archivos

* `excepciones.py`: excepciones personalizadas que podrá utilizar el grupo.
* `control\_errores.py`: mi módulo principal de validaciones, ejecución controlada y logs.
* `simulacion\_individual.py`: demostración con objetos temporales y 16 casos.
* `pruebas/test\_control\_errores.py`: 21 pruebas automáticas de mi aporte.
* `evidencias/`: ejemplos de salida y registro generados al ejecutar las pruebas.
* `registros/`: se crea automáticamente; los logs nuevos no se suben de forma automática a Git.
* 

## Requisitos

Python 3.10 o superior. No necesita instalar librerías externas.



## Cómo ejecutar

Desde la carpeta del proyecto:

```bash
python simulacion\_individual.py
python -m unittest discover -s pruebas -v
```

En algunos sistemas el comando es `py` en lugar de `python`.

Los registros quedan en `registros/sistema.log` y `registros/pruebas.log`.



## Cómo integrar con el proyecto del grupo

1. Conservar `excepciones.py` y `control\_errores.py`.
2. Importar las excepciones en las clases reales cuando haya datos, servicios o reservas inválidas.
3. Utilizar `ControlErrores().ejecutar\_operacion(...)` para llamar a los métodos del grupo y evitar que los errores detengan el flujo principal.
4. Sustituir los objetos temporales del ejemplo por las clases reales. Los nombres, parámetros y condiciones deben ajustarse cuando el equipo defina sus clases.

Ejemplo sencillo (solo si la clase `Reserva` de los compañeros dispone de `confirmar`):

```python
from control\_errores import ControlErrores

control = ControlErrores()
# reserva\_real sería un objeto creado en el módulo de otro integrante.
exito, resultado = control.ejecutar\_operacion(
    "Confirmar reserva", reserva\_real.confirmar
)
if exito:
    print("Reserva confirmada:", resultado)
else:
    print("No se pudo confirmar:", resultado)
```

**Nota:** `reserva\_real` es un nombre ilustrativo y no existe en este repositorio; es un ejemplo para adaptar, no un archivo ejecutable.



## Alcance y limitaciones

* Mi aporte realiza 16 simulaciones de validación y control de errores y 21 pruebas automáticas.
* Estas pruebas **no sustituyen** las 10 operaciones completas del sistema real que pide el Anexo 3. Las deben realizar los integrantes después de integrar todos los componentes.
* Mi aporte no contiene base de datos, gestión completa de clientes, alquileres, asesorías, confirmaciones, cancelaciones ni cálculo de impuestos o descuentos; esas funcionalidades pertenecen al proyecto grupal.
* Se registran las operaciones que pasan por `ejecutar\_operacion`. Si otra parte llama directamente una validación, debe capturar y registrar la excepción en su propio flujo.
* Un error normal de operación no detiene las simulaciones; no se garantiza continuidad frente a fallos externos extremos, por ejemplo falta de permisos para crear el archivo de registro.
* 

## Evidencia de participación

* **Rama:** `\[nombre-de-la-rama]`
* **Commits:** `\[enlace o identificadores de los commits realizados]`
* **Pull request:** `\[enlace cuando se cree]`
* **Foro UNAD:** `\[enlace o fecha de publicación]`

Las rutas y enlaces se completan **después** de hacer estas acciones realmente.

