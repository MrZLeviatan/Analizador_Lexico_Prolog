from tokens.numeros_naturales import es_numero_natural
from tokens.numero_reales import es_numero_real
from tokens.identificadores import es_variable, es_atomo
from tokens.palabras_reservadas import es_palabra_reservada
from tokens.simbolos_aritmeticos import es_simbolo_aritmetico
from tokens.operadores_comparacion import es_operador_comparativo

simbolos_validos = ['=', ',', '.', '(', ')', '{', '}', '+', '-', '*', '/', '<', '>', '!']

def analizar_codigo(codigo: str):
    resultados = []
    i = 0
    pos = 0
    longitud = len(codigo)

    while i < longitud:
        if codigo[i].isspace():
            i += 1
            continue

        token = ""
        j = i
        detectado = False

        # Detectar operador de comparación de hasta 3 caracteres
        for op_len in (3, 2, 1):
            if i + op_len <= longitud:
                posible_op = codigo[i:i+op_len]
                if es_operador_comparativo(posible_op):
                    resultados.append((posible_op, "Operador de Comparación", pos))
                    pos += 1
                    i += op_len
                    detectado = True
                    break
        if detectado:
            continue

        # Detectar "mod" como operador aritmético
        if codigo[i:i+3] == "mod" and es_simbolo_aritmetico("mod"):
            resultados.append(("mod", "Operador Aritmético", pos))
            pos += 1
            i += 3
            continue

        # Detectar palabra reservada
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

        # Identificadores y tokens alfanuméricos
        if token.strip() != "":
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
                        dividir_y_agregar(sub_token, pos, resultados)
                        pos += 1
                        sub_token = ""
                        sub_tipo = None
                        continue
                    elif sub_tipo in ["variable", "atomo"] and not (c.isalnum() or c == '_'):
                        dividir_y_agregar(sub_token, pos, resultados)
                        pos += 1
                        sub_token = ""
                        sub_tipo = None
                        continue
                    sub_token += c
                sub_i += 1

            if sub_token != "":
                dividir_y_agregar(sub_token, pos, resultados)
                pos += 1

            i = j
            continue

        # Procesar caracteres individuales
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

            elif es_simbolo_aritmetico(c):
                resultados.append((c, "Operador Aritmético", pos))
                i += 1
                pos += 1

            elif c in simbolos_validos:
                resultados.append((c, "Símbolo", pos))
                i += 1
                pos += 1

            elif c.isdigit():
                resultados.append((c, "Número Natural", pos))
                i += 1
                pos += 1

            else:
                resultados.append((c, "Token no reconocido", pos))
                i += 1
                pos += 1

    return resultados


def categorizar_token(token: str) -> str:
    if es_palabra_reservada(token):
        return "Palabra Reservada"
    elif es_simbolo_aritmetico(token):
        return "Operador Aritmético"
    elif es_operador_comparativo(token):
        return "Operador de Comparación"
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


def dividir_y_agregar(token: str, pos_inicial: int, resultados: list):
    """
    Fragmenta el token en partes de máximo 10 caracteres,
    clasifica cada fragmento y lo agrega a los resultados.
    """
    inicio = 0
    while inicio < len(token):
        fragmento = ""
        contador = 0
        for i in range(inicio, len(token)):
            fragmento += token[i]
            contador += 1
            if contador == 10:
                break
        tipo = categorizar_token(fragmento)
        resultados.append((fragmento, tipo, pos_inicial))
        pos_inicial += 1
        inicio += 10
