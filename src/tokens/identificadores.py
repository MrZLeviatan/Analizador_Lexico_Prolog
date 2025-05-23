def es_variable(cadena: str) -> bool:

    """
    Verifica si una cadena es una variable en Prolog.
    Reglas:
    - Debe comenzar con una letra mayúscula o con un guion bajo.
    - Puede estar seguida de letras (mayúsculas o minúsculas), dígitos o guiones bajos.
    
    Ejemplos válidos: "X", "_aux", "Var123"
    """
    
    if len(cadena) == 0:
        # Si la cadena está vacía, no puede ser una variable válida
        return False

    primera = cadena[0]  # Se obtiene el primer carácter de la cadena

    if not (primera == '_' or ('A' <= primera <= 'Z')):
        # Si el primer carácter no es un guion bajo ni una letra mayúscula, no es variable
        return False

    for char in cadena[1:]:
        # Se recorren los caracteres restantes
        if not (
            ('a' <= char <= 'z') or    # Letras minúsculas
            ('A' <= char <= 'Z') or    # Letras mayúsculas
            ('0' <= char <= '9') or    # Dígitos
            (char == '_')              # Guion bajo
        ):
            # Si encuentra un carácter inválido, no es una variable válida
            return False

    return True  # Todos los caracteres cumplen las reglas → es una variable válida



def es_atomo(cadena: str) -> bool:

    """
    Verifica si una cadena es un átomo en Prolog.
    Reglas:
    - Debe comenzar con una letra minúscula.
    - Puede estar seguida de letras, dígitos o guiones bajos.
    
    Ejemplos válidos: "atom", "valor1", "dato_aux"
    """
    
    if len(cadena) == 0:
        # Si la cadena está vacía, no puede ser un átomo válido
        return False

    primera = cadena[0]  # Se obtiene el primer carácter de la cadena

    if not ('a' <= primera <= 'z'):
        # Si el primer carácter no es una letra minúscula, no es un átomo válido
        return False

    for char in cadena[1:]:
        # Se recorren los caracteres restantes
        if not (
            ('a' <= char <= 'z') or    # Letras minúsculas
            ('A' <= char <= 'Z') or    # Letras mayúsculas
            ('0' <= char <= '9') or    # Dígitos
            (char == '_')              # Guion bajo
        ):
            # Si encuentra un carácter inválido, no es un átomo válido
            return False

    return True  # Todos los caracteres cumplen las reglas → es un átomo válido
