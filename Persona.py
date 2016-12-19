import random

class Persona:
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.dni = ""
        self.sexo = "M"
        self.peso = 0
        self.altura = 0
        self.generardni()

    def __init__(self, nombre="", edad=0, sexo="M"):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.dni = ""
        self.sexo = "M"
        self.peso = 0
        self.altura = 0
        self.generardni()
        self.comprobarsexo(self.sexo)

    def __init__(self, nombre="", edad=0, sexo="M", peso=0, altura=0):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.dni = ""
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.generardni()
        self.comprobarsexo(self.sexo)

    def calcularimc(self):
        if float(self.altura) != 0:
            imc = int(self.peso)/(self.altura**2)
            if imc >= 20 & imc <= 25:
                return 0
            if imc < 20:
                return -1
            else:
                return 1

    def esmayordeedad(self):
        if int(self.edad) >= 18:
            return True
        else:
            return False

    def introducirsexo(self, sexo):
        if sexo != "H" | sexo != "M":
            self.sexo = "M"

    def tostring(self):
        print(self.nombre, self.edad, self.dni, self.sexo, self.peso, self.altura)

    def generadni(self):
        dni = {}
        for x in range(9):
            dni[x] = random.randint(0, 9)

        dni[10] = random.choice("A", "B")
        print(dni)


    def setnombre(self, nombre):
        self.nombre = nombre

    def setedad(self, edad):
        self.edad = edad

    def setsexo(self, sexo):
        self.introducirsexo(sexo)

    def setPeso(self, peso):
        self.peso = peso

    def setaltura(self, altura):
        self.altura = altura

class Main:
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    sexo = input("Sexo: ")
    peso = input("Peso: ")
    altura = input("Altura (en metros): ")
    p1 = Persona(nombre, edad, sexo, peso, altura)
    p2 = Persona(nombre, edad, sexo)
    p3 = Persona()
    p3.setnombre(nombre)
    p3.setedad(edad)
    p3.setsexo(sexo)
    p3.introducirsexo()
    p3.setPeso(peso)
    p3.setaltura(altura)
    p1.esmayordeedad()
    p2.esmayordeedad()
    p3.esmayordeedad()
    p1.imprimir()


Main()

