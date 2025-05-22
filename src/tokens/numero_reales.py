# número_real.py
# English: Module to validate real numbers
# Español: Módulo para validar números reales

def es_numero_real(cadena: str) -> bool:
    """
    Verifica si una cadena representa un número real válido.
    Nota: Acepta números como 12.3, 0.56, .78, 45.
    """
    punto_encontrado = False
    digitos = 0

    for i, char in enumerate(cadena):
        if char == '.':
            if punto_encontrado:
                return False
            punto_encontrado = True
        elif char.isdigit():
            digitos += 1
        else:
            return False

    return punto_encontrado and digitos >= 1
