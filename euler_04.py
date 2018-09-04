# Encontrar o maior palindrome produto da multiplicação 
# de números com 3 dígitos

def encontra_palindrome():
	a = 999
	b = range(100, a) # range(100,999) 
	palindromes = []
	while a > 100:
		for n in b:
			num = a * n
			num = str(num)
			if(num == num[::-1]):
				num = int(num)
				palindromes.append(num)
		a -= 1
	
	print(max(palindromes))

encontra_palindrome()

#assert encontra_palindrome() == 9009
	
#A  x    B
#99 x [99,98,97,96,95,94,93,92,91,90]
#90 x [89,88,87,86,85,84,83,82,81,80]
#80 x [79,78,77,76,75,74,73,72,71,70]

#Multiplicar um número por uma lista de valores
#Quando acabar, fator A recebe novo valor e B recebe nova lista
#Verificar se há palindromes
#999 x ~ 100
#998 x ~ 100