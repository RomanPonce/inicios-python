# Numero aleatoria
import random

jugador = input("Elige un numero de 1 al 5:")
humano = int(jugador)
pc = random.randint(1, 5)

if pc == humano:
	print(f"Resultado: {pc}, {humano}")
	print("ganaste")
elif pc < humano:
	print(f"Resultado: {pc}, {humano}")
	print("Tu numero es mas grande")
elif pc > humano:
	print(f"Resultado: {pc}, {humano}")
	print("Tu número es mas chico")
else:
	print("No es un número")	
	pass
