# Hoja de Trabajo #1 - Termostato Inteligente (Agente Reflejo Simple)

Autoras: Camila Richter (23183), Marinés García (23391)

## Resumen
Implementación en Python de un Agente Reflejo Simple que interactúa con un entorno que simula un termostato. El agente percibe la temperatura actual y decide si calentar, enfriar o esperar, demostrando el ciclo percepción → decisión → acción.

## Contenido del README
- Descripción
- Requisitos
- Instalación y ejecución
- Estructura del proyecto
- Descripción breve de los módulos
- Ejemplo de uso y salida esperada

## Requisitos
- Python 3.8 o superior
- (Opcional) Crear un entorno virtual para aislar dependencias

No se necesitan librerías externas fuera de la biblioteca estándar para ejecutar el proyecto.

## Instalación
1. Clonar el repositorio o descargar los archivos en una carpeta local.
2. (Opcional) Crear y activar un entorno virtual:

   python3 -m venv venv
   source venv/bin/activate

3. Ejecutar el proyecto con Python:

   python3 main.py

## Estructura del proyecto
```
HDT1-IA/
├── agent.py         # Implementación del agente reflejo
├── environment.py   # Implementación del entorno (termómetro, física simple)
├── main.py          # Ciclo percepción → acción y entrada principal
├── README.md        # Este archivo
```

## Descripción breve de los módulos
- `environment.py`:
  - Clase `Environment` que mantiene la temperatura actual (`actual_temp`).
  - Métodos principales:
    - `get_percept()` — devuelve la temperatura actual (simula el sensor).
    - `update(action)` — aplica la acción del agente y ajusta la temperatura.

- `agent.py`:
  - Clase `Agent` con la función `act(percept)` que, a partir de la temperatura percibida, decide:
    - `"enfriar"` si temp > 25
    - `"calentar"` si temp < 18
    - `"esperar"` en caso contrario

- `main.py`:
  - Crea instancias de `Environment` y `Agent` y ejecuta el bucle principal durante varias iteraciones.
  - Imprime la temperatura, la acción elegida y la nueva temperatura.

## Uso — ejemplo
Al ejecutar `python3 main.py` verás una salida similar a la siguiente (resumen):

Iteración 1
Temperatura actual: 30°C
Acción del agente: enfriar
Nueva temperatura: 29°C

Iteración 2
Temperatura actual: 29°C
Acción del agente: enfriar
Nueva temperatura: 28°C

... (y así sucesivamente durante las iteraciones definidas en `main.py`)

## Extensiones sugeridas (opciones para ampliar el trabajo)
- Añadir histéresis o un control proporcional para evitar oscilaciones.
- Guardar un log de las temperaturas para graficar el comportamiento.
- Permitir parámetros de configuración (temperatura objetivo, rango aceptable, número de iteraciones).

## Créditos
- Camila Richter — implementación y diseño
- Marinés García — documentación y pruebas

## Licencia
Repositorio de trabajo de curso (sin licencia específica). Para uso académico y personal.

---
Si quieres, aplico estos cambios al `README.md` ahora y dejo una nota de qué edité y por qué.