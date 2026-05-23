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
        elif int(menu_option) == 5:
            None
        elif int(menu_option) == 6:
            None
        elif int(menu_option) == 7:
            None
        elif int(menu_option) == 8:
            None