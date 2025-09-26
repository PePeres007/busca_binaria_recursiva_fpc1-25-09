def busca_binaria(lista, alvo, quant_comp=0):
	inicio = 0
	fim = len(lista) - 1
	quant_comp += 1
	if inicio <= fim:
		meio = (inicio + fim + 1) // 2
		if lista[meio] == (alvo):
			print(quant_comp)
			return (meio, quant_comp)
		elif lista[meio] < alvo:
			inicio = meio + 1
		else:
			fim = meio - 1
		return busca_binaria(lista[inicio:fim+1], alvo, quant_comp)
	else:
		print(quant_comp)

lista = list(input().split(" "))
alvo = lista.pop(0)
busca_binaria(lista,alvo)
