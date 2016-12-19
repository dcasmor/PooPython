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

    def calcularimc(self, peso, altura):
        if float(self.altura) != 0:
            imc = int(self.peso)/(float(self.altura)**2)
            if imc in (20, 25):
                print ("Está en su peso ideal")
                return 0
            if imc < 20:
                print("Infrapeso")
                return -1
            else:
                print("Sobrepeso")
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

    def generadni(self):
        dni = {}
        for x in range(8):
            dni[x] = random.randint(0, 9)

        dni[9] = random.choice("A" "B" "C" "D" "E" "F" "G" "H" "I" "J" "K" "L" "M" "N"
                               "O" "P" "Q" "R" "S" "T" "U" "V" "W" "X" "Y" "Z")
        self.dni = dni


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
        print("Nombre:", self.nombre)
        print("Edad: ", self.edad)
        print("DNI: ", self.dni)
        print("Sexo: ", self.sexo)
        print("Peso:", self.peso)
        print("Altura: ", self.altura)
        self.calcularimc(self.peso, self.altura)

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

Main()

