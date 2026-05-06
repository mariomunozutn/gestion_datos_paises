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
            FILE_LOCATION = "data/paises.csv"
    
            paises = []
            try:
                with open(FILE_LOCATION, "r", encoding="utf-8") as file:
                   reader = csv.DictReader(file)
                   for row in reader:
                       row["poblacion"] = int(row["poblacion"])
                       row["superficie"] = int(row["superficie"])
                       paises.append(row)
            except FileNotFoundError:
                print(f"\n❌ Error: No se encontró el archivo {FILE_LOCATION}")
                continue  # este continue sí es válido porque está dentro del while True del menú
    
            if not paises:
                print("\n📭 No hay países cargados en el sistema.")
                continue
    
            nombre_buscar = input("\nIngrese el nombre del país a buscar (puede ser parcial): ").strip()
            if not nombre_buscar:
                print("\n❌ Nombre no válido.")
                continue
    
            texto = nombre_buscar.lower()
            coincidencias = [p for p in paises if texto in p["nombre"].lower()]
    
            if not coincidencias:
               print(f"\n❌ No se encontró ningún país que contenga '{nombre_buscar}'.")
               continue
    
            print(f"\n🔍 Se encontraron {len(coincidencias)} país(es):")
            for i, p in enumerate(coincidencias, start=1):
                print(f"   {i}. {p['nombre']} - {p['continente']} (población: {p['poblacion']:,})")
    
            if len(coincidencias) == 1:
                elegido = coincidencias[0]
                print("\n→ Único resultado, se seleccionará automáticamente.")
            else:
                elegido = None
                while True:
                    try:
                        opcion = input(f"\nElija el número (1-{len(coincidencias)}) o 0 para cancelar: ").strip()
                        if opcion == "0":
                            break
                        opcion = int(opcion)
                        if 1 <= opcion <= len(coincidencias):
                            elegido = coincidencias[opcion - 1]
                            break
                        print(f"Opción inválida. Debe ser 1-{len(coincidencias)}.")
                    except ValueError:
                        print("Ingrese un número válido.")
    
            if elegido:
                print("\n" + "="*50)
                print("✅ PAÍS SELECCIONADO:")
                print("="*50)
                print(f"   Nombre     : {elegido['nombre']}")
                print(f"   Población  : {elegido['poblacion']:,} hab.")
                print(f"   Superficie : {elegido['superficie']:,} km²")
                print(f"   Continente : {elegido['continente']}")
                print("="*50)
            elif coincidencias:
                print("\n🔁 Búsqueda cancelada.")
        elif int(menu_option) == 5:
            None
        elif int(menu_option) == 6:
            None
        elif int(menu_option) == 7:
            None
        elif int(menu_option) == 8:
            None