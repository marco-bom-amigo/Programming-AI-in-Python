from Corpus import Corpus

class CorpusEnhanced(Corpus):

    def __init__(self, lista_texto):
        Corpus.__init__(self, lista_texto)

    def converter_minusculas(self):
        count_word = lambda x: x.lower()
        Corpus.set_lista_texto(self, list(map(count_word, lista)))

    def mostrar_textos(self):
        for item in Corpus.get_lista_texto(self):
            print(item)

lista = ["DSDDSA dsada dsada das", "dsad dsa dsa dsa das"]

corpus = CorpusEnhanced(lista)
corpus.inserir_texto("Teste de texto")
print(corpus)

corpus.mostrar_textos()
corpus.converter_minusculas()
corpus.mostrar_textos()