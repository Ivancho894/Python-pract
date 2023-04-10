#En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
#Color
#Ruedas
#Puertas
#Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
#Velocidad
#Cilindrada
#Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.


class Vehiculo:
    color = ''
    ruedas = 0
    puertas = 0


class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0
    def __init__(self,color,ruedas,puertas,velocidad,cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def printear(self):
        print("Color: ",self.color," ruedas: ", self.ruedas," Cant puertas: ",self.puertas," velocidad max: ", self.velocidad, " cilindrada: ", self.cilindrada)


miAuto = Coche("blanco",4,4,120,3)
print(miAuto.printear())

