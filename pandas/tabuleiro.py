import numpy as np

def is_par(numero):
    return numero % 2 == 0

def gerar_tabuleiro(matrix):
    for idx, linha in enumerate(matrix):
        for idy, coluna in enumerate(linha):
            if is_par(idx) and is_par(idy):
                matrix[idx, idy] = 0
            if not is_par(idx) and not is_par(idy):
                matrix[idx, idy] = 0

tabuleiro = np.ones([6,6])
gerar_tabuleiro(tabuleiro)

print(tabuleiro)
np.savez("tabuleiro.npz", x=tabuleiro)

