import csv 

def display_statistics() -> None:

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

    mayor_poblacion = paises[0]
    menor_poblacion = paises[0]

    for pais in paises:

        if pais["poblacion"] > mayor_poblacion["poblacion"]:

            mayor_poblacion = pais

        if pais["poblacion"] < menor_poblacion["poblacion"]:

            menor_poblacion = pais

    suma_poblacion = 0

    for pais in paises:

        suma_poblacion = suma_poblacion + pais["poblacion"]

    promedio_poblacion = suma_poblacion / len(paises)

    suma_superficie = 0

    for pais in paises:

        suma_superficie = suma_superficie + pais["superficie"]

    promedio_superficie = suma_superficie / len(paises)

    continentes = {}

    for pais in paises:

        cont = pais["continente"]
        if cont in continentes:
            continentes[cont] = continentes[cont] + 1
        else:
            continentes[cont] = 1

    print("\n" + "=" * 50)
    print("      DASHBOARD DE ESTADÍSTICAS")
    print("=" * 50)
    print("\nPOBLACIÓN")
    print("Mayor población:", mayor_poblacion["nombre"])
    print("Habitantes:", mayor_poblacion["poblacion"])
    print("Menor población:", menor_poblacion["nombre"])
    print("Habitantes:", menor_poblacion["poblacion"])
    print("Promedio de población:", int(promedio_poblacion))
    print("\nSUPERFICIE")
    print("Promedio de superficie:", int(promedio_superficie), "km²")
    print("\nPAÍSES POR CONTINENTE")

    for cont in continentes:

        print(cont, ":", continentes[cont], "país(es)")

    print("\n" + "=" * 50)