##Genereador de contraseñas
print("Estimado, bienvenido al generador de contraseñas")
import random
minusculas = "abcdefghijklmnñopqrstuvxyz"
mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVXYZ"
numeros = "0123456789"
simbol = "°!@$#$%&/()=?¡¿+*-_.,:;"
base = minusculas+mayusculas+numeros+simbol
longitud = 10
muestra = random.sample(base,longitud)
password = "".join(muestra)
print(f"Su contraseña generada es: {password}")