# =Módulo para validar números naturales

def es_numero_natural(cadena: str) -> bool:

    """
    Verifica si una cadena es un número natural válido en Prolog.
    Reglas:
    - Debe contener numeros del 0 - 9 y sus variables.
    - No pueden ser negativos.

    Ejemplos: 666 / 123 / 2 
    
    """
     
    return cadena.isdigit()
