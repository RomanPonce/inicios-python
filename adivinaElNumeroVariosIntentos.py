import random


def el_numero_adivinar(x):

	
	print("==========================================")
	print("El juego consiste en tratar de adivinar el \nnumero que eliga la computadora. Si lo haces \nganas, si no pierdes.")
	print("==========================================")

	pc = random.randint(1, x) # Número aleatorio entre uno y cinco
	humano = 0

	while humano != pc:
		try:
			humano = int(input(f"Elige un numero de 1 al {x}: "))
		except:
			print("NO ES UN NUMERO")
		if humano == 0:
			print("*********************")
			print(f"Intentelo nuevamente")
			print("*********************")
		elif pc < humano:
			print(f"Intenta de nuevo, {humano} es mas mayor")
		elif pc > humano:
			print(f"Intenta de nuevo, {humano} es mas menor")
	
	print(f"Ganaste adivinaste número. {pc}")


el_numero_adivinar(10)