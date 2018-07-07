from collections import Counter

texto = "As Duas Torres é a Segunda parte da grande obra de ficção fantástica de J. R. R. Tolkien, O Senhor dos Anéis. É impossível transmitir ao novo leitor todas as qualidades e o alcance do livro. Alternadamente cômica, singela, épica, monstruosa e diabólica, a narrativa desenvolve-se em meio a inúmeras mudanças de cenários e de personagens, num mundo imaginário absolutamente convincente em seus detalhes. Nas palavras do romancista Richard Hughes, ´quanto à amplitude imaginativa, a obra praticamente não tem paralelos e é quase igualmente notável na sua vividez e na habilidade narrativa, que mantêm o leitor preso página após página´."
palavras = texto.split(" ")
count = Counter(palavras)

print(count.most_common(10))