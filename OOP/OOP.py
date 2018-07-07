class TeslaRoadster(object):
    part_number = 12345
    def __init__(self, cor, self_drive="", ludicrous_mode="", autonomia=""):
        self.cor = cor
        self.self_drive = self_drive
        self.ludicrous_mode = ludicrous_mode
        self.autonomia = autonomia

print(TeslaRoadster.part_number)

tesla = TeslaRoadster(cor="preto")
print(tesla.cor)