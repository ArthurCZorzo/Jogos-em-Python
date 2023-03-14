import forca
import adivinhacao

def escolhe_jogo():
    print("********************************")
    print("Escolha Seu Jogo")
    print("********************************")

    print("(1) Forca (2) Adivinhacao")
    jogo = int(input("Qual Jogo? "))

    if(jogo == 1):
        print("Jogo da forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogo de Adivinhacao")
        adivinhacao.jogar()
    else:
        print("Use 1 ou 2")

if(__name__ == "__main__"):
    escolhe_jogo()