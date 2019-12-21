# -*- coding: utf-8 -*-

from jogador import Jogador

def printAtual():
	print('--------------------------')
	print('Atual')
	print('--------------------------')

def main():
	jog1 = Jogador()
	jog1.digitaNome()

	jog2 = Jogador()
	jog2.digitaNome()

	jog1.adicionaVitoria()
	jog1.adicionaVitoria()

	printAtual()
	jog1.printJogador()
	jog2.printJogador()

	jog1.adicionaVitoria()
	jog1.adicionaVitoria()

	printAtual()
	jog1.printJogador()
	jog2.printJogador()

main()