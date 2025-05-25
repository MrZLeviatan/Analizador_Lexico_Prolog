# Listas de caracteres válidos para el análisis
LETRAS_MAYUS = [
    'A','B','C','D','E','F','G','H','I','J','K','L',
    'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

LETRAS_MINUS = [
    'a','b','c','d','e','f','g','h','i','j','k','l',
    'm','n','o','p','q','r','s','t','u','v','w','x','y','z'
]

DIGITOS = ['0','1','2','3','4','5','6','7','8','9']

GUION_BAJO = '_'


def es_variable(cadena: str) -> bool:
    """
    Verifica si una cadena es una variable en Prolog.
    - Debe comenzar con letra mayúscula o '_'
    - Puede tener letras, dígitos o '_' después
    - Máximo 10 caracteres
    """

    if len(cadena) == 0 or len(cadena) > 10:
        return False

    primer = cadena[0]

    # Verificar primer carácter: letra mayúscula o guion bajo
    primero_valido = False
    if primer == GUION_BAJO:
        primero_valido = True
    else:
        for letra in LETRAS_MAYUS:
            if primer == letra:
                primero_valido = True
                break

    if not primero_valido:
        return False

    # Verificar caracteres restantes: mayúsculas, minúsculas, dígitos o guion bajo
    for c in cadena[1:]:
        valido = False

        for letra in LETRAS_MAYUS:
            if c == letra:
                valido = True
                break

        if not valido:
            for letra in LETRAS_MINUS:
                if c == letra:
                    valido = True
                    break

        if not valido:
            for d in DIGITOS:
                if c == d:
                    valido = True
                    break

        if not valido and c == GUION_BAJO:
            valido = True

        if not valido:
            return False

    return True


def es_atomo(cadena: str) -> bool:
    """
    Verifica si una cadena es un átomo en Prolog.
    - Debe comenzar con letra minúscula
    - Puede tener letras, dígitos o '_' después
    - Máximo 10 caracteres
    """

    if len(cadena) == 0 or len(cadena) > 10:
        return False

    primer = cadena[0]

    # Verificar primer carácter: letra minúscula
    primero_valido = False
    for letra in LETRAS_MINUS:
        if primer == letra:
            primero_valido = True
            break

    if not primero_valido:
        return False

    # Verificar caracteres restantes: mayúsculas, minúsculas, dígitos o guion bajo
    for c in cadena[1:]:
        valido = False

        for letra in LETRAS_MAYUS:
            if c == letra:
                valido = True
                break

        if not valido:
            for letra in LETRAS_MINUS:
                if c == letra:
                    valido = True
                    break

        if not valido:
            for d in DIGITOS:
                if c == d:
                    valido = True
                    break

        if not valido and c == GUION_BAJO:
            valido = True

        if not valido:
            return False

    return True
