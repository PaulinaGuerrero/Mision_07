# Autor: Paulina Guerrero Ruiz
# calcula las  divisones y encuentra el numero mayor

def encontrarMayor() :
	numero = 0
	mayor = -1
	while numero != -1:
		numero = int(input(" Teclea un numero [-1 si deseas terminar: "))
		if numero >= mayor :
			mayor = numero
	if mayor == -1 :
		print(" No hay valor mayor")
	else :
		print(' El mayor es: %d'%(mayor))


def dividir(dividendo, divisor) :
	cociente = 0
	residuo = dividendo
	while residuo >= divisor :
		cociente += 1
		residuo = residuo - divisor
	print(' %d / %d = %d, sobra %d'%(dividendo, divisor, cociente, residuo))


def main() :
	opcion = int(input(" Teclea tu numero: "))
	if opcion == 1 :
		print("\n Calculando divisiones")
		dividendo = int(input(" Dividendo: "))
		divisor = int(input(" Divisor: "))
		dividir(dividendo, divisor)
		input(" Presione enter para continuar...")
		main()
	elif opcion == 2 :
		print("\n Teclea números en serie: ")
		encontrarMayor()
		input("Continuar...")
		main()
	elif opcion == 3 :
		print("\n Exit")
		exit(0)
	else :
		print(" ERROR, teclea unicamente los numeros 1, 2 o 3")
		main()


main()