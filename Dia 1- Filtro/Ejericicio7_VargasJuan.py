n1 =int(input ("Ingresa n1 :" ))
n2 =int(input ("Ingresa n2 :" ))

suma1 = 0
suma2 = 0

for i in range(1,n1-1):
    if n1 % i==0:
        suma1 += +i
for l in range (1,n2-1):
    if n2 % i==0:
        suma2 += + l
        
if suma1 == n2 and suma2==n1 :
    print(f"{n1} and {n2} "Son numeros amigos")
    else:
    print(f"{n1} and {n2} "No son numeros amigos")