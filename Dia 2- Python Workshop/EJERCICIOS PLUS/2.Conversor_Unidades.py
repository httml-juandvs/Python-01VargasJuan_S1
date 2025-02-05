print("Bienvenido al Conversor de Unidades  ")
print("1. Convertir de Kilometros a miilas  ")
print("2. Convertir de Celcius a Fahrenheit  ")
print("3. Convertir de Kilogramos a Libras  ")

conversor=int(input())
match conversor:
    case 1:
        kilometros=float(input("Ingrese la cantidad de de kilometros que deseea convertir  "))
        if kilometros <= 0:
            print("Estimado, recuerda que la cantidad debe ser positiva o mayor a cero")
        else:
            millas = kilometros*0,621371
            print(f"Estimado, los kilometros ingresados en MILLAS serian: {millas}mi")
    case 2:
        celcius=float(input("Ingrese los grados clecius que desee convertir  "))
        if celcius > 100 or celcius < -273.15 :
            print("Estimado,ERROR los rangos de temperatura que deseas agregar no estan permitidos")
        else:
            fahrenheit = (celcius * 9/5) + 32
            print(f"Estimado, los grados celcius ingresados en FAHRENHEIT serian: {fahrenheit}°")
    case 3:
        kilogramos=float(input("Ingrese la cantidad de kilogramos que desee convertir "))
        if kilogramos <=0:
            print("Estimado, recuerda que la cantidad debe ser positiva o mayor a cero")
        else:  
            libras = kilogramos*2
            print(f"Estimado, los kilogramos que deseea convertir en LIBRAS serian : {libras}Lb")
    case _:
        print("Estimado, escogiste una opccion incorrecta")
        exit