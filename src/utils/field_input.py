from src.utils.constants import STRING_FIELDS
from src.utils.constants import NUMBER_FIELDS
#from src.utils.field_input import get_n

# decide, según la clave 'key', qué campo debe completarse y ejecuta las funciones con las validaciones correspondientes
def request_field_value(key):
    if key in NUMBER_FIELDS:
        return request_numeric_field(key)
    if key in STRING_FIELDS:
        return request_text_field(key)

# se ejecuta para completar campos de tipo string alfabéticoss, como "nombre" o "continente",
# es decir, solo permite letras
def request_text_field(key) -> str:
   
    if key not in STRING_FIELDS:
        return None
    
    while True:
        input_field = input(f"\nIngrese el valor para el campo '{key}': ")
        if not(input_field.isalpha()):
            print(f"\n[ ERROR ] - El valor ingresado para el campo '{key}' no es válido. Inténtelo nuevamente")
            continue
        break
    return input_field

# se ejecuta para completar campos de tipo string numericos, como "poblacion" o "superficie",
# es decir, solo permite números en los string
def request_numeric_field(key) -> str:

    if key not in NUMBER_FIELDS:
        return None
    
    while True:
        input_field = input(f"\nIngrese el valor para el campo '{key}': ")
        if not(input_field.isdigit()):
            print(f"\n[ ERROR ] - El valor ingresado para el campo '{key}' no es válido. Inténtelo nuevamente")
            continue
        break
    return input_field