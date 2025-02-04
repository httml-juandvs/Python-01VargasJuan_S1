input ("Ingrese la cantidad de empleados: ")
mayorSueldo(0)
menorSueldo(0)
for i in range (1,N-1):
    input("Ingrese el nombre del empleado", i ," :")
    input("Ingrese las horas trabajadas: ")
    bruto = horas = 2000
    eps = bruto * 0.04
    pension = bruto  *0.04
    neto= bruto- eps -pension

    totalBruto = totalBruto +bruto
    totalEPS = totalEPS + eps
    totalPension = totalPension + pension
    totalNeto = totalNeto + neto

    if neto > mayorSueldo :
        mayorSueldo = neto
        nombreMayor = nombre
    if neto < menorSueldo:
        menorSueldo = neto
        nombreMenor = nombre
    input ("Empleado ", nombre)
    input ("Sueldo Bruto: $ ", bruto)
    input ("EPS: $ ",eps)
    input ("Pensión : $ ",pension)

