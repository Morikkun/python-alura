print("////////////////////////////////////////")
print("Bem vindo ao jogo da adivinhação mortal")
print("////////////////////////////////////////")

numero_secreto = 98
limite_tentativas = 3;
rodada = 1
for rodada in range(1, limite_tentativas + 1 ):
    print("Prepare-se para jogar, você tem 3 tentataivas para acerter o número, mortal")
    print("------------------------------------------------------------------------------")
    print("Tentativa {} de {}".format(rodada, limite_tentativas))

    chute = int(input("Digite um número: "))
    print("Você digitou ", chute)
    acerto = chute == numero_secreto
    alto_demais = chute > numero_secreto
    baixo_demais = chute < numero_secreto

    if(acerto):
        print("Parabéns, mortal, você acertou e viverá mais um dia")
        break
    else:
        if(alto_demais):
            print("Seja menos ambicioso, chute mais baixo")
        elif(baixo_demais):
            print("Seja mais ambicioso, seu chute foi muito baixo")


print("Fim do jogo, mortal")