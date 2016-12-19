class Electrodomestico:

    def __init__(self, precio=100, color="blanco", consumo="F", peso=5):
        self.precio = precio
        self.color = color
        self.consumo = consumo
        self.peso = peso

    def getprecio(self):
        return self.precio

    def getconsumo(self):
        return self.consumo

    def getcolor(self):
        return  self.color

    def getpeso(self):
        return self.peso

    def comprobarconsumo(self, letra):
        if letra != "A" and letra != "B" and letra != "C" and letra != "D" and letra "E":
            self.consumo = "F"

    def comprobarcolor(self, color):
        if color != "negro" and color != "gris"
            self.color = "blanco"

    def preciofinal(self):
        if self.consumo == "A":
            self.precio += 100
        if self.consumo == "B":
            self.precio += 80
        if self.consumo == "C":
            self.precio += 60
        if self.consumo == "D":
            self.precio += 50
        if self.consumo == "E":
            self.precio += 30
        if self.consumo == "F":
            self.precio += 10

        if 0 <= self.peso <= 19:
            self.precio += 10
        elif 20 <= self.peso <= 49:
            self.precio += 50
        elif 50 <= self.peso <= 79:
            self.precio += 80
        elif 80 >= self.peso:
            self.precio += 100

    def imprimir(self):
        print("Precio: " + self.precio)
        print("Color: " + self.color)
        print("Consumo: " + self.consumo)
        print("Peso: " + self.peso)

class Lavadora(Electrodomestico):

    def __init__(self, carga=5, precio=100, color="blanco", consumo="F", peso=5):

