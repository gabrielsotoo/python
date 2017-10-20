class hola(object):
	def metodo1(x):
		arreglo = x
		j = 0
		arreglo2 = []		#declaro arreglo2 como lista
		i = len(arreglo) 	#variable i tiene el valor del largo de ese array
		while(j<len(arreglo)):			#el ciclo ira hasta que j no sea menor que el largo del arreglo
			i-=1
			arreglo2.append(arreglo[i]) 		#agrega valores de arreglo a arreglo2
			j+=1
			print(arreglo2)			#imprime cadena valor por valor
			print(arreglo)			#imprime cadena total 
		if (arreglo2 == arreglo):	#compara entre dos arreglos
			a = True
		else:
			a = False		
		return a

	def metodo2(x):
		return x

print (hola.metodo1(['1','2','2','1']))
print (hola.metodo2('mi nombre es Gabriel Soto'))