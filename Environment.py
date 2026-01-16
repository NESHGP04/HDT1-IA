# Camila Richter

import random

class Environment:
    def __init__(self):
        self.actual_temp = random.randint(0, 100) #inicializa la temperatura en un número random

    def get_percept(self): #devuelve temperatura actual
        return self.actual_temp 

    def update(self, action): #modifica la temperatura actual
        if action == "enfriar":
            self.actual_temp -= 1
        elif action == "calentar":
            self.actual_temp += 1
        elif action == "mantener":
            pass

    