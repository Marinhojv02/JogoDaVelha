from comandos import *

matriz=cria_matriz()

turno = 1

while turno <= 9:
    if turno == 9:
        print("O jogo empatou")
        break
    else:
        movimento = jogada()
        executa_jogada(turno, matriz,movimento[0],movimento[1])
        print("turno: {}".format(turno))
        for i in range(3):
            print(matriz[i])
        if verifica_fim(matriz) == 1:
            print("X ganhou")
            break
        elif verifica_fim(matriz) == 2:
            print("O ganhou")
            break
        turno+=1