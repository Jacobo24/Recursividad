def dicotomia(tabla, t):
    izquierda = 0 # Inicio de la tabla
    derecha = len(tabla) - 1 # Final de la tabla
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if tabla[medio] == t:
            return medio # Para devolver la posición en la que se encuentra el elemento en la tabla
        elif tabla[medio] < t:
            izquierda = medio + 1 # Para que no se repita el elemento de en medio
        else:
            derecha = medio - 1 # Para que no se repita el elemento de en medio

    return "No encontrado"