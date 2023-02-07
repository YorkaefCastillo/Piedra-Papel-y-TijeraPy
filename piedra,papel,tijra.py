#
import random
#Titulo
Ador = ""
Titulo = "Piedra, Papel, Tijera"
print(f"{Ador.center(50,'*')}")
print(f"{Titulo.center(50).upper()}")
print(f"{Ador.center(50,'*')}")

print("Hola 🖐")
#Bloque donde la maquina compite con tigo para ver quien saca la evaluacion de quien gana 
def adivina():
    
        usuario = input("Escoge entre piedra papel o tijera: ") 
        x = random.choice(["PIEDRA", "PAPEL", "TIJERA"])
        if (x == "PIEDRA" and usuario.upper() == 'PAPEL') or (x == 'PAPEL' and usuario.upper() == 'TIJERA') or (x == 'TIJERA' and usuario.upper() =='PIEDRA'):
            print(f"Felicidades me ganaste con {usuario.title()} yo saque {x.title()}\n")
        elif usuario.upper() == x:
            print("Empate sacamos lo mismo 😅\n")
        else:
         print(f"Te gane con {x.title()} tu sacaste {usuario.title()}\n")
        
        #Bloque donde preguntar si quiere jugar de nuevo 
         
while True:
    adivina()
    print(f"{Ador.center(50,'_')}")
    SN = input("Quiere jugar otra ves S/N: ")
    if  SN.upper() == "S":
        continue
    else:
        break
