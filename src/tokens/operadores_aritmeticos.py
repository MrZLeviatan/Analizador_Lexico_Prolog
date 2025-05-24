def es_operador_aritmetico(cadena: str) -> bool:
    """
    Verifica si una cadena es un símbolo aritmético válido en Prolog.
    Permitido: "+", "-", "*", "/", "mod"
    """

    longitud = len(cadena)  # Obtener la longitud de la cadena

    # Símbolos aritméticos de un solo carácter
    if longitud == 1:
        if cadena[0] == '+':  # Verifica si es '+'
            return True
        elif cadena[0] == '-':  # Verifica si es '-'
            return True
        elif cadena[0] == '*':  # Verifica si es '*'
            return True
        elif cadena[0] == '/':  # Verifica si es '/'
            return True

    # Símbolo aritmético especial de tres caracteres: "mod"
    elif longitud == 3:
        if cadena[0] == 'm':  # Primera letra 'm'
            if cadena[1] == 'o':  # Segunda letra 'o'
                if cadena[2] == 'd':  # Tercera letra 'd'
                    return True  # Es "mod"

    return False  # No es símbolo aritmético válido


        
    
