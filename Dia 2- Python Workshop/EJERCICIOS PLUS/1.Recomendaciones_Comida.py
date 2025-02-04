##Recomendaciones Comida
print("Bienvenido usuario a recomendaciones de comidas")
print("Seleccione cómo está el clima:")
print(" 1. Soleado")
print(" 2. Lluvioso")
print(" 3. Frío")

clima = int(input()) 

print("¿Cuál es la hora del día?")
print(" 1. Mañana")
print(" 2. Tarde")
print(" 3. Noche")

hora = int(input())  
match clima:
    case 1:  # Soleado
            if hora ==1:
                print("Smoothie de frutas tropicales con tostadas de aguacate.")
            elif hora ==2:
                print("Ensalada fresca con pollo a la parrilla y una limonada.")
            elif hora == 3:
                print("Ceviche de pescado con maíz tostado y una bebida refrescante.")
            else:
                print("ERROR: Opción no válida")
        
    case 2:  # Lluvioso
        if hora ==1:
            print("Chocolate caliente con pan dulce o tamales.")
        elif hora == 2:
            print("Sopa de lentejas o caldo de pollo con arroz.")
        elif hora== 3:
                print("Pasta cremosa con champiñones y queso parmesano.")
        else:
            print("ERROR: Opción no válida")

    case 3:  # Frío
            if hora == 1:
                print("Avena caliente con canela y nueces.")
            elif hora ==2:
                print("Estofado de carne con papas y zanahorias.")
            elif hora == 3:
                print("Fondue de queso con pan o una sopa de cebolla gratinada.")
            else:
                print("ERROR: Opción no válida")

    case _:
        print("ERROR: Opción de clima no válida")
## Elaborado por Juan Vargas / T.I 1.097.499.083