import csv
import os
import funciones_filtrar
import funciones_ordenar
import funciones_estadisticas
import funcion_añadir_pais

ruta = r"C:\Users\User\Desktop\Trabajo Integrador\paises.csv"
datos_paises = []

# ============================================================
# CARGA O CREACIÓN DEL ARCHIVO CSV
# ============================================================
try:
    with open(ruta, "r", newline="", encoding="utf-8-sig") as archivo:
        lector_dict = csv.DictReader(archivo, delimiter=',')
        for fila in lector_dict:
            datos_paises.append(fila)
except ValueError:
    print("XXX Ocurrió un error XXX")
except FileNotFoundError:
    print("No se encontró el archivo, creando uno nuevo con encabezados...")
    with open(ruta, "w", newline="", encoding="utf-8-sig") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["nombre", "continente", "poblacion", "superficie"])
    print(f"Archivo creado en: {ruta}")
    print("⚠️  Todavía no hay países registrados. Use la opción 5 para añadir uno.")

# ============================================================
# MENÚ PRINCIPAL
# ============================================================
opcion = 0
while True:
    print('''
|------------------------------------------------------------|
|                       MENÚ PRINCIPAL                       |
|------------------------------------------------------------| 
| 1. Buscar países                                           |
| 2. Filtrar países                                          |
| 3. Ordenar países                                          |
| 4. Mostrar estadísticas                                    |
| 5. Crear/Añadir país                                       |
| 6. Salir                                                   |
|------------------------------------------------------------|
    ''')

    try:
        opcion = int(input("Elija una opción: "))
    except ValueError:
        opcion = 0
        print("Opción incorrecta. Por favor ingrese una de las opciones mostradas por pantalla.")
        continue

    # 🚨 Verificación: si no hay países cargados y se elige 1–4, mostrar aviso
    if opcion in [1, 2, 3, 4] and len(datos_paises) == 0:
        print("⚠️  Todavía no hay países registrados. Use la opción 5 para añadir uno.")
        continue

    # ============================================================
    # OPCIONES DEL MENÚ
    # ============================================================
    if opcion == 1:
        funciones_filtrar.filtar_por_paises(datos_paises)

    elif opcion == 2: 
        menu_filtrar_paises = 0
        while menu_filtrar_paises != 4:
            print('''
    **************************** Filtrar Países ****************************
        
        1. Filtrar por continente
        2. Filtrar por rango de población
        3. Filtrar por rango de superficie
        4. Volver
        
    ************************************************************************
            ''')
            try:
                menu_filtrar_paises = int(input("Elija una opción: ")) 
                if menu_filtrar_paises == 1:
                    funciones_filtrar.filtrar_por_continentes(datos_paises)
                elif menu_filtrar_paises == 2:
                    funciones_filtrar.filtar_por_habitantes(datos_paises)
                elif menu_filtrar_paises == 3:
                    funciones_filtrar.filtar_por_superficie(datos_paises)
                elif menu_filtrar_paises == 4:
                    print("Saliendo del menú de filtrado.")
                elif menu_filtrar_paises > 4:
                    print("Por favor elija una de las opciones mostradas por pantalla.")
            except ValueError:
                print("Por favor ingrese una opción válida.")  

    elif opcion == 3:
        menu_ordenar_paises = 0
        while menu_ordenar_paises != 4:
            print('''
    **************************** Ordenar Países ****************************
        
        1. Ordenar por nombre 
        2. Ordenar por población
        3. Ordenar por superficie
        4. Volver
        
    ************************************************************************
            ''')
            try:
                menu_ordenar_paises = int(input("Elija una opción: "))
            except ValueError:
                print("Por favor ingrese una de las opciones mostradas por pantalla.")
                continue
            
            if menu_ordenar_paises == 1:
                funciones_ordenar.ordenar_paises(datos_paises)
            elif menu_ordenar_paises == 2:
                funciones_ordenar.ordenar_paises_por_poblacion(datos_paises)
            elif menu_ordenar_paises == 3:
                funciones_ordenar.ordenar_paises_por_superficie(datos_paises)
            elif menu_ordenar_paises == 4:
                print("Saliendo del menú de ordenamiento.")
            elif menu_ordenar_paises > 4:
                print("Opción fuera de rango.")

    elif opcion == 4:
        menu_mostrar_estadisticas = 0
        while menu_mostrar_estadisticas != 5:
            print('''
    **************************** Promedio Países ****************************
    
        1. País con mayor y menor población
        2. Promedio de población
        3. Promedio de superficie
        4. Cantidad de países por continente
        5. Volver
        
    *************************************************************************
            ''')
            try:
                menu_mostrar_estadisticas = int(input("Elija una opción: "))
                if menu_mostrar_estadisticas == 1:
                    funciones_estadisticas.mayor_menor_poblacion(datos_paises)
                elif menu_mostrar_estadisticas == 2:
                    funciones_estadisticas.promedio_poblacion(datos_paises)
                elif menu_mostrar_estadisticas == 3:
                    funciones_estadisticas.promedio_superficie(datos_paises)
                elif menu_mostrar_estadisticas == 4:
                    funciones_estadisticas.paises_por_continente(datos_paises)
                elif menu_mostrar_estadisticas == 5:
                    print("Saliendo del programa de estadísticas.")
                elif menu_mostrar_estadisticas not in range(1,6):
                    print("Opción fuera de rango.")
            except ValueError:
                print("Por favor ingrese una opción válida.") 

    elif opcion == 5:
        funcion_añadir_pais.agregar_pais(ruta, datos_paises)

    elif opcion == 6:
        print("👋 Saliendo del programa...")
        break

    elif opcion > 6:
        print("Opción fuera de rango.")
