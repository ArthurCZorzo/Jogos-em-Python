import random

# UMA LETRA DEVE SER COMPARADA COM TODAS AS OUTRAS DA OUTRA PALAVRA SE ELA EXISTER NA PALVRA E ESTIVER NA POSIÇÃO CERTA -> 🟩, SE ELA EXISTIR NA PALAVRA E ESTIVER NA POSIÇÃO ERRADA 🟨, SE NÃO 🟥


def quebrar_palavra(palavra):
    palavra_quebrada = []
    for letra in palavra:
        palavra_quebrada.append(letra)
    return palavra_quebrada


palavras = ["sagaz", "negro", "mexer", "termo", "nobre", "senso", "algoz", "afeto", "plena", "sutil", "fazer"]
numero_aleatorio = random.randint(0,10)
palavra_aleatoria = palavras[numero_aleatorio]

print(palavra_aleatoria)

tentativas = 1
for tentativas in range(6):
    print("Tentativa {} de 5\n".format(tentativas))

    chute = input("Digite uma palavra de 5 letras: ")
    if (len(chute)) != 5:
        print("Usa palavras com 5 letras")
        continue

    if(chute == palavra_aleatoria):
        print("🟩🟩🟩🟩🟩")
        break

    if(quebrar_palavra(chute)[0] == quebrar_palavra(palavra_aleatoria)[0]):
        print("🟩",quebrar_palavra(chute)[0])
    else:
        print("🟥")
    if (quebrar_palavra(chute)[1] == quebrar_palavra(palavra_aleatoria)[1]):
        print("🟩",quebrar_palavra(chute)[1])
    else:
        print("🟥")
    if (quebrar_palavra(chute)[2] == quebrar_palavra(palavra_aleatoria)[2]):
        print("🟩",quebrar_palavra(chute)[2])
    else:
        print("🟥")
    if (quebrar_palavra(chute)[3] == quebrar_palavra(palavra_aleatoria)[3]):
        print("🟩",quebrar_palavra(chute)[3])
    else:
        print("🟥")
    if (quebrar_palavra(chute)[4] == quebrar_palavra(palavra_aleatoria)[4]):
        print("🟩",quebrar_palavra(chute)[4])
    else:
        print("🟥")