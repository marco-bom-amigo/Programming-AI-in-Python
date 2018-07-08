from collections import Counter, defaultdict, namedtuple
import functools
import datetime
import re

def quadrado1(numero):
    resultado = numero**2
    return resultado

def quadrado2(numero):
    return numero**2

quadrado3 = lambda numero: numero**2

def quadrado4(numero): return numero**2

print(quadrado1(4))
print(quadrado2(4))
print(quadrado3(4))
print(quadrado4(4))

def soma1(num1, num2):
    return num1 + num2

soma2 = lambda num1, num2: num1 + num2

print(soma1(1,3))
print(soma2(1,3))

def multiplicacao1(num1, num2, num3):
    return num1 * num2 * num3

multiplicacao2 = lambda x1, x2, x3: x1 * x2 * x3

print(multiplicacao1(1, 2, 3))
print(multiplicacao2(1, 2, 3))

lista = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 4, 5, 6, 5, 3, 3, 3]
print(Counter(lista))

lista = "kljlkqjqj321;k3;kkdla"
print(Counter(lista))

frase = "As Duas Torres é a Segunda parte da grande obra de ficção fantástica de J. R. R. Tolkien, O Senhor dos Anéis. É impossível transmitir ao novo leitor todas as qualidades e o alcance do livro. Alternadamente cômica, singela, épica, monstruosa e diabólica, a narrativa desenvolve-se em meio a inúmeras mudanças de cenários e de personagens, num mundo imaginário absolutamente convincente em seus detalhes. Nas palavras do romancista Richard Hughes, ´quanto à amplitude imaginativa, a obra praticamente não tem paralelos e é quase igualmente notável na sua vividez e na habilidade narrativa, que mantêm o leitor preso página após página´."
palavras = frase.split(" ")
contador = Counter(palavras)
print(contador)
print(contador.most_common(3))

dd = defaultdict(object)
dd["chave"]
[print(item) for item in dd]

dd_2 = defaultdict(lambda : 0)
print(dd_2["chave"])

for item in dd_2:
    print(item)
    print(dd_2[item])

Cachorro = namedtuple("Cachorro", "nome raca peso cor")
cachorro_1 = Cachorro(nome="Totó", raca="Pastor Alemão", peso=80, cor="Azul")
print(cachorro_1)

def kph_to_mph(kmh):
    mph = 0.6214 * kmh
    return mph
velocidades_kph = [100, 124, 200, 150, 178, 182]
velocidades_mph = list(map(kph_to_mph, velocidades_kph))
print(velocidades_mph)

velocidades_mph = list(map(lambda v: (0.6214) * v, velocidades_kph))
print(velocidades_mph)

lista = [1, 2, 3, 4, 5, 6]
lista_1 = [1, 2, 3, 4]
lista_2 = [1, 2, 3, 4]
lista_3 = [1, 2, 3, 4]

lista_soma = list(map(lambda a, b, c: (a + b + c), lista_1, lista_2, lista_3))
print(lista_soma)

lista_soma = functools.reduce(lambda x, y: (x + y), lista)
print(lista_soma)

def is_par(num):
    resto = num % 2
    if resto == 0:
        return True
    else:
        return False
lista_num = range(10)
lista_par = list(filter(is_par, lista_num))
print(lista_par)

lista_impar = list(filter(lambda x: x % 2 !=0, lista_num))
print(lista_impar)

lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
lZip = list(zip(lista_1, lista_2))
print(lZip)

maior_numero_lista = map(lambda par: max(par),
list(zip(lista_1, lista_2)))
lMaior = list(maior_numero_lista)
print(lMaior)

lista = range(1, 6)
for item in lista:
    print(item)

for indice, item in enumerate(lista):
    print("%s - %s" %(indice, item))

lista = [True, True, True, True]
print(any(lista))
print(all(lista))

lista_alt_1 = [True, False, True, True]
print(any(lista_alt_1))
print(all(lista_alt_1))

lista_alt_2 = [False, False, False, False]
print(any(lista_alt_2))
print(all(lista_alt_2))

palavra = "Paralelepípedo"
print(list(palavra))
print(set(palavra))

def gerar_quadrados(num):
    for n in range(num):
        yield n**2

for x in gerar_quadrados(5):
    print(x)

g = gerar_quadrados(3)
print(next(g))
print(next(g))
print(next(g))


print("Iniciando...")
try:
    'a' + 10
except TypeError:
    print("Erro de tipo")
finally:
    print("Operação realizada")


data1 = datetime.date(2018, 4, 25)
data2 = datetime.date(2017, 3, 25)
print(data1-data2)

data_hora1 = datetime.datetime(2018, 4, 25, 20, 0)
data_hora2 = datetime.datetime(2018, 4, 25, 15, 0)
print(data_hora1 - data_hora2)

time = datetime.time(23,35,0)
date = datetime.date(2018, 4, 25)
date_time = datetime.datetime(2018, 4, 20, 23, 34)
print(time)
print(date)
print(date_time)

print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)

print(datetime.date.min)
print(datetime.date.max)
print(datetime.date.resolution)

print(datetime.datetime.min)
print(datetime.datetime.max)
print(datetime.datetime.resolution)

print(datetime.timedelta(0, 0, 1))
print(datetime.timedelta(1))

padroes = ["prédio", "rua", "casa"]
texto = "O prédio que trabalharam ficava na rua de cima."
for padrao in padroes:
    if re.search(padrao, texto):
        print("Encontrado correspondência para %s." % padrao)
    else:
        print("Não encontrado correspondência para %s." % padrao)

padroes = ["sd*", "sd+", "sd?", "sd{3}", "sd{2,3}", "[sd]", "s[sd]+"]
frase_teste = "sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd"
for padrao in padroes:
    print(padrao + " " + str(re.findall(padrao, frase_teste)))

padrao = "[^!.?,; ]+"
print(re.findall(padrao, frase))

padroes = ["[a-z]+", "[A-Z]+", "[A-zA-Z]+", "[A-Z][a-z]+"]
frase_teste = "Ontem houve algum problema. Todos vieram resolver. Mas nem todos foram capazes."
for padrao in padroes:
   print("Analisando padrao " + padrao + " " + str(re.findall(padrao, frase_teste)))

padroes = [r"\d+", r"\D+", r"\s+", r"\S+", r"\w+", r"\W+"]
frase_teste = "O número de carros é de 100 unidades. Nesse caso será utilizado a hashtag #100unidades."
for padrao in padroes:
    print("Analisando padrao " + padrao + " " + str(re.findall(padrao, frase_teste)))

padrao = r"\d{2}/\d{2}/\d{4}"
texto = "10/04/2018"
print("Analisando padrao " + padrao + " " + str(re.findall(padrao, texto)))

padrao = r"(\d{2})/(\d{2})/(\d{4})"
padrao = re.search(padrao, texto)
if padrao is not None:
    print("Match %s, dia %s, mês %s e ano %s"%(padrao.group(0), padrao.group(1), padrao.group(2), padrao.group(3)))

print()