# -*- coding: utf-8 -*-

class Jogador:

	def __init__(self):
		self.nome = ''
		self.vitorias = 0

	def digitaNome(self):
		self.nome = raw_input('Digite o Nome do Jogador: ')

	def adicionaVitoria(self):
		self.vitorias += 1

	def printJogador(self):
		print ''
		print 'Jogador: ', self.nome
		print 'Vitorias: ', self.vitorias