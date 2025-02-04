years=int(input("Ingrese el Año que desee saber si es Bisiesto "))
if (years % 4 ==0) and (years % 100 !=0) or (years % 400 == 0):
     print("Estimado el Año ingresado !ES BISIESTO¡")
else:
    print("Estimado el Año ingresado NO es bisiesto :<" )
