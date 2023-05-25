# Ser capaz de organizar muchos datos relaciones, es parte escencial de la programación

age_1 = 4
age_2 = 40
age_3 = 53
age_4 = 13

# Listas 
tareas = ["Read" , "Workout" , "Code"]
print(tareas)

user = ["Luis" , "Kevin" , 5 , True]
print(user)

temperaturas = [12,14,26,25] #los numeros inician desde 0, y se cuentan hasta el infinito, en este caso el 26 seria el indice 2
print(temperaturas[2])

temperaturas[2] = 35
print(temperaturas[2])

print(type(temperaturas))

laps = [320, 315, 321]

laps.append(365) #Lo agrega al print 
laps.insert(1,319) #Agrega el numero en el indice 1

eliminado = laps.pop(0)  #Elimina el indice 0
print(laps)
print("El elemento eliminado es", eliminado)

#Recorrer listas por medio de un bucle

notas = [100,98,42,54,67,75]

print(notas)

for nota in notas:
    print(nota)

artistas = ["Marco" , "Antonio"]

for artista in artistas:
    print(artista)

#Podemos averiguar el numero de elementos de una lista con el comando LEN

users = ["Luis" , "Kevin","Greivin"]
users_cont = len(users)
print(users_cont)

#Podemos usar la longitud de las lista para crear declaraciones condicionales basadas en la cantidad de elementos como el anterior
if len(users) > 0:
    print("Empieza a trabajar")
else:
    print("No tienes nada en la lista")

lista_de_compras= ["papas", "arroz", "frijoles"]
if len(lista_de_compras) > 0:
    for arti in lista_de_compras:
        print (arti)
else:
    print("No es suficiente")