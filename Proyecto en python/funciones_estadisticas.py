#------------------------PAÍS CON MENOR Y MAYOR POBLACIÓN------------------------

def mayor_menor_poblacion(datos_paises):
    # Inicializamos las variables con el primer país del listado
    mayor_poblacion = int(datos_paises[0]['poblacion'])
    menor_poblacion = int(datos_paises[0]['poblacion'])
    pais_mayor = datos_paises[0]['nombre']
    pais_menor = datos_paises[0]['nombre']

    # Recorremos todos los países  
    for pais in datos_paises:
        poblacion = int(pais['poblacion'])
        if poblacion > mayor_poblacion:
            mayor_poblacion = poblacion
            pais_mayor = pais['nombre']
        if poblacion < menor_poblacion:
            menor_poblacion = poblacion
            pais_menor = pais['nombre']

    print("El país con mayor población es:")
    print(f"{pais_mayor}: {mayor_poblacion}")
    print("El país con menor población es:")
    print(f"{pais_menor}: {menor_poblacion}")
    print("\n")


#------------------------PROMEDIO DE POBLACIÓN------------------------

def promedio_poblacion(datos_paises):

    promedio = 0
    suma = 0
    total = 0
    for pais in datos_paises:
        poblacion_pais = int(pais['poblacion'])
        suma += poblacion_pais
        total += 1
    promedio = suma / total
    print(f"El promedio total de la población es: {promedio:,.2f}")
    print("\n")


#------------------------PROMEDIO DE SUPERFICIE------------------------

def promedio_superficie(datos_paises):

    promedio = 0
    suma = 0
    total = 0
    for pais in datos_paises:
        superficie_pais = int(pais['superficie'])
        suma += superficie_pais
        total += 1
    promedio = suma / total
    print(f"El promedio total de la superficie es: {promedio:,.2f}km²")
    print("\n")


#------------------------CANTIDAD PAÍS POR CONTINENTE------------------------

def paises_por_continente(datos_paises):

    america = 0
    europa = 0
    asia = 0
    oceania = 0
    africa = 0
    for pais in datos_paises:
        if pais['continente'] == "América":
            america += 1
        elif pais['continente'] == "Europa":
            europa += 1
        elif pais['continente'] == "Asia" :
            asia += 1
        elif pais['continente'] == "Oceanía":
            oceania += 1
        elif pais['continente'] == "África":
            africa += 1
    
    print(f''' Cantidad de paises por continente:\n
        América : {america}
        Europa : {europa}
        Asia: {asia}
        Oceanía: {oceania}
        África: {africa}''')