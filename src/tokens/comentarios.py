
def es_comentario_valido(codigo: str, i: int, pos: int):
    """
    Verifica si un comentario es válido:
    - Comentarios de una línea empiezan con %
    - Comentarios multilínea empiezan con /* y terminan con */
    - Si dentro del comentario aparece \n como texto, se tokeniza como Separador
    - Si no se cierra el comentario con */, se marca como 'Comentario no completado'
    """

    resultados = []         # Lista de tokens resultantes
    comentario = ""         # Almacena el texto completo del comentario
    contenido = ""          # Almacena solo el contenido del comentario sin delimitadores
    longitud = len(codigo)  # Longitud del código fuente
    cerrada = False         # Indica si un comentario multilínea fue cerrado con */

    # 🔹 Comentario de una línea que comienza con %
    if codigo[i] == '%':
        comentario += '%'   # Agrega el símbolo de inicio del comentario
        i += 1              # Avanza al siguiente carácter
        # Recoge todo hasta que encuentre un salto de línea
        while i < longitud and codigo[i] != '\n':
            contenido += codigo[i]
            comentario += codigo[i]
            i += 1
        # Agrega el token del comentario de una línea
        resultados.append(('%' + contenido, "Comentario", pos))
        pos += 1
        # Si hay salto de línea al final, lo omite
        if i < longitud and codigo[i] == '\n':
            i += 1

    # 🔹 Comentario multilínea que comienza con /*
    elif codigo[i:i+2] == "/*":
        comentario += "/*"  # Agrega delimitador de inicio
        i += 2              # Avanza después de /*
        # Itera hasta encontrar el delimitador de cierre */
        while i < longitud - 1:
            if codigo[i:i+2] == "*/":
                comentario += "*/"  # Añade el cierre
                cerrada = True      # Marca como cerrado
                i += 2
                break

            # Detecta secuencia \n como texto dentro del comentario
            if codigo[i] == '\\' and i + 1 < longitud and codigo[i+1] == 'n':
                comentario += "\\n"
                contenido += ' '  # Reemplaza con espacio en contenido
                resultados.append(('\\n', "Separador", pos))  # Token de separador
                pos += 1
                i += 2
            else:
                comentario += codigo[i]
                contenido += codigo[i]
                i += 1

        # Si el comentario fue cerrado correctamente, se agrega como Comentario
        if cerrada:
            resultados.append(('/*' + contenido + '*/', "Comentario", pos))
        else:
            # Si no se cerró, se marca como Comentario no completado
            resultados.append(('/*' + contenido, "Comentario no completado", pos))
        pos += 1

    return resultados, i, pos
