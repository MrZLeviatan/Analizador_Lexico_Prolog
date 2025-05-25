
def es_cadena_valida(codigo: str, i: int, pos: int):
    """
    Verifica si una cadena de caracteres es válida:
    - Debe comenzar y terminar con comillas dobles.
    - Puede contener caracteres escapados como: \", \n, \t, \\
    - Muestra el contenido limpio sin secuencias \n o \t (reemplazados por espacio)
    - Retorna un token indicando si la cadena está completa o no.
    """

    resultados = []          # Lista para almacenar los tokens resultantes
    cadena = '"'            # Token de la cadena con comillas incluidas
    contenido = ""          # Contenido limpio de la cadena para mostrar al usuario
    longitud = len(codigo)  # Longitud total del código fuente
    i += 1                  # Saltar la comilla inicial que ya fue detectada
    cerrada = False         # Bandera para indicar si la cadena fue cerrada correctamente

    while i < longitud:
        c = codigo[i]
        if c == '\\':  # Detecta secuencias de escape
            i += 1
            if i < longitud:
                esc = codigo[i]
                if esc == 'n':        # Secuencia \n: salto de línea reemplazado por espacio
                    resultados.append(('\\n', "Separador", pos))
                    contenido += ' '
                    cadena += '\\n'   # Mantener en token para el lexer
                    pos += 1
                elif esc == 't':      # Secuencia \t: tabulación reemplazada por espacio
                    resultados.append(('\\t', "Separador", pos))
                    contenido += ' '
                    cadena += '\\t'
                    pos += 1
                elif esc == '"':      # Comilla doble escapada \" se convierte en espacio visible
                    resultados.append(('\\\"', "Separador", pos))
                    contenido += ' '
                    cadena += '\\"'
                    pos += 1
                elif esc == '\\':     # Barra invertida escapada \\ también convertida en espacio visible
                    resultados.append(('\\\\', "Separador", pos))
                    contenido += ' '
                    cadena += '\\\\'
                    pos += 1
                else:
                    # Para otras secuencias, se mantiene tal cual
                    contenido += '\\' + esc
                    cadena += '\\' + esc
                
        elif c == '"':  # Comilla de cierre encontrada: cadena completa
            cadena += '"'
            cerrada = True
            i += 1
            break
        else:
            # Caracter normal, se agrega al contenido y token
            contenido += c
            cadena += c
        i += 1

    # Agrega un token con el contenido limpio entre comillas para mostrar
    if cerrada:
        resultados.append(('\"' + contenido + '\"', "Cadena de Caracteres", pos))
    else:
        # Si no se cerró la cadena, se marca como cadena no completada
        resultados.append(('\"' + contenido, "Cadena no completada", pos))

    pos += 1
    return resultados, i, pos
