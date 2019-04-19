# Encontra e soma todos os numeros pares da 
# sequencia de fibonacci até o limite de 4000000

def encontra_fib():
	seq = [1,2]
	limite = 4000000
	while (seq[-1] <= limite):
		soma = seq[-1] + seq[-2]
		if (soma < limite):
			seq.append(soma)
		else:
			return seq
	
seq = encontra_fib()

def encontra_pares(seq):
	pares = []
	for indice in seq:
		if (indice % 2 == 0 ):
			pares.append(indice)
	print(pares)
	return pares


pares = encontra_pares(seq)

def soma(pares):
	soma = 0
	for par in pares:
		soma += par
	return soma
	 
soma = soma(pares)
print ("Soma = " + str(soma))

	