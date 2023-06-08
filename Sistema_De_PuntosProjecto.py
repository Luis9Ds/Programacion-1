Jugador_1 = "Luis"
Jugador_2 = "Kevin"

Sistema_de_Puntos = [15, 30, 40]

Puntaje_Jugador_1 = 0
Puntaje_Jugador_2 = 0

for i in range(len(Sistema_de_Puntos)):
    Pregunta = input("A qué jugador le deseas dar el punto (1/2): ")

    if Pregunta == "1":
        Puntaje_Jugador_1 += Sistema_de_Puntos[i]
        print("Punto para " + Jugador_1 + ".")
        print("Puntos de " + Jugador_1 + ": " + str(Puntaje_Jugador_1))
        print("Puntos de " + Jugador_2 + ": " + str(Puntaje_Jugador_2))
        if Puntaje_Jugador_1 >= 40:
            print("¡Felicidades " + Jugador_1 + "! Has alcanzado 40 puntos.")
            break
    elif Pregunta == "2":
        Puntaje_Jugador_2 += Sistema_de_Puntos[i]
        print("Punto para " + Jugador_2 + ".")
        print("Puntos de " + Jugador_1 + ": " + str(Puntaje_Jugador_1))
        print("Puntos de " + Jugador_2 + ": " + str(Puntaje_Jugador_2))
        if Puntaje_Jugador_2 >= 40:
            print("¡Felicidades " + Jugador_2 + "! Has alcanzado 40 puntos.")
            break

    input("Presiona Enter para continuar.")
