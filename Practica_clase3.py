# Practica usar If, For e In para ordenar la lista dependiendo de si es mayor o menor. Comparando los datos con For y cambiando la lista segun el numero
lista = [10,9,7,6,5,3,1,2,8,4]
for i in range(len(lista)):
        for j in range(len(lista)-1):
                if lista[j] > lista[j+1]:
                        
                        
                        lista[j],lista[j+1] = lista [j+1], lista[j]

print(lista)
    
