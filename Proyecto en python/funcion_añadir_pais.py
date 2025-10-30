import csv

def agregar_pais(ruta, datos_paises):
    
    """
    Permite al usuario agregar un país al archivo CSV y a la lista en memoria.
    """
    print("========== Agregar un nuevo país ==========")
    nombre = input("Nombre del país: ").strip().capitalize()
    continente = input("Continente: ").strip().capitalize()
    try:
        poblacion = int(input("Población (en habitantes): "))
        superficie = float(input("Superficie (en km²): "))
    except ValueError:
        print("Error: la población y la superficie deben ser números.")
        return
    
    # --- Verificar si el país ya existe ---
    for pais in datos_paises:
        if pais["nombre"].strip().lower() == nombre.lower():
            print(f"\n⚠️ El país '{nombre}' ya existe en el registro.\n")
            return

    # Crear el nuevo registro
    nuevo_pais = {
        "nombre": nombre,
        "continente": continente,
        "poblacion": poblacion,
        "superficie": superficie
    }
    # Añadir al CSV
    try:
        with open(ruta, "a", newline="", encoding="utf-8-sig") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "continente", "poblacion", "superficie"])
            escritor.writerow(nuevo_pais)
    except Exception as e:
        print("Error al escribir en el archivo:", e)
        return

    # Añadir a la lista en memoria
    datos_paises.append(nuevo_pais)
    print(f"\n✅ País '{nombre}' agregado correctamente.\n")
