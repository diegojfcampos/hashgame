
#HASH GAME

"Globals"

tabuleiro = [0, 0, 0, 0, 0, 0, 0, 0, 0]
posicao = 0
jogo = True
jogador = 1
jogadas = 9

"""IMPORT´s"""


"""Def's"""

def printTabuleiro(tabuleiro):
    print("---TABULEIRO---")
    tab = ""
    for i in range(0, 9):
        mark = " "
        if tabuleiro[i] == 1:
            mark = "X"
        elif tabuleiro[i] == -1:
            mark = "0"
        tab += " | " + mark

        if i == 2 or i == 5 or i == 8:
            print(tab + " | ")
            tab = ""
    print("---------------")


def restart(reinicia):
                global tabuleiro
                global posicao
                global jogo
                global jogador
                global jogadas

                tabuleiro[0:9] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                posicao = 0
                jogo = True
                jogador = 1
                jogadas = 9
                print("==============")
                print("GAME RESTARTED")
                print("==============")
                printTabuleiro(tabuleiro)



def teste(teste):
            soma1 = tabuleiro[0] + tabuleiro[1] + tabuleiro[2]
            soma2 = tabuleiro[3] + tabuleiro[4] + tabuleiro[5]
            soma3 = tabuleiro[6] + tabuleiro[7] + tabuleiro[8]
            soma4 = tabuleiro[0] + tabuleiro[4] + tabuleiro[8]
            soma5 = tabuleiro[2] + tabuleiro[4] + tabuleiro[6]
            soma6 = tabuleiro[0] + tabuleiro[3] + tabuleiro[6]
            soma7 = tabuleiro[1] + tabuleiro[4] + tabuleiro[7]
            soma8 = tabuleiro[2] + tabuleiro[5] + tabuleiro[8]

            if soma1 == 3 or soma2 == 3 or soma3 == 3 or soma4 == 3 or soma5 == 3 or soma6 == 3 or soma7 == 3 or soma8 == 3:
                print("JOGADOR 1 VENCEU")
                restart(tabuleiro)
            elif soma1 == -3 or soma2 == -3 or soma3 == -3 or soma4 == -3 or soma5 == -3 or soma6 == -3 or soma7 == -3 or soma8 == -3:
                print("JOGADOR 2 VENCEU")
                restart(tabuleiro)



def empate(empate):
                soma1 = tabuleiro[0] + tabuleiro[1] + tabuleiro[2]
                soma2 = tabuleiro[3] + tabuleiro[4] + tabuleiro[5]
                soma3 = tabuleiro[6] + tabuleiro[7] + tabuleiro[8]
                soma4 = tabuleiro[0] + tabuleiro[4] + tabuleiro[8]
                soma5 = tabuleiro[2] + tabuleiro[4] + tabuleiro[6]
                soma6 = tabuleiro[0] + tabuleiro[3] + tabuleiro[6]
                soma7 = tabuleiro[1] + tabuleiro[4] + tabuleiro[7]
                soma8 = tabuleiro[2] + tabuleiro[5] + tabuleiro[8]

                if soma1 != 0 and soma1 > -3 and soma1 < 3:
                    if soma2 != 0 and soma2 > -3 and soma2 < 3:
                        if soma3 != 0 and soma3 > -3 and soma3 < 3:
                            if soma4 != 0 and soma4 > -3 and soma4 < 3:
                                if soma5 != 0 and soma5 > -3 and soma5 < 3:
                                    if soma6 != 0 and soma6 > -3 and soma5 < 3:
                                        if soma7 != 0 and soma7 > -3 and soma5 < 3:
                                            if soma8 != 0 and soma8 > -3 and soma5 < 3:
                                                print("EMPATE")
                                                restart(tabuleiro)



#JOGO

while jogo == True:
        teste(tabuleiro)
        if jogador == 1:
            print("JOGADOR 1")
        else:
            print("JOGADOR 2")
        posicao = int(input("Digite a posição de 0 a 8: "))
        if posicao < 0 or posicao > 8:
            print("Posição inválida, digite de 1 a 9.")
        elif tabuleiro[posicao] == 1 or tabuleiro[posicao] == -1:
            print("Posicão Indisponível, tente outra opção entre 0 a 8.")
        else:
            if jogador == 1 and tabuleiro[posicao] == 0:
                tabuleiro[posicao] = 1
                printTabuleiro(tabuleiro)
                jogador = -1
                teste(tabuleiro)
                empate(empate)

            if jogador == -1 and tabuleiro[posicao] == 0:
                tabuleiro[posicao] = -1
                printTabuleiro(tabuleiro)
                jogador = 1
                teste(tabuleiro)
                empate(empate)









