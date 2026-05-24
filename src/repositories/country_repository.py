from src.utils.dict_parser import dictionary_to_string
import csv

# ESTE ARCHIVO SOLO DEBE TENER EL CODIGO PARA LEER, GUARDAR Y ACTULIZAR UN REGISTRO DEL ARCHIVO CSV

FILE_LOCATION = "data/paises.csv"

# guarda la información en el archivo csv
def save_new_country(country_data):
    new_row = dictionary_to_string(country_data)
    with open(FILE_LOCATION, "a", newline="", encoding="utf-8") as file:
        file.write("\n")
        file.write(new_row)

# Devuelve una lsita con todos lo nombre de los paises        
def find_all_countries_map() -> list:
    country_name_by_index = []
    country_data_by_name = {}
    log_index = 1

    with open(FILE_LOCATION, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file) 
        for row in reader:
            country_name = row.get("nombre")
            country_name_by_index.append({log_index: country_name})
            country_data_by_name[country_name] = dict(row) 
            log_index += 1

    return country_name_by_index, country_data_by_name

#actualza la superficie y población de un pais
def update_country(country_name: str, new_data: dict) -> None:
    rows = []
    with open(FILE_LOCATION, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        for row in reader:
            if row.get("nombre", "").strip() == country_name.strip():
                if new_data.get("poblacion") is not None:
                    row["poblacion"] = new_data.get("poblacion")
                if new_data.get("superficie") is not None:
                    row["superficie"] = new_data.get("superficie")
            rows.append(row)

    with open(FILE_LOCATION, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)