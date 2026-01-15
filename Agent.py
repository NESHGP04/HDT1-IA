# Camila Richter

class Agent:
    def act(self, perception): #función que implementa la lógica f(estado)
        if perception > 25:
            return "enfriar"
        elif perception < 18:
            return "calentar"
        else:
            return "esperar"
