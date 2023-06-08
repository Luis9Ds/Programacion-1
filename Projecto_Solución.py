import random

respuesta = input("¡Bienvenido compa! Estamos en Costa Rica, fijo que tú también... ¿Te explico las reglas del tenis? (sí/no): ")

if respuesta.lower() == "sí" or respuesta.lower() == "si":
    print("Puntos: El sistema de puntuación del tenis se basa en una secuencia de puntos: 15, 30, 40 y juego. Al inicio del juego, ambos jugadores tienen 0 puntos, que se denomina 'love'. Cuando un jugador gana el primer punto, su puntuación se cambia a 15. Si ganan otro punto, su puntuación se cambia a 30. Si ganan otro punto más, su puntuación se cambia a 40. Si el jugador gana otro punto y ya tenía 40, gana el juego.")

print("Continuemos con el resto del programa...")

Jugador_1 = input("Nombre del jugador 1: ")
Jugador_2 = input("Nombre del jugador 2: ")

print(Jugador_1)
print(Jugador_2)

print("¡La épica pelea de " + Jugador_1 + " y " + Jugador_2 + " dará inicio!")

puntajes = {Jugador_1: 0, Jugador_2: 0}

modo_juego = input("¿Deseas jugar manualmente o que la computadora seleccione aleatoriamente los puntos? (manual/computadora): ")

while True:
    print("\nPuntajes:")
    print(f"{Jugador_1}: {puntajes[Jugador_1]}")
    print(f"{Jugador_2}: {puntajes[Jugador_2]}")
    
    if puntajes[Jugador_1] == 40 and puntajes[Jugador_2] == 40:
        print("Deuce")
    elif puntajes[Jugador_1] == "advantage":
        print("Ventaja para " + Jugador_1)
    elif puntajes[Jugador_2] == "advantage":
        print("Ventaja para " + Jugador_2)
        
    ganador = None
    if puntajes[Jugador_1] == "Juego":
        ganador = Jugador_1
    elif puntajes[Jugador_2] == "Juego":
        ganador = Jugador_2
    
    if ganador:
        print("\n¡" + ganador + " ha ganado el juego!")
        break
    
    if modo_juego.lower() == "manual":
        print("\n¿A quién le gustaría otorgarle el punto?")
        jugador = input("Ingrese '1' para " + Jugador_1 + " o '2' para " + Jugador_2 + ": ")
        
        if jugador == '1':
            jugador = Jugador_1
        elif jugador == '2':
            jugador = Jugador_2
        else:
            print("Opción inválida. Por favor, ingrese '1' o '2'.")
            continue
    elif modo_juego.lower() == "computadora":
        jugador = random.choice([Jugador_1, Jugador_2])
        print("La computadora otorga el punto a: " + jugador)
    else:
        print("Modo de juego inválido. Por favor, ingrese 'manual' o 'computadora'.")
        continue
    
    if puntajes[jugador] == 40 and puntajes[jugador] != "advantage":
        puntajes[jugador] = "Juego"
    elif puntajes[jugador] == "advantage":
        puntajes[jugador] = 0
    elif puntajes[jugador] == 30:
        puntajes[jugador] = 40
    elif puntajes[jugador] == 15:
        puntajes[jugador] = 30
    elif puntajes[jugador] == 0:
        puntajes[jugador] = 15
    else:
        puntajes[jugador] += 15
