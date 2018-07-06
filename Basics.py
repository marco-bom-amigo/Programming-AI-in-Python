from bs4 import BeautifulSoup
import requests
import random

nome = "José da Silva"
idade = 30
pi = 3.1415
print(nome + " " + str(30))
print("Valor de pi = %s" %(pi))
print("Valor de pi = %1.2f" % (pi))

print("O primeiro valor é %s, o segundo %s e o terceiro %s" %(1, 2, 3))

print("Documento: {a}, Processo: {a}".format(a="processado"))
print("Documento: {a}, Processo: {b}".format(a="processado", b="erro"))

str = "Hello, Python!!"
print(str.lower())
print(str.upper())
print(str.isdigit())
print(str.splitlines())

if True:
    print("Verdadeiro...!")
a = 10
if a >= 10:
    print("a >= 10")

lista=range(1,10)
for item in lista:
    print(item)

parada = 10
inicio = 0
while parada > 0:
    print(parada)
    parada -= 1

parada = 10
inicio = 0
while parada > 0:
    print(parada)
    parada -= 1
    if parada == 3:
        break
    elif parada ==4:
        continue
    else:
        pass
else:
    print("final")

def menor_numero(num_list):
    num = num_list[0]
    for item in num_list:
        if item < num:
            num = item
        return num

def numero_par(num):
    resto = num % 2
    if resto == 0:
        return True
    else:
        return False

def repete_valor(lista, num=2):
    return lista * num

print(menor_numero([0,1,2,3]))
print(numero_par(4))
print(repete_valor([0,1,2,3], 2))

lista_palavras = []
for palavra in "paralelepípedo":
    lista_palavras.append(palavra)
print(lista_palavras)

lista_palavras_2 = [print(palavra) for palavra in "paralelepípedo"]

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_numeros_2 = [num * 100 for num in lista_numeros]
print(lista_numeros_2)

lista_numeros_pares = [num for num in lista_numeros if num % 2 == 0]
print(lista_numeros_pares)

var = "marco antonio bonamichi junior"
import string
print(string.capwords(var))

url = "http://www.uol.com.br"
response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")
print(response.content)
print(soup.text)

def verifica_numero_impar(numero):
    resto = numero % 2
    if resto == 0:
        print("\nNúmero %s é par" %numero)
        return False
    else:
        print("\nNúmero %s é ímpar" %numero)
        return True

verifica_numero_impar(10)
verifica_numero_impar(11)

f = 1.3
ll = [1.2232, 2.322, 43.2313, 6.34324, 78.3243]

l_rounded = []
for num in ll:
    l_rounded.append(round(num, 2))
print(l_rounded)

l_rounded = []
l_rounded = [round(num,2) for num in ll]
print(l_rounded)

lista_rand = random.sample(range(0,10000), 10000)


def min_max_media(lista):
    min = lista[0]
    max = lista[1]
    soma = 0
    for item in lista:
        soma += item
        if item > max:
            max = item
        if item < min:
            min = item
    media = soma / len(lista)
    return min, max, media
print(min_max_media(lista_rand))

texto = "Esta história cresceu conforme foi sendo contada, até se tornar uma história da Grande Guerra do Anel, incluindo muitas passagens da história ainda mais antiga que a precedeu. O conto foi iniciado logo depois que o Hobbit foi escrito e antes de sua publicação, em 1937; mas não continuou nessa seqüência, pois eu queria primeiro completar e colocar em ordem a mitologia e as lendas dos Dias Antigos, que já vinham tomando forma havia alguns anos. Quis fazer isso para minha própria satisfação, e tinha alguma esperança de que outras pessoas ficassem interessadas nesse trabalho, especialmente por ser ele fruto de uma inspiração primordialmente lingüística, e por ter sido iniciado a fim de fornecer o pano de fundo “histórico” necessário para as línguas élficas."


def obter_info_texto(texto):
    palavras = [palavra for palavra in texto.split(" ") if palavra.isalpha()]
    numeros  = [palavra for palavra in texto.split(" ") if palavra.isdigit()]
    frases   = [palavra for palavra in texto.split(".")]
    retorno = {"palavras": [len(palavras), palavras], "numeros": [len(numeros), numeros], "frases": [len(frases) - 1, frases]}
    return retorno
print(obter_info_texto(texto))
