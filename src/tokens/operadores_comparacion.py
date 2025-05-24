def es_operador_comparativo(cadena : str) -> bool:
    """
    Verifica si una cadena es un operador de comparación valido en Prolog.
    Permitido: "==, "-==", "<", ">", "=<", ">="
    """

    longitud = len(cadena)

    if longitud == 1:
        if cadena[0] == '>':
            return True
        elif cadena[0] == '<':
            return True
    elif longitud == 2:
        if cadena [0] == '=':
            if cadena[1] == '=':
                return True
            elif cadena [1] == '<':
                return True
            
        elif cadena [0] == '>':
            if cadena [1] == '=':
                return True
            
    elif longitud == 3:
        if cadena[0] == '-':
            if cadena [1] == '=':
                if cadena [2] == '=':
                    return True

    return False