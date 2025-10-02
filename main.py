import os
import time as t
import random as rd
from random import randrange as rand
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

campo = []
bola = []
jgc = 0
jg = 0

def main():
	global campo
	clear()
	print('***** Quebra Cabeca das Bolas Numeradas *****')
	print('Organize os numeros iguais na mesma linha para vencer')
	demo(5,2)
	input('\n\tPressione qualquer tecla para continuar...')

	print(f'''
	Escolha o nivel de dificuldade :

	[1]. Nivel 1
	[2]. Nivel 2
	[3]. Nivel 3
''')
	try:
		dif = int(input(' ~> '))
	except:
		print('\nNao e um numero, tente novamente')
		t.sleep(2)
		main()

	if dif == 1:
		nf, nfv = 5,2
	elif dif == 2:
		nf, nfv = 6,2
	elif dif == 3:
		nf, nfv = 7,2
	else:
		print('\nNivel inexistente')
		t.sleep(2)
		main()

	carregarNivel(nf,nfv)
	while True:
		exibir(campo)
		campo = jogabilidade(nf,nfv)


def carregarNivel(nf,nfv):
	global campo, bola
	nfc = nf - nfv
	nBola = nfc * 4

	# preencher bolas padrao
	for i in range(nfc):
		for j in range(4):
			bola.append(i)
	# misturar bolas
	rd.shuffle(bola)

	# distribuir bolas no campo
	for i in range(nf):
		aux = []
		if i < nfc:
			for j in range(4):
				ult = bola.pop()
				aux.append(ult)
		campo.append(aux)
	return campo

# exibir bolas no campo
def exibir(campo):
	clear()
	print()
	for i in range(len(campo)):
		frasco = ' '.join(map(str,campo[i]))
		print(f'''\t[{i+1}] {frasco}''')

def demo(nf,nfv):
	# carregar
	bolaDemo = []
	campoDemo = []
	nfc = nf - nfv
	print('\n\n')

	for i in range(nf):
		aux = []
		if i < nfc:
			for j in range(4):
				aux.append(i)
		else:
			for j in range(4):
				aux.append(' ')
		campoDemo.append(aux)

	# exibir
	for i in range(len(campoDemo)):
		frasco = ' '.join(map(str,campoDemo[i]))
		print(f'''\t[{i+1}] {frasco}''')


def jogabilidade(nf,nfv):
	global campo, jg, jgc

	verificarVitoria(nf,nfv, jg, jgc)

	# permitir jogada
	print('\nInsira o numero de Origem e de Destino')

	try:
		o, d = input(' ~> ').split()
		o, d = int(o), int(d)
		o, d = o-1, d-1

		if o >= nf or d >= nf:
			print('\n\tFrasco Inexistente')

		elif len(campo[o]) == 0:
			print('\n\tFrasco de Origem Vazio !!!')

		elif len(campo[d]) > 3:
			print('\n\tFrasco de Destino Cheio !!!')

		else:
			aux = campo[o].pop()
			campo[d].append(aux)
			jgc += 1
	except:
		print('\n\tMovimento Invalido')

	jg += 1
	t.sleep(1)
	return campo

def verificarVitoria(nf,nfv,jgc,jg):
	global campo
	contar = 0
	nfc = nf - nfv

	for i in range(nf):
		if len(campo[i]) == 4:
			iguais = any(campo[i].count(x) > 3 for x in campo[i])
			if iguais == True:
				contar += 1
	if contar == nfc:
		jge = jg - jgc
		porc = round((jgc / jg) * 100,2)
		print(f'''
|---| Vitoria |---|
  |      |      |
  |      |      |
   ------ ------
         |   {jgc} Jogadas Corretas
         |   {jge} Jogadas Erradas
        / \\ {porc} % Precisao de movimentos
       /   \\
      /     \\
''')
		exit()

# Inicio do programa
main()


