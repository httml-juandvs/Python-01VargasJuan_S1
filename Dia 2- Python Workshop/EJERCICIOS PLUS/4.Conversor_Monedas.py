print("Bienvenido al conversor de monedas de USD a otras monedas")
usd=int(input("Ingrese cuantos USD desea convertir "))
print("Selecione la moneda para hacer la conversión")
print(" 1. Euros € " )
print(" 2. Pesos Colombianos COP ")
print(" 3. Yenes ¥ ")
moneda=int(input())

match moneda:
    case 1:
       euros= usd * 0.85
       print(f"Estimado, los {usd} USD ingresados en Euros serian € {euros}.")
    case 2 :
        cop = usd * 4100
        print(f"Estimado, los {usd} USD ingresados en Pesos Colombianos serian {cop} COP.")
    case 3 :
        yen =usd * 110
        print(f"Estimado, los {usd} USD5
         ingresados en Yenes serian ¥ {yen}.")
    case _:
        print("Estimado la moneda seleccionada no esta disponible :< ")



