from tokens.numeros_naturales import es_numero_natural
from tokens.numero_reales import es_numero_real
from tokens.identificadores import es_variable, es_atomo
from tokens.palabras_reservadas import es_palabra_reservada
from tokens.operadores_aritmeticos import es_operador_aritmetico
from tokens.operadores_comparacion import es_operador_comparativo
from tokens.operadores_logicos import es_operador_logico
from tokens.operadores_asignacion import es_operador_asignacion
from tokens.llaves import es_llave
from tokens.parentesis import es_parentesis


def analizar_codigo(codigo: str):
    resultados = []
    i = 0
    pos = 0
    longitud = len(codigo)
    llaves_pendientes = []  # Pila para almacenar posiciones de '{' no cerradas
    parentesis_pendientes = [] # Pila para almacenar posiciones de '(' no cerrados

    while i < longitud:
        if codigo[i].isspace():
            i += 1
            continue

        token = ""
        j = i
        detectado = False

        # 🔹 Operadores lógicos
        for log_len in (3, 2, 1):
            if i + log_len <= longitud:
                posible_logico = codigo[i:i+log_len]
                if es_operador_logico(posible_logico):
                    resultados.append((posible_logico, "Operador Lógico", pos))
                    pos += 1
                    i += log_len
                    detectado = True
                    break
        if detectado:
            continue

        # 🔹 Operadores de comparación
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

        # 🔹 Operadores de asignación
        for asig_len in (2, 1):
            if i + asig_len <= longitud:
                posible_asig = codigo[i:i+asig_len]
                if es_operador_asignacion(posible_asig):
                    resultados.append((posible_asig, "Operador de Asignación", pos))
                    pos += 1
                    i += asig_len
                    detectado = True
                    break
        if detectado:
            continue

        # 🔹 "mod" como operador aritmético
        if codigo[i:i+3] == "mod" and es_operador_aritmetico("mod"):
            resultados.append(("mod", "Operador Aritmético", pos))
            pos += 1
            i += 3
            continue

        # 🔹 Palabras reservadas
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

        # 🔹 Identificadores y números alfanuméricos
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

        # 🔹 Caracteres individuales
        if i < longitud:
            c = codigo[i]

            if c == '.' and len(resultados) > 0 and resultados[-1][1] == "Número Natural" and i + 1 < longitud and codigo[i + 1].isdigit():
                anterior = resultados.pop()
                numero = anterior[0]
                i += 1
                decimal = ""
                while i < longitud and codigo[i].isdigit():
                    decimal += codigo[i]
                    i += 1
                resultados.append((numero + '.' + decimal, "Número Real", anterior[2]))

            elif es_operador_aritmetico(c):
                resultados.append((c, "Operador Aritmético", pos))
                i += 1
                pos += 1

            elif c.isdigit():
                resultados.append((c, "Número Natural", pos))
                i += 1
                pos += 1

            elif es_llave(c) == "Llave Abierta":
                llaves_pendientes.append((pos, c))
                resultados.append((c, "Llave Abierta", pos))

                i += 1
                pos += 1

            elif es_llave(c) == "Llave Cerrada":
                if llaves_pendientes:
                    llaves_pendientes.pop()
                    resultados.append((c, "Llave Cerrada", pos))
                else:
                    resultados.append((c, "Token no reconocido", pos))
                i += 1
                pos += 1

            elif es_parentesis(c) == "Parentesis Abierto":
                parentesis_pendientes.append((pos,c))
                resultados.append((c,"Parentesis Abierto",pos))

                i += 1
                pos +=1
            
            elif es_parentesis(c) == "Parentesis Cerrado":
                
                if parentesis_pendientes:
                    parentesis_pendientes.pop()
                    resultados.append((c,"Parentesis Cerrado", pos))
                else:
                    resultados.append((c,"Token no reconocido", pos))

                i += 1
                pos += 1    

            else:
                resultados.append((c, "Token no reconocido", pos))
                i += 1
                pos += 1

    # Verificar llaves sin cerrar
    for posicion, simbolo in llaves_pendientes:
        resultados.append((simbolo, "Llave sin cerrar", posicion))

    # Verificar parentesis sin cerrar 
    for posicion, simbolo in parentesis_pendientes:
        resultados.append((simbolo, "Parentesis sin cerrar", posicion))

    return resultados


def categorizar_token(token: str) -> str:
    if es_palabra_reservada(token):
        return "Palabra Reservada"
    elif es_operador_aritmetico(token):
        return "Operador Aritmético"
    elif es_operador_comparativo(token):
        return "Operador de Comparación"
    elif es_operador_asignacion(token):
        return "Operador de Asignación"
    elif es_operador_logico(token):
        return "Operador Lógico"
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
