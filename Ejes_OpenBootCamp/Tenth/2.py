#En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo,
# haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

import pickle



class Vehiculo:
    nombre = None
    color = None

    def __init__(self,nombre,color):
        self.nombre= nombre
        self.color = color
    def printear(self):
        print("El vehiculo es: " + self.nombre + " color: " + self.color)


miAuto = Vehiculo("Fiat","Negro")
f = open('miVehiculo.bin','wb')
pickle.dump(miAuto,f)
f.close()
p = open ('miVehiculo.bin','rb')
objeto = pickle.load(p)
p.close()
objeto.printear()