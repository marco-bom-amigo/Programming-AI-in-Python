from OOP.MarkI import MarkI

class BleedingEdge(MarkI):

    def __init__(self, arc_reactor, jet_boost, armadura, missil_qtde, personal_assistant, nanotech, laser_qtde=1):
        MarkI.__init__(self, arc_reactor, jet_boost, armadura, missil_qtde)
        self.personal_assistant = personal_assistant
        self.nanotech = nanotech
        self.laser_qtde = laser_qtde

    def lancar_laser(self):
        if self.laser_qtde > 0:
            self.laser_qtde -= 1
            print("Laser ativado")
        else:
            print("Sem cartucho de laser")

    def set_laser_qtde(self, laser_qtde):
        self.laser_qtde = laser_qtde