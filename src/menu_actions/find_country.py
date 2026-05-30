import csv


def search_country() -> None:
    paises = []
    try:
        with open("data/paises.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                fila["poblacion"] = int(fila["poblacion"])
                fila["superficie"] = int(fila["superficie"])
                paises.append(fila)
    except:
        print("\nError al abrir el archivo")
        return

    if len(paises) == 0:
        print("\nNo hay países cargados")
        return

    nombre = input("\nIngrese el nombre del país: ").strip()

    if nombre == "":
        print("\nDebe ingresar un nombre")
        return

    encontrados = []

    for pais in paises:
        if nombre.lower() in pais["nombre"].lower():
            encontrados.append(pais)

    if len(encontrados) == 0:
        print("\nNo se encontraron coincidencias")
        return

    print("\nResultados encontrados:\n")

    for i in range(len(encontrados)):
        print(
         str(i + 1) + ".",
         encontrados[i]["nombre"],
         "-",

         encontrados[i]["continente"]
        )

    if len(encontrados) == 1:
        elegido = encontrados[0]
    else:
        elegido = None
        while elegido == None:
            opcion = input("\nSeleccione un número o 0 para cancelar: ")
            if opcion == "0":
                break
            if opcion.isdigit():
                num = int(opcion)
                if num >= 1 and num <= len(encontrados):
                    elegido = encontrados[num - 1]
                else:
                    print("Número inválido")
            else:
                print("Ingrese solo números")

    if elegido != None:
        print("\n========== DATOS DEL PAÍS ==========")
        print("Nombre:", elegido["nombre"])
        print("Población:", elegido["poblacion"])
        print("Superficie:", elegido["superficie"], "KM cuadrados")
        print("Continente:", elegido["continente"])
        print("====================================")