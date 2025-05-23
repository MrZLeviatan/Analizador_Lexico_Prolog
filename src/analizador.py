from tokens.numeros_naturales import es_numero_natural
from tokens.numero_reales import es_numero_real
from tokens.identificadores import es_variable, es_atomo
from tokens.palabras_reservadas import es_palabra_reservada

simbolos_validos = ['=', ',', '.', '(', ')', '{', '}', '+', '-', '*', '/', '<', '>', '!']

def analizar_codigo(codigo: str):
    resultados = []
    i = 0
    pos = 0
    longitud = len(codigo)

    while i < longitud:
        token = ""
        j = i
        detectado = False

        # Intentar detectar palabra reservada de izquierda a derecha
        while j < longitud and (codigo[j].isalnum() or codigo[j] == '_'):
            token += codigo[j]
            if es_palabra_reservada(token):
                resultados.append((token, "Palabra Reservada", pos))
                pos += 1
                i = j + 1
                detectado = True
                break
            j += 1

        if detectado:
            continue

        if token != "":
            # Fragmentar secuencia tipo 23A2isnot
            sub_i = 0
            sub_token = ""
            sub_tipo = None
            while sub_i < len(token):
                c = token[sub_i]
                if sub_token == "":
                    if c.isdigit():
                        sub_tipo = "numero"
                    elif c == '_' or ('A' <= c <= 'Z'):
                        sub_tipo = "variable"
                    elif 'a' <= c <= 'z':
                        sub_tipo = "atomo"
                    sub_token += c
                else:
                    if sub_tipo == "numero" and not c.isdigit():
                        resultados.append((sub_token, categorizar_token(sub_token), pos))
                        pos += 1
                        sub_token = ""
                        sub_tipo = None
                        continue
                    elif sub_tipo in ["variable", "atomo"] and not (c.isalnum() or c == '_'):
                        resultados.append((sub_token, categorizar_token(sub_token), pos))
                        pos += 1
                        sub_token = ""
                        sub_tipo = None
                        continue
                    sub_token += c
                sub_i += 1

            if sub_token != "":
                # Intentar detectar palabras reservadas dentro del resto
                temp_i = 0
                while temp_i < len(sub_token):
                    acumulado = ""
                    k = temp_i
                    while k < len(sub_token):
                        acumulado += sub_token[k]
                        if es_palabra_reservada(acumulado):
                            resultados.append((acumulado, "Palabra Reservada", pos))
                            pos += 1
                            temp_i = k + 1
                            break
                        k += 1
                    else:
                        # No es palabra reservada, construir token válido
                        fragmento = ""
                        while temp_i < len(sub_token) and not es_palabra_reservada(sub_token[temp_i:]):
                            fragmento += sub_token[temp_i]
                            temp_i += 1
                        if fragmento != "":
                            resultados.append((fragmento, categorizar_token(fragmento), pos))
                            pos += 1
                i = j
                continue

        if i < longitud and (codigo[i].isalnum() or codigo[i] == '_'):
            i += 1
            continue

        if i < longitud:
            c = codigo[i]
            if c == '.':
                if len(resultados) > 0 and resultados[-1][1] == "Número Natural" and i + 1 < longitud and codigo[i + 1].isdigit():
                    anterior = resultados.pop()
                    numero = anterior[0]
                    i += 1
                    decimal = ""
                    while i < longitud and codigo[i].isdigit():
                        decimal += codigo[i]
                        i += 1
                    resultados.append((numero + '.' + decimal, "Número Real", anterior[2]))
                else:
                    resultados.append(('.', "Símbolo", pos))
                    i += 1
                    pos += 1
            elif c.strip() != "":
                if c in simbolos_validos:
                    resultados.append((c, "Símbolo", pos))
                elif c.isdigit():
                    resultados.append((c, "Número Natural", pos))
                else:
                    resultados.append((c, "Token no reconocido", pos))
                i += 1
                pos += 1
            else:
                i += 1  # espacios y tabulaciones

    return resultados


def categorizar_token(token: str) -> str:
    if es_palabra_reservada(token):
        return "Palabra Reservada"
    elif es_numero_real(token):
        return "Número Real"
    elif es_numero_natural(token):
        return "Número Natural"
    elif es_variable(token):
        return "Variable"
    elif es_atomo(token):
        return "Átomo"
    else:
        return "Token no reconocido"
