class Linha(object):

    def __init__(self, coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2

    def get_distancia(self):
        x1, x2 = self.coord1
        y1, y2 = self.coord2
        return ((x2 -x1 )**2 + (y2 -y1 ) **2)**0.5

    def get_inclinacao(self):
        x1, x2 = self.coord1
        y1, y2 = self.coord2
        return ((y2 -y1 ) / (x2 -x1))

    def __len__(self):
        return int(self.get_distancia())

x1 = (10,5)
x2 = (40,31)

linha = Linha(x1, x2)

print(linha.get_distancia())
print(linha.get_inclinacao())
print(len(linha))