# Ejemplos de Bucles

num1 = 1
num1 = num1 + 1
print(num1)

# Bucle While
Control = True
while Control == True:
    print(num1)
    num1 += 1
    if num1 == 301:
        Control = False

contador = 0
num2 = 1
while contador < 100:
    print(num2)
    num2 += 1
    contador += 1

contador = 0
online =  True
num2 = 1
while contador < 100 and online:
    print(num2)
    num2 += 1
    contador += 1

# Bucle o Ciclo For

for i in range (4):
    print(i)
for c in range (2):
    print("We will")
print("Rock you!")

for num in range (0,11,2):
    print(num)
