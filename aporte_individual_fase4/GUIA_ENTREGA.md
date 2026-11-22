# Guía corta para entregar mi aporte en GitHub y en la UNAD

**Importante:** este documento es una guía. No confirma que los pasos de GitHub o del foro ya se realizaron.

## 1. Ejecutar y revisar

Desde la carpeta `aporte_individual_fase4`:

```bash
python simulacion_individual.py
python -m unittest discover -s pruebas -v
```

Revisar `registros/sistema.log` y `registros/pruebas.log` y tomar una captura propia de la consola y otra del registro si se requiere. La carpeta `evidencias` tiene **ejemplos generados al probar este código**, no evidencia de publicación por parte del estudiante.

## 2. Subir mi contribución a GitHub

Usar el **repositorio del grupo** si existe y se tiene acceso de escritura. Para no reemplazar archivos del equipo, se recomienda crear en ese repositorio la carpeta `aportes/control_errores/` y copiar allí el contenido de este proyecto. No reemplazar los archivos `README.md` o `.gitignore` de la raíz del equipo.

Desde una terminal dentro del repositorio grupal:

```bash
git pull origin main
git switch -c aporte/control-errores-apellido
```

Si la rama principal del grupo se llama `master`, utilizar `master` en lugar de `main`. Si no existe un repositorio grupal, pedir el enlace y acceso; se puede publicar un repositorio individual como evidencia provisional, pero eso no reemplaza la colaboración requerida.

Después de copiar la carpeta al repositorio:

```bash
git add aportes/control_errores/excepciones.py
git commit -m "Agregar excepciones personalizadas"

git add aportes/control_errores/control_errores.py
git commit -m "Implementar validaciones y registro de errores"

git add aportes/control_errores/simulacion_individual.py aportes/control_errores/pruebas
git commit -m "Agregar simulaciones y pruebas automatizadas"

git add aportes/control_errores/README.md aportes/control_errores/GUIA_ENTREGA.md aportes/control_errores/evidencias aportes/control_errores/.gitignore aportes/control_errores/registros/.gitkeep
git commit -m "Documentar el aporte y sus evidencias"

git push -u origin aporte/control-errores-apellido
```

**Notas:** los logs producidos automáticamente están ignorados; los ejemplos de la carpeta `evidencias` sí se incluyen. No es necesario subir `__pycache__` ni `.pyc`.

Entrar a GitHub y seleccionar **Compare & pull request**. Colocar como título `Fase 4 - Validaciones, manejo de excepciones y logs`. En la descripción indicar qué archivos agregaste, cómo ejecutar las 16 simulaciones y las 21 pruebas, y que las clases temporales no sustituyen las del equipo. Crear el pull request hacia la rama principal; no afirmar que fue integrado hasta que lo aprueben y fusionen.

La rúbrica también menciona **issues asignados**: si tienes permisos, crear un issue titulado `Implementar excepciones y registro de errores`, asignártelo y enlazar el pull request. Solo documentar el issue si realmente fue creado.

## 3. Publicación para el foro (completar antes de enviar)

Asunto: Fase 4 - Aporte individual: manejo de excepciones y logs

Buen día, compañeros y tutor.

Como aporte a la Fase 4, preparé un módulo de manejo de excepciones y validación de datos para el Sistema Integral de Gestión de Clientes, Servicios y Reservas. Incluye excepciones personalizadas, validaciones de textos y números, control de disponibilidad, estados de reserva y registro de eventos y errores mediante `logging`.

Para verificarlo, ejecuté [número real] simulaciones y [número real] pruebas automatizadas, con el siguiente resultado: [resultado]. Utilicé clases temporales únicamente para las pruebas; el componente se podrá conectar a las clases definitivas del equipo mediante el método `ejecutar_operacion`.

Repositorio: [enlace real]  
Rama o pull request: [enlace real]

Quedo atento a los ajustes necesarios para integrarlo al trabajo grupal.

## 4. Relación con la rúbrica

- **Excepciones (50):** demostrable con el módulo, el log y las pruebas.
- **Simulaciones y logs (35):** pruebas individuales demostrables, pero las 10 operaciones completas del sistema son del equipo.
- **Claridad del código (35):** código documentado y pruebas del componente; evaluación del proyecto general sigue pendiente.
- **Colaboración GitHub (30):** tu rama, commits y pull request serían evidencia individual. La participación equilibrada de los cinco miembros depende del grupo.

La guía exige además un **único documento grupal en PDF** con portada, introducción, enlace al repositorio, conclusiones y referencias en APA. Este aporte individual no reemplaza esa entrega.
