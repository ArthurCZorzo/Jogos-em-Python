# usar uma hierarquia onde o programa le os resultados da procura e caso joga em uma array
# verde > amarelo > vermelho

palavra1 = ["p","o","r","t","a"]
palavra2 = ["g","r","a","t","o"]

def compara_listas(lista1,lista2):
    for x in lista1:
        print("Letra da vez é {}\n".format(x))
        indexDoX = lista1.index(x)
        for y in range(0,5):
            if(indexDoX == y and x == lista2[y]):
                print("🟩")
            elif(x == lista2[y]):
                print("🟨")
            else:
                print("🟥")


print(compara_listas(palavra2,palavra1))