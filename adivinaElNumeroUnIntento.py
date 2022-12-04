# Numero aleatoria
import random

print("==========================================")
print("El juego consiste en tratar de adivinar el \nnumero que eliga la computadora. Si lo haces \nganas, si no pierdes.")
print("==========================================")

humano = input("Elige un numero de 1 al 5:")
humano = int(humano)
pc = random.randint(1, 5) # Número aleatorio entre uno y cinco

if pc == humano:
	print(f"Resultado: Pc {pc}, Tu {humano}")
	print("ganaste")
elif pc < humano:
	print(f"Resultado: Pc {pc}, Tu {humano}")
	print("Tu numero es mas grande")
elif pc > humano:
	print(f"Resultado: Pc {pc}, Tu {humano}")
	print("Tu número es mas chico")
else:
	print("No es un número")	
	pass
