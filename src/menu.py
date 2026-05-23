from src.menu_actions.new_country import create_new_country

MENU = """
| 1: Agregar país   | 2: Actualizar población | 3: Actualizar superficie | 4: Buscar país por nombre |
| 5: Filtrar países | 6: Ordenar países       | 7: Mostrar estadísticas  | 8: Salir                  |"""
MENU_ALLOW_OPTIONS = [1,2,3,4,5, 6,7,8]

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
            None
        elif int(menu_option) == 3:
            None
        elif int(menu_option) == 4:
            None
        elif int(menu_option) == 5:
            None
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
                continue
            else:
                print("\nOpción inválida")
                continue

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
        elif int(menu_option) == 7:
            None
        elif int(menu_option) == 8:
            None