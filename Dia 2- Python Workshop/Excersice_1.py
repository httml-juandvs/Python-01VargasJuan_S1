## Conversion de grados Celsius a Fahrenheit
def celciusFahrenheit():
    C= int(input("Ingrese los grados Celsius que desee convertir: "))
    temperaturaF=(C * 9/5) + 32 
    print(f"La conversión serian {temperaturaF}° grados FAHRENHEIT ")

def FahrenheitCelsius ():
    F=int(input("Ingrese los grados Fahrenheit que desee convertir: " ))
    temperaturaC = ( F-32) * 5/9
    print(f"La conversión serian {temperaturaC}° grados CELCIUS ")

print("Elija una de las opcciones que desee usar")
print(" 1. Convertir de CELSIUS - FAHRENHEIT ")
print(" 2. Convertir de FAHRENHEIT - CELSIUS")

opc =int(input ())
if opc ==1:
    celciusFahrenheit()
elif opc ==2 :
    FahrenheitCelsius()
else:
    print("Opcción no válida")

## Elaborado por : Juan Vargas / T.I : 1.097.499.083