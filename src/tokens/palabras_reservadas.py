
def es_palabra_reservada(cadena: str) -> bool:
    """
    Verifica si una cadena es una palabra reservada en Prolog.
    Solo se permite usar if/else y comparación carácter por carácter.

    Ejemplo: is / not / halt / true / repeat / retract
    """

    longitud = len(cadena)  # Obtener la longitud de la cadena

    # Palabra reservada: "is"
    if longitud == 2:
        if cadena[0] == 'i':  # Primera letra debe ser 'i'
            if cadena[1] == 's':  # Segunda letra debe ser 's'
                return True  # Es palabra reservada

    # Palabra reservada: "not"
    elif longitud == 3:
        if cadena[0] == 'n':  # Primera letra 'n'
            if cadena[1] == 'o':  # Segunda letra 'o'
                if cadena[2] == 't':  # Tercera letra 't'
                    return True  # Es palabra reservada

    # Palabras reservadas de longitud 4: "true", "fail", "halt"
    elif longitud == 4:
        if cadena[0] == 't':  # Primera letra 't'
            if cadena[1] == 'r':  # Segunda letra 'r'
                if cadena[2] == 'u':  # Tercera letra 'u'
                    if cadena[3] == 'e':  # Cuarta letra 'e'
                        return True  # Es palabra reservada "true"
        else:
            if cadena[0] == 'f':  # Primera letra 'f'
                if cadena[1] == 'a':  # Segunda letra 'a'
                    if cadena[2] == 'i':  # Tercera letra 'i'
                        if cadena[3] == 'l':  # Cuarta letra 'l'
                            return True  # Es palabra reservada "fail"
            else:
                if cadena[0] == 'h':  # Primera letra 'h'
                    if cadena[1] == 'a':  # Segunda letra 'a'
                        if cadena[2] == 'l':  # Tercera letra 'l'
                            if cadena[3] == 't':  # Cuarta letra 't'
                                return True  # Es palabra reservada "halt"

    # Palabras reservadas de longitud 6: "repeat", "assert", "clause"
    elif longitud == 6:
        if cadena[0] == 'r':  # Primera letra 'r'
            if cadena[1] == 'e':  # Segunda letra 'e'
                if cadena[2] == 'p':  # Tercera letra 'p'
                    if cadena[3] == 'e':  # Cuarta letra 'e'
                        if cadena[4] == 'a':  # Quinta letra 'a'
                            if cadena[5] == 't':  # Sexta letra 't'
                                return True  # Es palabra reservada "repeat"
        else:
            if cadena[0] == 'a':  # Primera letra 'a'
                if cadena[1] == 's':  # Segunda letra 's'
                    if cadena[2] == 's':  # Tercera letra 's'
                        if cadena[3] == 'e':  # Cuarta letra 'e'
                            if cadena[4] == 'r':  # Quinta letra 'r'
                                if cadena[5] == 't':  # Sexta letra 't'
                                    return True  # Es palabra reservada "assert"
            else:
                if cadena[0] == 'c':  # Primera letra 'c'
                    if cadena[1] == 'l':  # Segunda letra 'l'
                        if cadena[2] == 'a':  # Tercera letra 'a'
                            if cadena[3] == 'u':  # Cuarta letra 'u'
                                if cadena[4] == 's':  # Quinta letra 's'
                                    if cadena[5] == 'e':  # Sexta letra 'e'
                                        return True  # Es palabra reservada "clause"

    # Palabras reservadas de longitud 7: "consult", "retract"
    elif longitud == 7:
        if cadena[0] == 'c':  # Primera letra 'c'
            if cadena[1] == 'o':  # Segunda letra 'o'
                if cadena[2] == 'n':  # Tercera letra 'n'
                    if cadena[3] == 's':  # Cuarta letra 's'
                        if cadena[4] == 'u':  # Quinta letra 'u'
                            if cadena[5] == 'l':  # Sexta letra 'l'
                                if cadena[6] == 't':  # Séptima letra 't'
                                    return True  # Es palabra reservada "consult"
        else:
            if cadena[0] == 'r':  # Primera letra 'r'
                if cadena[1] == 'e':  # Segunda letra 'e'
                    if cadena[2] == 't':  # Tercera letra 't'
                        if cadena[3] == 'r':  # Cuarta letra 'r'
                            if cadena[4] == 'a':  # Quinta letra 'a'
                                if cadena[5] == 'c':  # Sexta letra 'c'
                                    if cadena[6] == 't':  # Séptima letra 't'
                                        return True  # Es palabra reservada "retract"

    return False  # No es palabra reservada

