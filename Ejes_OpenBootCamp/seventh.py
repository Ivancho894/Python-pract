#En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos
# su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje
# con el resultado de la nota y si ha aprobado o no.



class Alumno:
    nombre = None
    nota = None
    def __init__(self,nombre,nota):
        self.nota = nota
        self.nombre = nombre
    def printear(self):
        if self.nota>=7:
            result = 'aprobado'

        else:
            result = 'desaprobado'
        print("El alumno: ",self.nombre, "Saco la nota: ",self.nota," por lo que esta",result)

yo = Alumno("Ivan",8)
yo.printear()