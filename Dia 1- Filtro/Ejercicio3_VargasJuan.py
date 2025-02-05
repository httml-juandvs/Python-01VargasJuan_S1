##Programa que completa la expresión

input ("Los numeros que satisfacen la expresion dada son:")
for i in range(0,200):
    for q in range(0,200):
        expresionMatematica = i**3+ q**4 -2* i**2
        if expresionMatematica < 680:
            input ("p", i)
            input ("q" , q)
            input("Sumatoria: ",expresionMatematica)

##Desarrollado por: Juan Vargas  / T.I: 1.097.499.083