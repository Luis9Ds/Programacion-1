# Funciones
# A veces necesitamos repetir ciertos fragmentos de código y en lugar de escribir nuevamente lo mismo una y otra vez, en programación existe lo que se conocecomo funciones, las mismas las usamos para realizar tareas que se repiten.

def saludo():
    print("hola clase, buenas")
    print("Mi nombre es Oliver Atom")

saludo()

# En ocasioneslas funciones necesitan información específica para realizar las tareas para las cuales fueron programadas, a estos elementos se les conoce como parámetros

def salud2(nombre,apellido):
    print("Hola, espero que estes bien")
    print(nombre)
    print("te apedillas",apellido,"verdad?")
    print("Sera un placer tener a un jugador como tu en el equipo")

nombre = "Steve"
apellido = "Hyuga"

salud2(nombre , apellido)

# Retornos: Una funcion puede devolver un valor al código que la llamo, las funcionaes se escriben para realizar tareas, y a veces es posible que necesitamos el resultado de las tareas, esto se puede hacer por medio de un RETURN

def edad(edad):
    label = "la edad del usuario es: " + edad
    return label

print (edad("18"))

def impar(num):
    if num %2 == 0:
        label = str(num) + " es par"
    else:
        label = str(num) + " es impar"
    
    return label

print(impar(14))
print(impar(23))