#En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time.
# Necesitaréis la fecha del sistema y poder comprobar la hora.
#En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.
from datetime import datetime



now = datetime.now()

def checkReturnTime():
    if now.hour<=19:
        cuanto = 19-now.hour
        print("Todavia tenes que permanecer trabajndo",cuanto,"horas")
    else:
        print("Ya es hora de ir a casa")


checkReturnTime()