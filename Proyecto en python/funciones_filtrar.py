#----------------------REEMPLAZAR LETRAS CON TILDE----------------------

import unicodedata

def normalizar(info):
    """
    Elimina acentos y convierte a minúsculas.
    """
    # buscar_pais = buscar_pais.lower()
    info = unicodedata.normalize('NFD', info)
    info = ''.join(c for c in info if unicodedata.category(c) != 'Mn')
    return info.lower()




#------------------------FUNCIONES PARA FILTRAR------------------------

# ---------------------------------------Filtrar por paises (especifico o coincidensia)--------------------------


def filtar_por_paises(datos_paises):

    buscar_pais = input("Dime el nombre de un pais:\n").strip()
    buscar_pais_normalizado = normalizar(buscar_pais)
    if buscar_pais == "":
        print("No se encontro el pais")
        print("\n")
    else:
        for dato_de_un_pais in datos_paises:
            nombre_pais_normalizado = normalizar(dato_de_un_pais["nombre"])

            if buscar_pais_normalizado in nombre_pais_normalizado:
                # Convertir a números para poder formatear
                poblacion = int(dato_de_un_pais['poblacion'])
                superficie = float(dato_de_un_pais['superficie'])

                print("───────────────────────────────")
                print(f" Nombre del país:  {dato_de_un_pais['nombre']}")
                print(f" Población:       {poblacion:,.0f} habitantes")
                print(f" Superficie:      {superficie:,.0f} km²")
                print(f" Continente:      {dato_de_un_pais['continente']}")    
                print("───────────────────────────────\n")
        print("\n")
        



# ---------------------------------------Paises por continentes---------------------------------------------
def filtrar_por_continentes(datos_paises):

    ver_paises_por_continente = input("Dime un continente y te mostraré todos sus países:\n").strip()
    continente_normalizado = normalizar(ver_paises_por_continente)
    # Crear lista de países que coincidan con el continente (sin importar tildes o mayúsculas)
    paises_filtrados = [
        pais["nombre"] for pais in datos_paises
        if normalizar(pais["continente"]) == continente_normalizado
    ]

    if paises_filtrados:
        print(f"\nPaíses en {ver_paises_por_continente.capitalize()}:")
        for pais in paises_filtrados:
            print("-", pais)
        print("\n")
    else:
        print("Continente inexistente. Volviendo al menú...\n")


# --------------------------------Filtrar por habitantes------------------------------      
def filtar_por_habitantes(datos_paises):
    
    try:
        buscar_por_poblacion = int(input("Dime un numero de habitantes y te dire los paises que superan o estan por debajo de ese numero de ese numero: "))  
        mayor_poblacion= []
        menor_poblacion = []
        igual_poblacio = []

        for pais in datos_paises:
            try:
                poblacion = int(pais["poblacion"])
            except ValueError:
                continue  # si hay un valor no numérico, lo salta

            if poblacion > buscar_por_poblacion:
                mayor_poblacion.append(pais["nombre"])
            elif poblacion < buscar_por_poblacion:
                menor_poblacion.append(pais["nombre"])
            elif poblacion == buscar_por_poblacion:
                igual_poblacio.append(pais["nombre"])

        opcion = 0
        while opcion != 3:
            print('''
        ::::::::::::::::::::::::::::::::::::: 
        1. Ver poblacion mayor
        2. Ver poblacion menor
        3. Volver
        :::::::::::::::::::::::::::::::::::::''')
            try:
                opcion = int(input("Elija una opcion: "))
                if opcion == 1:
                    if not mayor_poblacion:
                        print(f"No hay paises con mayor población a {buscar_por_poblacion}")
                        continue
                    print(f"\nPaíses con población MAYOR a {buscar_por_poblacion}:")
                    if igual_poblacio:
                        print(f"\nPaís(es) con población EXACTA a {buscar_por_poblacion}:")
                    for p in igual_poblacio:
                        print("-", p)
                    for p in mayor_poblacion: 
                        print("-", p)
                if opcion == 2:
                    if not menor_poblacion:
                        print(f"No hay paises con menor población a {buscar_por_poblacion}")
                        continue
                    if igual_poblacio:
                        print(f"\nPaís(es) con población EXACTA a {buscar_por_poblacion}:")
                    for p in igual_poblacio:
                        print("-", p)
                    print(f"\nPaíses con población MENOR a {buscar_por_poblacion}:")
                    for p in menor_poblacion:  
                        print("-", p)     
                if opcion == 3:
                    print("Saliendo del programa...")
                    print("\n")
                    break
                if opcion not in range(1,4):
                    print("Porfavor elija una de las opciones mostradas por pantalla")
            except ValueError:
                print("Porfavor ingrese una de las opciones mostradas por pantalla")
    except ValueError:
        print("Tipo de dato incorrecto")
        
        
        
# ---------------------Filtrar por superficie-------------------------
    
    
def filtar_por_superficie(datos_paises):
    
    try:
        buscar_por_superficie = float(input("Dime un numero de superficie y te dire los paises que estan por debajo y por arriba de ese numero: "))
        
        mayor_superficie = []
        menor_superficie = []
        igual_superficie = []
        for pais in datos_paises:
            try:
                superficie = float(pais["superficie"])
            except ValueError:
                continue  # si hay un valor no numérico, lo salta

            if superficie > buscar_por_superficie:
                mayor_superficie.append(pais["nombre"])
            elif superficie < buscar_por_superficie:
                menor_superficie.append(pais["nombre"])
            else:
                igual_superficie.append(pais["nombre"])
        if igual_superficie:
            print(f"\nPaís(es) con superficie EXACTA a {buscar_por_superficie}:")
            for p in igual_superficie:
                print("-", p)
        opcion = 0
        while opcion != 3:
            print('''
        ::::::::::::::::::::::::::::::::::::: 
        1. Ver superficie mayor
        2. Ver superficie menor
        3. Volver
        :::::::::::::::::::::::::::::::::::::''')
            try:
                opcion = int(input("Elija una opcion: "))
            except ValueError:
                print("Ingrese un número válido.")
                continue
            if opcion == 1:
                print(f"\nPaíses con superficie MAYOR a {buscar_por_superficie}:")
                for p in mayor_superficie:
                    print("-", p)

            elif opcion == 2:
                print(f"\nPaíses con superficie MENOR a {buscar_por_superficie}:")
                for p in menor_superficie:
                    print("-", p)
                    
            elif opcion == 3:
                print("Saliendo del programa...")
                print("\n")
            elif opcion not in range(1,4):
                print("Porfavor elija una de las opciones mostradas por pantalla")
    except ValueError:
        print("Tipo de dato incorrecto")
        


