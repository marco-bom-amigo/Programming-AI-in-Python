from random import randrange

lista = range(1,10001)
lista_rand = list(map(lambda x: randrange(0,10001), lista))

def is_par_mod(num):
    resto = num % 2
    if resto != 0 and num < 12:
        return True
    else:
        return False

lista_impar_mod = filter(is_par_mod, lista_rand)

print(set(lista_impar_mod))