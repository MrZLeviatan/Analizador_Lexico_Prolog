# Módulo para validar números reales en Prolog

def es_numero_real(cadena: str) -> bool:
    
    """
    Verifica si una cadena es un número real válido en Prolog.
    Reglas:
    - Debe contener exactamente un punto.
    - Debe tener al menos un dígito antes y después del punto.

    Ejemplos: 12.3 / 3.24 /. 6.66
    
    """
    # Módulo para validar números reales en Prolog

def es_numero_real(cadena: str) -> bool:
    """
    Verifica si una cadena es un número real válido en Prolog.
    Reglas:
    - Debe contener exactamente un punto.
    - Debe tener al menos un dígito antes y después del punto.
    """

    punto_encontrado = False        # Bandera para indicar si ya se encontró un punto
    digitos_antes = 0               # Contador de dígitos antes del punto
    digitos_despues = 0            # Contador de dígitos después del punto
    despues_del_punto = False      # Bandera para saber si se están procesando los dígitos después del punto

    for char in cadena:         # For de toda la vida
        if char == '.':
            if punto_encontrado:
                # Si ya se encontró un punto anteriormente, entonces hay más de uno → inválido
                return False
            punto_encontrado = True    # Se marca que se ha encontrado el punto
            despues_del_punto = True  # Se activa el procesamiento de la parte decimal
        elif char >= '0' and char <= '9':
            if not punto_encontrado:
                digitos_antes += 1    # Se cuenta un dígito en la parte entera
            else:
                digitos_despues += 1  # Se cuenta un dígito en la parte decimal
        else:
            # Si el carácter no es un punto ni un dígito → inválido
            return False

    # Validar que se haya encontrado un solo punto y que haya al menos un dígito en cada lado
    if punto_encontrado and digitos_antes >= 1 and digitos_despues >= 1:
        return True
    else:
        return False


