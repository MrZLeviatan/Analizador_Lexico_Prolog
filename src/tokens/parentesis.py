
def es_parentesis(cadena: str) -> str:
    """
    Devuelve el tipo de parentesis si corresponde.
    - '(' → 'Parentesis Abierto'
    - ')' → 'Parentesis Cerrado'
    
    """

    if cadena == '(':
        return "Parentesis Abierto"
    elif cadena == ')':
        return "Parentesis Cerrado"
    return ""