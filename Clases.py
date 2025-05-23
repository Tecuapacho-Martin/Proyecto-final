class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
persona1 = Persona("Ana", 20)
persona1.saludar()
if persona1.es_mayor_de_edad():
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")
