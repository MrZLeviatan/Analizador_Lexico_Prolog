
def es_operador_asignacion(cadena: str) -> bool:
    """
    Verifica si una cadena es un operador de asignación en Prolog.
    Permitidos: '=', ':=' e 'is'
    """

    # Si la cadena tiene un solo carácter y es el signo igual (=)
    if len(cadena) == 1 and cadena[0] == '=':
        return True

    # Si la cadena tiene dos caracteres
    elif len(cadena) == 2:
        # Verifica si es el operador := (asignación de valor)
        if cadena[0] == ':' and cadena[1] == '=':
            return True
        # Verifica si es la palabra 'is' (asignación aritmética en Prolog)
        elif cadena[0] == 'i' and cadena[1] == 's':
            return True

    # Si no coincide con ningún operador válido de asignación
    return False

