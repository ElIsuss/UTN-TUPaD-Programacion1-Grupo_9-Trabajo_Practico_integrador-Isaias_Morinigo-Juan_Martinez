#------------------------FUNCIONES PARA ORDENAR------------------------

#------------------------------Ordenar paises por nombre--------------
def ordenar_paises(datos_paises):

    opcion = 0
    while opcion != 3:
        print('''
    # :::::::::::::::::::::::::::::::::::::
    #    1. Ascendente (A-Z)
    #    2. Desendente (Z-A)
    #    3. Volver
    # :::::::::::::::::::::::::::::::::::::''')
        try:
            opcion = int(input("Elije una opcion: "))
            if opcion == 1:
                for fila in datos_paises:
                    print(fila)
                print("\n")
            if opcion == 2:
                for fila in datos_paises[::-1]:
                    print(fila)
                print("\n")
            if opcion == 3:
                print("Volviendo al menu ordenar por paises...")
            if opcion not in range(1,4):
                print ("Porfavor elija una de las opciones mostradas por pantalla")
        except ValueError:
            print("Por favor elija una de las opciones mostradas por pantalla")

#-------------------------Ordenar paises por poblacion-------------------------

def ordenar_paises_por_poblacion(datos_paises):

    ordenar = sorted(datos_paises, key=lambda p: float(p["poblacion"]), reverse=True)
    paises_ordenados = ordenar

    print("Países ordenados por población (de mayor a menor):\n")
    for pais in paises_ordenados:
        print(f"{pais['nombre']:30}  {pais['poblacion']} habitantes")
    print("\n")




#-------------------------Ordenar paises por superficie-------------------------

def ordenar_paises_por_superficie(datos_paises):

    opcion = 0
    while opcion != 3:
        print('''
    :::::::::::::::::::::::::::::::::::::
        1. Ascendente 
        2. Desendente 
        3. Volver
    :::::::::::::::::::::::::::::::::::::''')
        try:
            opcion = int(input("Elije una opcion: "))
            if opcion == 1:
                    ordenar = sorted(datos_paises, key=lambda p: float(p["superficie"]), reverse=True)
                    paises_ordenados = ordenar
                    print("Países ordenados por superficie (de mayor a menor):\n")
                    for pais in paises_ordenados:
                        print(f"{pais['nombre']:30}  {pais['superficie']} superficie")
            if opcion == 2:
                    ordenar = sorted(datos_paises, key=lambda p: float(p["superficie"]), reverse=False)
                    paises_ordenados = ordenar
                    print("Países ordenados por superficie (de menor a mayor):\n")
                    for pais in paises_ordenados:
                        print(f"{pais['nombre']:30}  {pais['superficie']} superficie")
            if opcion == 3:
                    print("Volviendo al menu ordenar por paises...")
            if opcion not in range(1,4):
                        print("Porfavor elija una de las opciones mostradas por pantalla.")
        except ValueError:
            print("Por favor ingrese una de las opciones mostradas por pantalla")

