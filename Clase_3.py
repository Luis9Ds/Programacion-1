# Minimo y Maximo, Clasificación de Listas, sumando lista, como unir conjuntos de datos y contar numeros de apariciones
# Ademas de la utilización de instrumentos de cuerda y actualización de cadenas.

numeros = [10,45,2,89,54,1,-3]
print(max(numeros), min(numeros))

maximo = max(numeros)
minimo= min (numeros)
print(maximo)
print(minimo)

#Se puede hacer directamente con el max, o tambien usando la variable correspondiente (operaciones matematicas)
sumar = max(numeros) + min(numeros) 
print(sumar)

numeros.sort()
print(numeros)

nombres = ["Luis","Kevin","Goku","Luffy","Antonio","Bobert"]
nombres.sort()
print(nombres)
print("------------------------------------------------------------------------------------------------------")
# Sumar listas
promedios = [85,95,65,23,100]
print(sum(promedios))

print("------------------------------------------------------------------------------------------------------")
# Unir listas o conjuntos de datos
ventas_sab = [12,32,43,434,90]
ventas_dom = [13,576,75,33,12,3]
ventas_totales = ventas_sab + ventas_dom
print(ventas_totales)

# Como saber la moda (mas popular, dato mas repetido)
print("------------------------------------------------------------------------------------------------------")

pregunta1 = [1,1,1,1,1,1,2,2,2,4,4,4,4,3,3,3,5,5,5,5,5,1,1,1,1,1,1,4,4,9,9,9,9,9,9,7,7,7,7,7,7,7,5,2,2,2,2,2,1,1,1,1,1,1,1,1]
print(pregunta1.count(4))
print(30 in pregunta1)

print("------------------------------------------------------------------------------------------------------")

# Instrumentos de cuerda
nuevo_usuario = "Luis Diego Picado Beita"
usuario_lista = nuevo_usuario.split()
print(usuario_lista)

direccion = "Urb El Peregrino, Volcán, Buenos Aires, Puntarenas, Costa Rica, 60301"
nueva_direccion = direccion.replace("Volcán","Volcancito")

dataset = direccion.split(",")

print(dataset)
print(nueva_direccion)

# Practica usar If, For e In para ordenar la lista dependiendo de si es mayor o menor. Comparando los datos con For y cambiando la lista segun el numero
lista = [10,9,7,6,5,3,1,2,8,4]
lista_ordenada =[1,2,3,4,5,6,7,8,9,10]

if lista != [1,2,3,4,5,6,7,8,9,10]:
    print(lista_ordenada)





