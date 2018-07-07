from random import randrange
import functools

lista = range(1,501)
list(lista)[0], list(lista)[-1]
lista_rand = list(map(lambda x: randrange(0,50001), lista))

max_value = functools.reduce(lambda x, y: x if x > y else y, lista_rand)
print(max_value)

min_value = functools.reduce(lambda x, y: x if x < y else y, lista_rand)
print(min_value)

menor = lista_rand[0]
maior = lista_rand[0]

for item in lista_rand:
    if item < menor:
        menor = item
    if item > maior:
        maior = item
print(maior, menor)