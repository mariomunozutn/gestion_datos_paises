from src.repositories.country_repository import find_countries_by_filters
from src.utils.field_input import request_numeric_field, request_text_field
from src.utils.constants import FILTERS, FILTER_LABELS, CSV_HEADERS

def filter_countries() -> None: 
    filters = dict(FILTERS)

    print(f"\n[ FILTRAR PAÍSES ]")

    # desempaquetar los valores de la tupla "continente": ("continente", "texto"),
    for key, (label, type) in FILTER_LABELS.items():
        
        while True:
            answer = input(f"\n¿Desea filtrar por '{label}'? [Y/N]: ")
            if answer.upper() in ["Y", "N"]:
                break
            print(f"\n[ ERROR ] - Opción inválida. Ingrese Y o N")

        if answer.upper() != "Y":
            continue

        if type == "texto":
            filters[key] = request_text_field("continente")
        else:
            filters[key] = request_numeric_field(label)

    results = find_countries_by_filters(filters)

    print(f"\n[ RESULTADOS DE LA BUSQUEDA - {len(results)} ]")
    print(f"| {'Nombre'}{' ' * (16 - len('Nombre'))}| {'Poblacion'}{' ' * (16 - len('Poblacion'))}| {'Superficie'}{' ' * (16 - len('Superficie'))}| {'Continente'}{' ' * (16 - len('Continente'))}|")
    print(f"{'-' * 75}")
    for country in results:
        nombre     = country.get('nombre', '').strip()
        poblacion  = country.get('poblacion', '').strip()
        superficie = country.get('superficie', '').strip()
        continente = country.get('continente', '').strip()
        print(f"| {nombre}{' ' * (16 - len(nombre))}| {poblacion}{' ' * (16 - len(poblacion))}| {superficie}{' ' * (16 - len(superficie))}| {continente}{' ' * (15 - len(continente))} |")