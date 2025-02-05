from modulos1 import*
bo=True
while bo:
    print("\nBienvenido al programa de lista de estudiantes")
    print("Que te gustaría hacer?")
    print("1.Agregar estudiante")
    print("2. Ver estudiantes")
    print("3.Editar estudiante")
    print("4.Eliminar estudiante")
    print("5.Salir del programa")
    opc=int(input(":"))
    
    if opc==1:
        agregarEstudiante()
    elif opc==2:
        verLista()
    elif opc==3:
        editarEstudiate()
    elif opc==4:
        eliminarEstudiante    
    elif opc==5:
        break
    else:
        print("La opcion que ingreso es incorrecta")
    bo=False
