
def es_operador_logico(cadena: str) -> bool:
    """
    Verifica si una cadena es un operador lógico válido de Prolog.
    Permitido: ",", ";", "->", "\+"
    """

    longitud = len(cadena)  # Se obtiene la longitud de la cadena

    # Operadores lógicos de un solo carácter
    if longitud == 1:
        if cadena[0] == ',' or cadena[0] == ';':  # Coma (conjunción) o punto y coma (disyunción)
            return True

    # Operadores lógicos de dos caracteres
    elif longitud == 2:
        if cadena[0] == '\\' and cadena[1] == '+':  # Negación lógica (\+)
            return True
        elif cadena[0] == '-' and cadena[1] == '>':  # Implicación (->)
            return True

    # Si no coincide con ninguno de los operadores válidos
    return False
