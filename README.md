Hoja de Trabajo #1 - Inteligencia Artificial

Autores: Camila Richter 23183
         Marinés García 23391

# Termostato Inteligente – Agente Reflejo Simple

## Descripción del Proyecto
Este proyecto implementa la **estructura básica de un Agente Reflejo Simple**, siguiendo la Arquitectura de Agente vista en clase (Slides 26–29).  
El objetivo no es resolver un problema complejo de búsqueda, sino **traducir el concepto teórico de agente y entorno a código orientado a objetos en Python**.

El sistema simula un **termostato inteligente**, donde un agente percibe la temperatura del entorno y decide una acción para regularla.

---

## Objetivo
- Implementar un **Agente Reflejo Simple**.
- Separar claramente el **Entorno (Environment)** del **Agente (Agent)**.
- Implementar el **ciclo Percepción → Acción** durante varias iteraciones.
- Mostrar cómo la función del agente depende únicamente de la percepción actual.

---

## Estructura del Proyecto
proyecto/
│── main.py
│── environment.py
│── agent.py
│── README.md

---

## Environment (Entorno)
La clase `Environment` representa el entorno físico del termostato.

### Características:
- Contiene una variable `actual_temp` que representa la temperatura actual.
- La temperatura inicial se genera de forma aleatoria.
- Provee métodos para que el agente perciba y actúe sobre el entorno.

### Métodos:
- `__init__()`  
  Inicializa la temperatura con un valor aleatorio.
- `get_percept()`  
  Simula los sensores y devuelve la temperatura actual.
- `update(action)`  
  Modifica la temperatura según la acción recibida:
  - `"enfriar"` → disminuye la temperatura.
  - `"calentar"` → aumenta la temperatura.
  - `"esperar"` → no realiza cambios.

---

## Agent (Agente)
La clase `Agent` representa un **agente reflejo simple**.

### Características:
- No tiene memoria del pasado.
- Toma decisiones únicamente con base en la percepción actual.
- Implementa la función del agente:  
  **f(percepción) → acción**

### Lógica del método `act(perception)`:
- Si la temperatura es mayor a 25 → retorna `"enfriar"`.
- Si la temperatura es menor a 18 → retorna `"calentar"`.
- En cualquier otro caso → retorna `"esperar"`.

---

## Ciclo Percepción / Acción (main)
El archivo `main.py` implementa el ciclo principal del sistema.

### Funcionamiento:
- Se crean instancias del `Environment` y del `Agent`.
- El sistema se ejecuta durante **10 iteraciones**.
- En cada iteración se imprime:
  - La temperatura actual (percepción).
  - La acción seleccionada por el agente.
  - La nueva temperatura después de ejecutar la acción.

Este ciclo simula el comportamiento continuo de un agente interactuando con su entorno.

---

## Ejemplo de Salida
Iteración 1
Temperatura actual: 30°C
Acción del agente: enfriar
Nueva temperatura: 29°C

---

## Conclusión
Este proyecto demuestra cómo los conceptos teóricos de:
- Agente
- Entorno
- Percepción
- Acción
- Función del agente  

pueden ser representados de forma clara mediante **programación orientada a objetos**, cumpliendo con la definición de un **Agente Reflejo Simple**.

---