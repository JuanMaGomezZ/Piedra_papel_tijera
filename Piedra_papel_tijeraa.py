# PIERDA PAPEL O TIJERA

print(chr(27) + "[34m" + "\nBienvenido al tradicional juego de piedra papel o tijeras!") # Cartel de bienvenida

reglas = int(input("\nPresione: \n\t1- Reglas \n\t2- Continuar al juego \n\tRespuesta: ")) #Nos da a elegir si queremos ver las reglas del juego


if reglas == 1:
    print(" \nREGLAS: Un juego de manos en el que existen tres elementos: la piedra que vence a la tijera rompiéndola, "
          "la tijera que vence al papel cortándolo y el papel que vence a la piedra       envolviéndola, dando lugar"
          " a un círculo o ciclo cerrado")

modo = int(input("\nPresione: \n\t1- Jugador vs PC \n\t2- Jugador1 vs Jugador2  \n\t3- PC vs PC \n\tRespuesta: "))
# Nos da a elegir la modalidad del juego, si queremos jugar solos vs la pc O entre 2 personas

 # Ingreso de la eleccion de j1


if modo == 1:
    import random
    pc = random.randint(1, 3) # La eleccion aleatoria de la PC
    j1 = int(input("\nJUGADOR1: \n\t1- Piedra \n\t2- Papel \n\t3- Tijera \n\tRespuesta: ")) # Eleccion j1

    # Todas las posibilidades de victoria del jugador1 ante la PC
    if j1 == 1 and pc == 3:
        print(chr(27) + "[32m" + "\nJugador1 = Piedra")
        print(chr(27) + "[31m" + "PC = Tijera")
        print(chr(27) + "[32m" + "Jugador1 Gana")
    elif j1 == 2 and pc == 1:
        print(chr(27) + "[32m" + "\nJugador1 = Papel")
        print(chr(27) + "[31m" + "PC = Piedra")
        print(chr(27) + "[32m" + "Jugador1 Gana")
    elif j1 == 3 and pc == 2:
        print(chr(27) + "[32m" + "\nJugador1 = Tijera")
        print(chr(27) + "[31m" + "PC = Papel")
        print(chr(27) + "[32m" + "Jugador1 Gana")



    #Todas las posibilidades de victoria de la PC ante el jugador1
    elif pc == 2 and j1 == 1:
        print(chr(27) + "[31m" + "\nPC = Piedra")
        print(chr(27) + "[32m" + "Jugador1 = Papel")
        print(chr(27) + "[31m" + "PC Gana")
    elif pc == 3 and j1 == 2:
        print(chr(27) + "[32m" + "\nJugador1 = Papel")
        print(chr(27) + "[31m" + "PC = Tijera")
        print(chr(27) + "[31m" + "PC Gana")
    elif pc == 1 and j1 == 3:
        print(chr(27) + "[32m" + "\nJugador1 = Tijera")
        print(chr(27) + "[31m" + "PC = Piedra")
        print(chr(27) + "[31m" + "PC Gana")

    # Empate
    elif j1 == pc:
        print(chr(27) + "[36m" + "\nEmpate")



# Todas las posibilidades de victoria del Jugador1
if modo == 2:
    j1 = int(input("\nJUGADOR1: \n\t1- Piedra \n\t2- Papel \n\t3- Tijera \n\tRespuesta: ")) # Eleccion j1
    j2 = int(input("\nJUGADOR2: \n\t1- Piedra \n\t2- Papel \n\t3- Tijera \n\tRespuesta: ")) # Eleccion j2
    if j1 == 1 and j2 == 3:
        print(chr(27) + "[32m" + "\nJugador1 = Piedra")
        print(chr(27) + "[31m" + "Jugador2 = Tijera")
        print(chr(27) + "[32m" + "Jugador1 Gana")
    elif j1 == 2 and j2 == 1:
        print(chr(27) + "[32m" + "\nJugador1 = Papel")
        print(chr(27) + "[31m" + "Jugador2 = Piedra")
        print(chr(27) + "[32m" + "Jugador1 Gana")
    elif j1 == 3 and j2 == 2:
        print(chr(27) + "[32m" + "\nJugador1 = Tijera")
        print(chr(27) + "[31m" + "Jugador2 = Papel")
        print(chr(27) + "[32m" + "Jugador1 Gana")

# Todas las posibilidades de victoria del Jugador2
    elif j2 == 2 and j1 == 1:
        print(chr(27) + "[31m" + "\nJugador2 = Piedra")
        print(chr(27) + "[32m" + "Jugador1 = Papel")
        print(chr(27) + "[31m" + "Jugador2 Gana")
    elif j2 == 3 and j1 == 2:
        print(chr(27) + "[32m" + "\nJugador1 = Papel")
        print(chr(27) + "[31m" + "Jugador2 = Tijera")
        print(chr(27) + "[31m" + "Jugador2 Gana")
    elif j2 == 1 and j1 == 3:
        print(chr(27) + "[32m" + "\nJugador1 = Tijera")
        print(chr(27) + "[31m" + "Jugador2 = Piedra")
        print(chr(27) + "[31m" + "Jugador2 Gana")
    elif j1 == j2:
        print(chr(27) + "[36m" + "\nEmpate")
    else:
        print(chr(27) + "[35m" + "\nSu elección es incorrecta")


if modo == 3:
    print(chr(27) + "[33m" + "\nComing soon")
