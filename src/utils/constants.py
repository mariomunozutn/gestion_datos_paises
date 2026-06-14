STRING_FIELDS = ["nombre", "continente"]
NUMBER_FIELDS = ["poblacion", "superficie"]

FILTERS = {
    "continente": None,
    "poblacion_min": None,
    "poblacion_max": None,
    "superficie_min": None,
    "superficie_max": None,
}


FILTER_LABELS = {
    "continente": ("continente", "texto"),
    "poblacion_min": ("población mínima", "numero"),
    "poblacion_max": ("población máxima", "numero"),
    "superficie_min": ("superficie mínima", "numero"),
    "superficie_max": ("superficie máxima", "numero"),
}

CSV_HEADERS = ["nombre", "poblacion", "superficie", "continente"]