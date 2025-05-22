# =Módulo para validar números naturales

def es_numero_natural(cadena: str) -> bool:

    # Verifica si una cadena es un número natural (entero positivo)
    return cadena.isdigit()
