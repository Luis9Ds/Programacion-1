def mostrar_puntaje(puntaje):
    if puntaje == 0:
        return "0"
    elif puntaje == 15:
        return "15"
    elif puntaje == 30:
        return "30"
    elif puntaje == 40:
        return "40"
    elif puntaje == "advantage":
        return "Ventaja"
    else:
        return "Juego"

puntajes = {"Luis": 0, "Diego": 0}

while True:
    print("Puntajes:")
    print(f"Luis: {mostrar_puntaje(puntajes['Luis'])}")
    print(f"Diego: {mostrar_puntaje(puntajes['Diego'])}")
    
    if puntajes['Luis'] == 40 and puntajes['Diego'] == 40:
        print("Deuce")
    elif puntajes['Luis'] == "advantage":
        print("Ventaja para Luis")
    elif puntajes['Diego'] == "advantage":
        print("Ventaja para Diego")
        
    ganador = None
    if puntajes['Luis'] == "Juego":
        ganador = "Luis"
    elif puntajes['Diego'] == "Juego":
        ganador = "Diego"
    
    if ganador:
        print(f"\n¡{ganador} ha ganado el juego!")
        break
    
    print("\n¿A quién le gustaría otorgarle el punto?")
    jugador = input("Ingrese 'Luis' o 'Diego': ")
    
    if jugador not in puntajes.keys():
        print("Jugador inválido. Por favor, ingrese 'Luis' o 'Diego'.")
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
    elif puntajes[jugador] == 40 and puntajes[jugador] == "advantage":
        puntajes[jugador] = "Juego"
    else:
        puntajes[jugador] += 15
