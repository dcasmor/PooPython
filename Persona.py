class Persona:

    __nombre = ""
    __edad = 0
    __DNI = 0
    __sexo = 'M'
    __peso = 0
    __altura = 0

    def __init__(self):
        self.__nombre = ""
        self.__edad = 0
        self.__dni = ""
        self.__sexo = "M"
        self.__peso = 0
        self.__altura = 0
        self.generarDni()

    def __init__(self, nombre="", edad=0, sexo="M"):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__dni = ""
        self.__sexo = "M"
        self.__peso = 0
        self.__altura = 0
        self.generarDni()
        self.comprobarSexo(self.sexo)

    def __init__(self, nombre, edad, dni, sexo, peso, altura):
        this.nombre = nombre

    def calcularimc(self):
        imc = peso/(altura**2)
        if imc>=20 & imc<=25:
            return 0
        if imc < 20:
            return -1
        else:
            return 1

    def esMayorDeEdad(self):
        if edad >= 18:
            return True
        else:
            return False

    def introducirSexo(self, sexo):
        if sexo != "H" | sexo != "M":
            self.sexo = "M"

    def toString(self):
        print(nombre, edad, dni, sexo, peso, altura)

    def generaDni(self):
        this.dni = dni

    def setNombre(self, nombre):
        this.nombre = nombre

    def setEdad(self, edad):
        this.edad = edad

    def setSexo(self, sexo):
        introducirSexo(sexo)

    def setPeso(self, peso):
        this.peso = peso

    def setAltura(self, altura):
        this.altura = altura

