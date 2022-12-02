# Historias Locas

print("Ha empezado un apocalipsis zombi")

lugar = input("Donde se encuentra usted?: ").upper()
arma = input("Que objeto de su alerededor puede utilizar para defenderse: ").upper()
compañero = input("Quien lo acompaña?: ").upper()

#Historia

print(f"Cuando estabas en {lugar} traquilamente lo ataca un zombi \nintenta defenderse con {arma} pero el zombi es mas fuerte \njusto antes de que lo muerda entra {compañero} y lo salva y \nambos huyen")

#Toma de desiciones

print("Hacia que lugar escapan: a. hospital b.cominasaria")
huida = input(str())
if huida == "a":
	print(f"{compañero} lo traiciona y te mato con tu {arma}")
elif huida == "b": 
	print(f"matas {compañero} con tu {arma} y te lo comes")
else:
	print("No eligio ninguna de las opciones")