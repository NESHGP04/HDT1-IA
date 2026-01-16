# Marinés García
from environment import Environment
from agent import Agent

def main():
    env = Environment()
    agent = Agent()

    print("Simulación de Termostato Inteligente\n")

    for step in range(10):
        print(f"Iteración {step + 1}")

        # Percepción
        current_temp = env.get_percept()
        print(f"Temperatura actual: {current_temp}°C")

        # Decisión del agente
        action = agent.act(current_temp)
        print(f"Acción del agente: {action}")

        # Acción sobre el entorno
        env.update(action)
        new_temp = env.get_percept()
        print(f"Nueva temperatura: {new_temp}°C\n")

if __name__ == "__main__":
    main()