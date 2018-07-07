import math

class Circulo(object):

    def __init__(self, raio):
        self.raio = raio

    def get_area(self):
        return math.pi * self.raio ** 2

    def get_perimetro(self):
        return 2 * math.pi * self.raio

    def get_raio(self):
        return self.raio

    def set_raio(self, raio):
        self.raio = raio

circulo = Circulo(10)

print(circulo.get_area())
print(circulo.get_perimetro())
print(circulo.get_raio())

circulo.set_raio(54)

print(circulo.get_raio())
print((circulo.get_area(), circulo.get_perimetro()))