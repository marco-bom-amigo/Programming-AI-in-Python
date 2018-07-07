import numpy as np

archive = np.load("tabuleiro.npz")
tabuleiro = archive['x']
print(tabuleiro)

def eliminar(matrix, posicao):
    if matrix[posicao] == 1 or matrix[posicao] == 3 :
        matrix[posicao] = 0
    else:
        matrix[posicao] = 1

def movimentar(matrix, posicao, valor):
    if matrix[posicao] == 1:
        matrix[posicao] = valor + 1
    else:
        matrix[posicao] = valor


movimentar(tabuleiro, (0, 0), 1)
print(tabuleiro)

movimentar(tabuleiro, (1, 1), 3)
print(tabuleiro)

movimentar(tabuleiro, (2,2), 1)
eliminar(tabuleiro, (1,1))
print(tabuleiro)
