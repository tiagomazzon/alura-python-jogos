
def jogar():
    print("***************************")
    print("Bem vindo ao jogo de Forca!")
    print("***************************")

    palavra_secreta = "laranja".upper()
    letras_acertadas = ["_","_","_","_","_","_","_"]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    #enquanto não enforcou e não acertou
    while(not enforcou and not acertou):

        chute = input("Qual letra?").strip().upper()

        if(chute in palavra_secreta):

            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    #print("Encontrei a letra {} na posição {}".format(letra, index))
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        #uso de count
        letras_faltando = str(letras_acertadas.count('_'))
        print('Ainda faltam acertar {} letras'.format(letras_faltando))

    if(acertou):
        print("Você ganhou!!!")
    else:
        print("Você perdeu!!!")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()