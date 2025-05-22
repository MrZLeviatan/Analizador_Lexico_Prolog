# Módulo para identificar variables y átomos de Prolog

def es_variable(cadena: str) -> bool:
    
    """
    Verifica si una cadena es una variable en Prolog.
    Comienza con mayúscula o guion bajo, seguida de letras, dígitos o guion bajo.

    Ejemplo: X / _aux / Var123
    """
    if len(cadena) == 0:
        return False

    primera = cadena[0]
    if not (primera == '_' or ('A' <= primera <= 'Z')):
        return False

    for char in cadena[1:]:
        if not (
            ('a' <= char <= 'z') or
            ('A' <= char <= 'Z') or
            ('0' <= char <= '9') or
            (char == '_')
        ):
            return False

    return True


def es_atomo(cadena: str) -> bool:
    """
    Verifica si una cadena es un átomo en Prolog.
    Comienza con minúscula, seguida de letras, dígitos o guion bajo.
    """
    if len(cadena) == 0:
        return False

    primera = cadena[0]
    if not ('a' <= primera <= 'z'):
        return False

    for char in cadena[1:]:
        if not (
            ('a' <= char <= 'z') or
            ('A' <= char <= 'Z') or
            ('0' <= char <= '9') or
            (char == '_')
        ):
            return False

    return True
