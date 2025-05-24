def es_operador_comparativo(cadena: str) -> bool:
    """
    Verifica si una cadena es un operador de comparación válido en Prolog.
    Permitido: "==", "-==", "<", ">", "=<", ">="
    """

    longitud = len(cadena)  # Se obtiene la longitud de la cadena

    # Operadores de un solo carácter
    if longitud == 1:
        if cadena[0] == '>':  # Mayor que
            return True
        elif cadena[0] == '<':  # Menor que
            return True

    # Operadores de dos caracteres
    elif longitud == 2:
        if cadena[0] == '=':
            if cadena[1] == '=':  # Igualdad (==)
                return True
            elif cadena[1] == '<':  # Menor o igual (<=)
                return True

        elif cadena[0] == '>':
            if cadena[1] == '=':  # Mayor o igual (>=)
                return True

    # Operador de tres caracteres: -==
    elif longitud == 3:
        if cadena[0] == '-':
            if cadena[1] == '=':
                if cadena[2] == '=':  # No igualdad (-==)
                    return True

    # Si no coincide con ninguno, no es operador válido
    return False
