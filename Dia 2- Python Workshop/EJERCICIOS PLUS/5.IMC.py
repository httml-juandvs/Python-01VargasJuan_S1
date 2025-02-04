print("Binevenido a la calculador a de IMC")
peso= 0
peso=float(input("Ingrese su peso corporal en KG  "))

if peso < 18.5:
    print("Bajo de peso")
elif peso >= 18.5 and peso <= 24.9:
    print("Peso normal")
elif peso < 25 and peso >= 29.9 :
    print("Sobrepeso")
elif peso > 30 :
    print("Sobre peso")
