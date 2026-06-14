from src.utils.field_input import request_field_value
from src.repositories.country_repository import find_all_countries_map, update_country


# ticker UPT1-4
# Se deben desarrollar las siguientes 2 funcionalidades del menú
#   - Actualizar población
#   - Actualizar  superficie de un país existente


def update_country_data() -> None:
    countries_tuple = find_all_countries_map()
    # una lista de objetos [{indice, {key,value}}]
    country_name_by_index = countries_tuple[0]
    # objeto: {contryName, country_data}
    country_name_by_name = countries_tuple[1]
    
    print(f"\n[ DEBE ELEGIR UN PAIS Y ACTUALIZAR SUS DATOS ]")
    
    index = 0
    know_idices = []
    
    print(f"| Indice{' ' * (16 - len('Indice')) }| País{' ' * ( 16 - len('pais')) }|")
    print(f"{"-" * 35}")
    for country in country_name_by_index:
        
        index += 1
        know_idices.append(index) # una lista de variables para validar las opciones validas de un menu
        country_name = country.get(index)

        print(f"| {index}{' '*(16  - len(str(index)))}| {country_name}{' '*(15  - len(str(country_name)))} |")

    while True:
        number_index = input("\nEsperando indice del país: ")

        if not(number_index.isdigit() and int(number_index) > 0 and int(number_index) in know_idices):
            print("\n[ ERROR ] - Indice inválido. Inténtelo nuevamente")
            continue
        else:
            break
    
    key_name = country_name_by_index[int(number_index)-1].get(int(number_index)) 
    country_data = country_name_by_name.get(key_name)
   
   # se escpecica dict[str, str | None] sino nvim se queja   
    update_data_request:dict[str, str | None] = {
        "poblacion": None,
        "superficie": None
    }

    # solo permitir editar 2 propiedades
    for key in update_data_request:
        while True:
            confirmar = input(f"\n¿Desea actualizar '{key}'? (Y/N): ")
            if confirmar.upper() in ["Y", "N"]:
                break
            print(f"\n[ ERROR ] - Opción inválida. Ingrese Y o N")

        if confirmar.upper() != "Y":
            continue
        
        update_data_request[key] = request_field_value(key)
        
    update_country(key_name, update_data_request) 
    print(f"\n[ ÉXITO] - El registro de '{key_name}' ha sido actualizado correctamente")