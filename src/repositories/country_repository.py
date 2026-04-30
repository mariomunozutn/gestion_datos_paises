from src.utils.dict_parser import dictionary_to_string

# ESTE ARCHIVO SOLO DEBE TENER EL CODIGO PARA LEER, GUARDAR Y ACTULIZAR UN REGISTRO DEL ARCHIVO CSV

FILE_LOCATION = "data/paises.csv"

# guarda la información en el archivo csv
def save_new_country(country_data):
    new_row = dictionary_to_string(country_data) # convierte de diccionario a string. Plabras separadas por ','
    with open(FILE_LOCATION,"a") as file:
        file.write("\n")
        file.write(new_row)