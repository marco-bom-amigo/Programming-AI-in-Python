from random import randrange

numero_secreto = randrange(0,11)

def check_hunt(num, num_secreto):
    if num == num_secreto:
        print("Parabéns, o número secreto é %s"%num_secreto)
        return True
    elif num > num_secreto:
        print("O número secreto é menor")
    else:
        print("O número secreto é maior")
    return False

acertou = False

while acertou == False:
    try:
        hunch = int(input("Entre com seu palpite "))
        acertou = check_hunt(hunch, numero_secreto)
    except:
        print("Entre com um número válido")