# cnvierte un diccionario en una cadena de texto, con palabras separadas por comas
# la cadena representa un registro con el formato: "nombre,poblacion,superficie,continente"
def dictionary_to_string(data) -> str:
    dictionary_zise = len(data)
    counter = 0
    new_row = ""
    for key in data:
        counter += 1
        new_row = new_row + data.get(key) 
        # decide si agregar una coma o no. Si es el último elemento del diccionario, no la agrega
        if dictionary_zise != counter:
            new_row = new_row + ","
    return new_row
        