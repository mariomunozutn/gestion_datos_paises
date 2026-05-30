from src.menu_actions.new_country import create_new_country
from src.menu_actions.update_country_data import update_country_data
from src.menu_actions.filter_countries import filter_countries
from src.menu_actions.statistics import display_statistics
from src.menu_actions.find_country import search_country
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
            search_country() 
        elif int(menu_option) == 4:
            filter_countries()
        elif int(menu_option) == 5:
            sort_countries()
        elif int(menu_option) == 6:
            display_statistics() 
        elif int(menu_option) == 7:
            print("[ CERRANDO PROGRAMA ...]")
            break