import functools

class Corpus(object):

    def __init__(self, lista_texto):
        self.lista_texto = lista_texto

    def inserir_texto(self, texto):
        self.lista_texto.append(texto)

    def get_lista_texto(self):
        return self.lista_texto

    def set_lista_texto(self, lista_texto):
        self.lista_texto = lista_texto

    def __str__(self):
        count_word = lambda x: len(x.split(" "))
        lista_palavras = list(map(count_word, lista))
        maior_num_palavras = functools.reduce(lambda x, y: x if x > y else y, lista_palavras)
        retorno = "Número de textos %s\nMaior número de palavras %s" % (len(self.lista_texto), maior_num_palavras)
        return retorno

    def __len__(self):
        return len(self.lista_texto)

lista = ["dsada dsada dsada das", "dsad dsa dsa dsa das"]
corpus = Corpus(lista)

len(corpus)
print(corpus)

corpus.inserir_texto("dsa das da das dsa dsa da da das dsa da da dsa da das da das da das dsa")
len(corpus)
print(corpus)