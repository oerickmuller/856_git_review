from datetime import datetime

from modelo import Modelo

def main(): 
    print(datetime.now())
    m = Modelo()
    m.modelar()
    print("Iniciando a aplicacao")