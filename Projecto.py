respuesta = input("¡Bienvenido compa! Estamos en Costa Rica fijo ud esta como yo....¿Te explico las reglas del tenis? (sí/no): ")

if respuesta.lower() == "sí" or respuesta.lower() == "si":
    print("Puntos: El sistema de puntuación del tenis se basa en una secuencia de puntos: 15, 30, 40 y juego. Al inicio del juego, ambos jugadores tienen 0 puntos, que se denomina love Cuando un jugador gana el primer punto, su puntuación se cambia a 15. Si ganan otro punto, su puntuación se cambia a 30. Si ganan otro punto más, su puntuación se cambia a 40. Si el jugador gana otro punto y ya tenía 40, gana el juego.")

print("Continuemos con el resto del programa...")

Jugador_1 = input("Nombre del jugador 1: ")
print(Jugador_1)

opcion = input("¿Deseas jugar contra otro jugador o contra la computadora, presione 1 para jugador, 2 para computadora (1/2): ")
if opcion.lower() == "jugador":
    Jugador_2 = input("Nombre del jugador 2: ")
else:
    Jugador_2 = "computadora"

print(Jugador_2)

print("La épica pelea de " + Jugador_1 + " y " + Jugador_2 + " dará inicio")

Sistema_de_Puntos = [15,30,40]
for i in range(len(Sistema_de_Puntos)):
    