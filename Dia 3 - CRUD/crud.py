#Recorrer una lista
nombres = [
    ["Adrián"],
    ["Alejandra"],
    ["Ámbar", "Isabella"],
    ["Andrés", "David"],
    ["Aura", "Camila"],
    ["Camilo", "Andrés"],
    ["Daniel", "Esteban"],
    ["David", "Santiago"],
    ["Edgar", "Leonardo"],
    ["Gerson", "Steven"],
    ["Harley", "Yefrey"],
    ["John", "Stiven"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "Eduardo"],
    ["Juan", "Fernando"],
    ["Juan", "Jose"],
    ["Maria", "Juliana"],
    ["Mateo", "Roman"],
    ["Naya", "Zarela"],
    ["Nicolas"],
    ["Omar", "Fernando"],
    ["Santiago"],
    ["Santiago", "Andrés"],
    ["Santiago"],
    ["Sara", "Sofía"],
    ["Sayara", "Yurley"],
    ["Sergio", "Andrés"],
    ["Simón", "Dante"],
    ["Thomas", "Sebastián"],
    ["Vladimir"]
]

apellidos = [
    ["Quintero", "Pinzón"],
    ["Pinzón", "Alvarez"],
    ["Plata", "López"],
    ["Reyes", "Espinel"],
    ["Pico", "Araque"],
    ["Suárez", "Fuentes"],
    ["Guerrero", "Quintero"],
    ["Vera", "Mendez"],
    ["Acevedo", "Arteaga"],
    ["Chaparro", "Martínez"],
    ["Cabrales", "Vargas"],
    ["Negron", "Regalado"],
    ["Saavedra", "Jaimez"],
    ["Santoyo", "Jaimes"],
    ["Vargas", "Soto"],
    ["Pinilla", "Guzmán"],
    ["Umaña", "Barragan"],
    ["Abril", "Roman"],
    ["Saavedra", "Mejia"],
    ["Camargo"],
    ["Lizcano", "Jaimes"],
    ["Chedraui", "Mantilla"],
    ["Granados", "Parra"],
    ["Aguilar", "Vesga"],
    ["Quiñonez", "Sosa"],
    ["Jaimes", "Perez"],
    ["Díaz", "Rodríguez"],
    ["Aparicio", "Arciniegas"],
    ["Rueda", "Hernández"],
    ["Salamanca", "Galvis"],
    ["Bastos", "Garcia"],
    ["Diaz", "Contreras"]
]
for  i in zip(nombres, apellidos):
    nombreCompleto = " ".join(nombres[i]) + " " + " ".join(apellidos[i])

booleanito= True
while (booleanito==True):
    print("\nBienvenido al programa de lista de estudiantes")
    print("Que te gustaría hacer?")
    print("1.Agregar estudiante")
    print("2. Ver estudiantes")
    print("3.Editar estudiante")
    print("4.Eliminar estudiante")
    print("5.Salir del programa")
    opcionUsuario= int(input(":"))


if (opcionUsuario==1):
    print("listadeestudiantes")
    for i in range (len (nombres)):
        nombreCompleto="".join(nombres[i]) +" "+" ".join(apellidos [1])
        print (f"{1+1}. {nombreCompleto}")
    nombreEstudiante=int(input(" A Cual estudiante quieres editarle el nombre ? (numero):"))
    nombreEstudianteNuevo=input("Cual será el nombre nuevo del estudiante?: ")
    apellidoEstudianteNuevo=input("Cual será el apellido nuevo del estudiante?:")
    nombres [nombreEstudiante-1]=nombreEstudianteNuevo
    print(nombreCompleto)

elif(opcionUsuario==2):
        print("Lista estudiantes:")
        for i in range(len(nombres)):##Indicar cuántas veces debe recorrerlo de acuerdo al tamaño de la lista
            nombreCompleto = " ".join(nombres[i]) + " " + " ".join(apellidos[i])
            print=(f"Estudiante # {i+1} {nombreCompleto[i]}")
            print (nombreCompleto)

elif(opcionUsuario==3):
        print("Lista de estudiantes:")
        for i in range(len(nombreCompleto)):##Indicar cuántas veces debe recorrerlo de acuerdo al tamaño de la lista
            print("Estudiante #",i+1,": ",nombreCompleto[i])
        numeroEstudiante=int(input("Cual estudiante quieres editar?:"))
        nombreEstudianteNuevo=input("Cual será el nombre nuevo del estudiante?:")
        nombreCompleto[numeroEstudiante-1]=nombreEstudianteNuevo

elif(opcionUsuario==4):
        print("Lista de estudiantes:")
        for i in range(len(nombreCompleto)):##Indicar cuántas veces debe recorrerlo de acuerdo al tamaño de la lista
            print("Estudiante #",i+1,": ",nombreCompleto[i])
        numeroEstudiante=int(input("Cual estudiante quieres eliminar?:"))
        nombreCompleto.pop(numeroEstudiante-1)

elif(opcionUsuario==5):
        booleanito== False