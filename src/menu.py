from src.menu_actions.new_country import create_new_country
from src.menu_actions.update_country_data import update_country_data
from src.menu_actions.filter_countries import filter_countries
from src.menu_actions.sort_countries import sort_countries
MENU = """
| 1: Agregar país   | 2: Actualizar Datos del País | 3: Buscar país por nombre | ---------- |
| 4: Filtrar países | 5: Ordenar países            | 6: Mostrar estadísticas   | 7: Salir   |"""
MENU_ALLOW_OPTIONS = [1,2,3,4,5, 6,7]

def show_main_menu() -> None:
    # todas las opciones de menú estrán aqui dentro. Será la forma de volver al menú automaticamente luego de 
    # ejecutar cada opcion del menu
    while True:
        print(f"\n {MENU}")
        
        menu_option = input("\nElija la opción del Menú: ")
        # si es un número y está en en la lista de opciones permitidas
        if not( menu_option.isdigit() and int(menu_option) in MENU_ALLOW_OPTIONS ):
            print("\n[ERROR] - Ha elegido una opción que no se encuentra en el menú principal. Inténtelo nuevamente")
            continue
        
        # Cada opción del menú se implementa en su propio módulo dentro de menu_actions/
        if int(menu_option) == 1:
            create_new_country()
        elif int(menu_option) == 2:
            update_country_data()
        elif int(menu_option) == 3:
            import csv

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
                continue

            if len(paises) == 0:
                print("\nNo hay países cargados")
                continue

            nombre = input("\nIngrese el nombre del país: ").strip()

            if nombre == "":
                print("\nDebe ingresar un nombre")
                continue

            encontrados = []

            for pais in paises:
                if nombre.lower() in pais["nombre"].lower():
                    encontrados.append(pais)

            if len(encontrados) == 0:
                print("\nNo se encontraron coincidencias")
                continue

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
                print("Superficie:", elegido["superficie"], "km²")
                print("Continente:", elegido["continente"])
                print("====================================")
        elif int(menu_option) == 4:
            filter_countries()
        elif int(menu_option) == 5:
            sort_countries()
        elif int(menu_option) == 6:
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
                continue

            if len(paises) == 0:

                print("\nNo hay países cargados")
                continue

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
        elif int(menu_option) == 7:
            print("[ CERRANDO PROGRAMA ...]")
            break