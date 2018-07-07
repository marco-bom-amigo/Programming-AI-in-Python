import datetime

data = datetime.date(1500, 4, 22)
print(data)

data_agora = datetime.datetime.now()
print(data_agora)

diferenca = data_agora.date() - data
print(diferenca)
print(diferenca.days)

meses = diferenca.days/30
print(meses)

