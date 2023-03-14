import random

def jogar():

    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1,101)
    quantidade_chutes = 0
    pontos = 1000

    print("Qual é a dificuldade?")
    print("(1) Fácil, (2) Médio, (3) Difícil")
    nivel_dificuldade = int(input("Defina o Nível "))

    if nivel_dificuldade == 1:
        quantidade_chutes = 20
    elif nivel_dificuldade == 2:
        quantidade_chutes = 10
    else:
        quantidade_chutes = 5

    print("Você tem {} pontos".format(pontos))
    print("Numero secreto {}".format(numero_secreto))

    while quantidade_chutes > 0:
        print("tentativa {} \n".format(quantidade_chutes))

        chute = int(input("Digite o seu número de 1 a 100: "))
        acertou = chute == numero_secreto
        maior = chute > numero_secreto

        if chute < 1 or chute > 100:
            print("Use número de 1 a 100\n")
            continue

        if acertou:
            print("Acertou!")
            print("Você terminou com {} pontos".format(pontos))
            break
        else:
            quantidade_chutes -= 1
            if maior:
                print("O numero secreto é menor que o seu chute")
            else:
                print("O numero secreto é maior que o seu chute")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    if quantidade_chutes == 0:
        print("Você perdeu o jogo, o número secreto {}".format(numero_secreto))

    print("********************************")
    print("Fim do jogo de adivinhação")
    print("********************************")

if(__name__ == "__main__"):
    jogar()