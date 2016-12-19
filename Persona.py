import random

class Persona:

    def __init__(self, nombre="", edad=0, sexo="M", peso=0, altura=0):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.dni = ""
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.generadni()
        self.introducirsexo(self.sexo)

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
        if sexo == "H":
            self.sexo = "Hombre"
        else:
            self.sexo = "Mujer"

    def tostring(self):
        print(self.nombre, self.edad, self.dni, self.sexo, self.peso, self.altura)

    def generadni(self):
        dni = {}
        for x in range(8):
            dni[x] = random.randint(0, 9)

        dni[9] = random.choice("A" "B" "C" "D" "E" "F" "G")
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

    def imprimir(self):
        print(self.nombre, self.edad, self.sexo, self.peso, self.altura)

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
    #p3.introducirsexo()
    p3.setPeso(peso)
    p3.setaltura(altura)
    p1.esmayordeedad()
    p2.esmayordeedad()
    p3.esmayordeedad()
    p1.imprimir()
    p2.imprimir()
    p3.imprimir()

Main()

