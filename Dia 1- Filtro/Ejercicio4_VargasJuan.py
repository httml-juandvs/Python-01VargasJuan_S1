# Programa para encontrar el número mayor y menor de una lista de 10 números ingresados por el usuario

grande = 0
pequeno = 0
for i in range(1, 10):
    numerito = int(input("Ingrese el número {i}: "))
    if grande is None or pequeno is None:
        grande = numerito
        pequeno = numerito
    else:
       
        if numerito > grande:
            grande = numerito
        if numerito < pequeno:
            pequeno = numerito

print("Grande: " , grande)
print("Pequeño: ", pequeno)

##Desarrollado por: Juan Vargas  / T.I: 1.097.499.083