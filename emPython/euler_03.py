# Encontrar o maior fator primo de 600851475143
# Podemos encontrar os fatores da raiz desse numero
# e ver quais são primos para então mostrar o maior

num = 600851475143
def encontra_fator(num):
	raiz = int(num**(0.5)) + 1
	fatores = []
	for n in range(2, raiz):		
		if(num % n == 0):
			fatores.append(n)
	return(fatores) 

fatores = encontra_fator(num)

def encontra_primos(fatores):  # fatores = [5, 7, 13, 29, 35, 65, 91]
	for n in fatores:
		i = 1
		divisores = 0
		while i <= n:
			if(n % i == 0):				
				divisores += 1				
			i += 1
		if (divisores == 2):
			print(n)
			

			

encontra_primos(fatores)


			
