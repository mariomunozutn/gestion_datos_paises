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
            print("hola mundo")
        elif int(menu_option) == 5:
            None
        elif int(menu_option) == 6:
            None
        elif int(menu_option) == 7:
            None
        elif int(menu_option) == 8:
            None