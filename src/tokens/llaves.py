
def es_llave(cadena: str) -> str:
    """
    Devuelve el tipo de llave si corresponde.
    - '{' → 'Llave Abierta'
    - '}' → 'Llave Cerrada'
    
    """

    if cadena == '{':
        return "Llave Abierta"
    elif cadena == '}':
        return "Llave Cerrada"
    return ""