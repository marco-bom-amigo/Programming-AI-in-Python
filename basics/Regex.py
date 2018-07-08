import re

padroes_positivos = []
padroes_positivos.append("ótimo")
padroes_positivos.append("gostei")
padroes_positivos.append("excelente")
padroes_positivos.append("legal")
padroes_positivos.append("melhor")
padroes_positivos.append("adorei")

padroes_negativos = []
padroes_negativos.append("não")
padroes_negativos.append("confuso")
padroes_negativos.append("ruins")

frases = []
frases.append("O filme foi ótimo, adorei muito.")
frases.append("Não gostei, muito confuso e os atores estavam ruins.")
frases.append("Foi excelente, mas no começo não achei legal.")
frases.append("Poderia ser melhor.")

for frase in frases:
    score = 0
    for padrao in padroes_positivos:
        if re.search(padrao, frase):
            score += 1
    for padrao in padroes_negativos:
        if re.search(padrao, frase):
            score -= 1
    print("%s: análise sentimento %s" % (frase, score))