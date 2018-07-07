class Livro(object):

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas

    def __del__(self):
        print("Objeto apagado")

livro = Livro("Python", "José da Silva", 432)

print(livro)
print(len(livro))
del(livro)