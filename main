def busca_binaria(lista, alvo, qtdeComparacoes=0):
	inicio = 0
	fim = len(lista) - 1
	qtdeComparacoes += 1
	if inicio <= fim:
		meio = (inicio + fim + 1) // 2
		if lista[meio] == (alvo):
			print(qtdeComparacoes)
			return (meio, qtdeComparacoes)
		elif lista[meio] < alvo:
			inicio = meio + 1
		else:
			fim = meio - 1
		return busca_binaria(lista[inicio:fim+1], alvo, qtdeComparacoes)
	else:
		print(qtdeComparacoes)


lista = list(input().split(" "))
alvo = lista.pop(0)
busca_binaria(lista,alvo)
