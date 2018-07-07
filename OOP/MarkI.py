class MarkI(object):

    def __init__(self, arc_reactor, jet_boost, armadura, missil_qtde):
        self.arc_reactor = arc_reactor
        self.jet_boost = jet_boost
        self.armadura = armadura
        self.missil_qtde = missil_qtde

    def voar(self):
        print("Ativar modo voo")

    def lancar_missil(self):
        if self.missil_qtde > 0:
            self.missil_qtde -= 1
            print("Míssil lançado")
        else:
            print("Sem munição")
            
    def set_missil_qtde(self, missil_qtde):
        self.missil_qtde = missil_qtde