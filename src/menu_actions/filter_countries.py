from src.repositories.country_repository import find_countries_by_filters
from src.utils.field_input import request_numeric_field, request_text_field
from src.utils.constants import FILTERS, FILTER_LABELS

import csv
def filter_countries() -> None:
    
    paises = []
    try:
        with open("data/paises.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                fila["poblacion"] = int(fila["poblacion"])
                fila["superficie"] = int(fila["superficie"])
                paises.append(fila)
    except:
        print("\nError al abrir el archivo")
        return
    
    if len(paises) == 0:
        print("\nNo hay países cargados")
        return
    
    continente = None
    pob_min = None
    pob_max = None
    sup_min = None
    sup_max = None
    
    print("\n[ FILTRAR PAÍSES ]")
    
    while True:
        opcion = input("\n¿Filtrar por continente? [Y/N]: ").strip().upper()
        if opcion == "Y" or opcion == "N":
            break
        print("Solo Y o N")
    if opcion == "Y":
        continente = input("Continente: ").strip().lower()
    
    while True:
        opcion = input("\n¿Filtrar por población mínima? [Y/N]: ").strip().upper()
        if opcion == "Y" or opcion == "N":
            break
        print("Solo Y o N")
    if opcion == "Y":
        while True:
            try:
                pob_min = int(input("Población mínima: "))
                break
            except:
                print("Número válido")
    
    while True:
        opcion = input("\n¿Filtrar por población máxima? [Y/N]: ").strip().upper()
        if opcion == "Y" or opcion == "N":
            break
        print("Solo Y o N")
    if opcion == "Y":
        while True:
            try:
                pob_max = int(input("Población máxima: "))
                break
            except:
                print("Número válido")
    
    while True:
        opcion = input("\n¿Filtrar por superficie mínima? [Y/N]: ").strip().upper()
        if opcion == "Y" or opcion == "N":
            break
        print("Solo Y o N")
    if opcion == "Y":
        while True:
            try:
                sup_min = int(input("Superficie mínima (km cuadrados): "))
                break
            except:
                print("Número válido")
    
    while True:
        opcion = input("\n¿Filtrar por superficie máxima? [Y/N]: ").strip().upper()
        if opcion == "Y" or opcion == "N":
            break
        print("Solo Y o N")
    if opcion == "Y":
        while True:
            try:
                sup_max = int(input("Superficie máxima (km²): "))
                break
            except:
                print("Número válido")
    
    resultados = paises.copy()
    
    if continente:
        nuevos = []
        for p in resultados:
            if p["continente"].lower() == continente:
                nuevos.append(p)
        resultados = nuevos
    
    if pob_min is not None:
        nuevos = []
        for p in resultados:
            if p["poblacion"] >= pob_min:
                nuevos.append(p)
        resultados = nuevos
    
    if pob_max is not None:
        nuevos = []
        for p in resultados:
            if p["poblacion"] <= pob_max:
                nuevos.append(p)
        resultados = nuevos
    
    if sup_min is not None:
        nuevos = []
        for p in resultados:
            if p["superficie"] >= sup_min:
                nuevos.append(p)
        resultados = nuevos
    
    if sup_max is not None:
        nuevos = []
        for p in resultados:
            if p["superficie"] <= sup_max:
                nuevos.append(p)
        resultados = nuevos
    
    print("\n" + "=" * 50)
    print(f"Resultados: {len(resultados)} paises")
    print("=" * 50)
    
    if len(resultados) == 0:
        print("No hay resultados")
    else:
        for p in resultados:
            print(p["nombre"] + " | Poblacion: " + str(p["poblacion"]) + " | Superficie: " + str(p["superficie"]) + " km² | " + p["continente"])
    
    print("=" * 50)