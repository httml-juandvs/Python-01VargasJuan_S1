
from math import sqrt
def parImpar(num):
    if num % 2 != 0:
        print(f"Estimado, el número {num} es IMPAR")
    else:
        print(f"Estimado, el número {num} es PAR")

def primoCompuesto(num):
    if num < 2:
        print(f"Estimado, el número {num} NO es primo ni compuesto")
        return
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            print(f"Estimado, el número {num} es COMPUESTO")
            return
    print(f"Estimado, el número {num} es PRIMO")

def cuadradoPerfect(num):
     raiz = int(sqrt(num))
     if (raiz * raiz == num):
        print(f"Estimado, el número {num} ES un CUADRADO PERFECTO")
     else:
        print(f"Estimado, el número {num} NO es un CUADRADO PERFECTO")

num=int(input("Ingrese un numero aleatorio: "))
parImpar()
primoCompuesto()
cuadradoPerfect()
    
