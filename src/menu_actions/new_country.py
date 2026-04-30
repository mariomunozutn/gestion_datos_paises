from src.utils.field_input import request_field_value
from src.repositories.country_repository import save_new_country

# los datos serán solicitados cuando se llame a esta función
def create_new_country() -> None:
    request_data = {
        "nombre": None,
        "poblacion": None,
        "superficie": None,
        "continente": None
    }

    for key in request_data:
        # request_field_value completa el campo correspondiente a cada iteración
        request_data[key] = request_field_value(key)
    
    save_new_country(request_data)
    print(f"\n[ NUEVO PAIS ({request_data.get('nombre')}) GUARDADO CORRECTAMENTE ]")