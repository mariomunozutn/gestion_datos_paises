import csv


def sort_countries() -> None:
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

    print("\n===== ORDENAR PAÍSES =====")
    print("1. Nombre (A-Z)")
    print("2. Población (menor a mayor)")
    print("3. Población (mayor a menor)")
    print("4. Superficie (menor a mayor)")
    print("5. Superficie (mayor a menor)")
    print("0. Volver")

    opcion = input("\nSeleccione una opción: ")


    if opcion == "1":
        for i in range(len(paises)):
            for j in range(i + 1, len(paises)):
                if paises[i]["nombre"] > paises[j]["nombre"]:
                    aux = paises[i]
                    paises[i] = paises[j]
                    paises[j] = aux
        print("\nPaíses ordenados por nombre (A-Z)")

    elif opcion == "2":
        for i in range(len(paises)):
            for j in range(i + 1, len(paises)):
                if paises[i]["poblacion"] > paises[j]["poblacion"]:
                    aux = paises[i]
                    paises[i] = paises[j]
                    paises[j] = aux
        print("\nPaíses ordenados por población (menor a mayor)")
    elif opcion == "3":
        for i in range(len(paises)):
            for j in range(i + 1, len(paises)):
                if paises[i]["poblacion"] < paises[j]["poblacion"]:
                    aux = paises[i]
                    paises[i] = paises[j]
                    paises[j] = aux
        print("\nPaíses ordenados por población (mayor a menor)")


    elif opcion == "4":
        for i in range(len(paises)):
            for j in range(i + 1, len(paises)):
                if paises[i]["superficie"] > paises[j]["superficie"]:
                    aux = paises[i]
                    paises[i] = paises[j]
                    paises[j] = aux
        print("\nPaíses ordenados por superficie (menor a mayor)")

    elif opcion == "5":
        for i in range(len(paises)):
            for j in range(i + 1, len(paises)):
                if paises[i]["superficie"] < paises[j]["superficie"]:
                    aux = paises[i]
                    paises[i] = paises[j]
                    paises[j] = aux
        print("\nPaíses ordenados por superficie (mayor a menor)")

    elif opcion == "0":
        return
    else:
        print("\nOpción inválida")
        return

    print("\n" + "-" * 60)
    for pais in paises:
        print(
         pais["nombre"],
         "- Población:",
         pais["poblacion"],
         "- Superficie:",
         pais["superficie"],
         "km² -",
         pais["continente"]
        )
    print("-" * 60)