## Calculadora de intereses
print("Bienvenido Usuario a la calculadora de Intereses")
capital=int(input("Ingrese el Capital"))
tasa=int(input("Ingrese la Tasa de Interes"))
tiempo=int(input("Ingrese el tiempo en *MESES* "))

interesSimple = capital*tasa*tiempo
print ("El interes Simple es de : $", interesSimple)

opc=int(input("¿Desea Calcular el interes compuesto? S / N"))
if opc == "S":
    capitalC = int(input("Ingrese el Capital: "))
    tasaC = float(input("Ingrese la Tasa de Interés Anual (en decimal, por ejemplo 0.05 para 5%): "))
    tiempoC = int(input("Ingrese el tiempo en *AÑOS*: "))

    interes_compuesto = capitalC * (1 + tasaC) ** tiempoC
    print(f"El interés compuesto es de: ${interes_compuesto:.2f}")

elif opc == "N":
    print("Gracias por usar la calculadora de intereses. ¡Hasta luego!")
## Elaborado por : Juan Vargas / T.I : 1.097.499.083