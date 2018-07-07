class TeslaS(object):

    part_number = 123456

    def __init__(self, cor, self_drive=True, autonomia=320, ludicrous_mode=False):
        self.cor = cor
        self.self_drive = self_drive
        self.autonomia = autonomia
        self.ludicrous_mode = ludicrous_mode

    def ligar(self):
        self.status = "Ligado"
        print(self.status)

    def desligar(self):
        self.status = "Desligado"
        print(self.status)

    def set_cor(self, cor):
        self.cor = cor

    def get_cor(self):
        return self.cor

    def gen_service_tag(self):
        print("Part Number: %s\nCor: %s\nSelf-Drive: %s" % (TeslaS.part_number, self.cor, self.self_drive))
