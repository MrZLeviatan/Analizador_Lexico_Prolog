from tokens.numeros_naturales import es_numero_natural
from tokens.numero_reales import es_numero_real
from tokens.identificadores import es_variable, es_atomo

simbolos_validos = ['=', ',', '.', '(', ')', '{', '}', '+', '-', '*', '/', '<', '>', '!']

def analizar_codigo(codigo: str):
    resultados = []
    token = ""
    tipo_token = None  # "numero", "variable", "atomo"
    pos = 0
    i = 0
    longitud = len(codigo)

    while i < longitud:
        char = codigo[i]

        if char.isalnum() or char == '_':
            if token == "":
                # Determinar el tipo al ver el primer caracter
                if char.isdigit():
                    tipo_token = "numero"
                elif char == '_' or ('A' <= char <= 'Z'):
                    tipo_token = "variable"
                elif 'a' <= char <= 'z':
                    tipo_token = "atomo"
                token += char
                i += 1
            else:
                if tipo_token == "numero" and not char.isdigit():
                    # Se corta el número si hay letra
                    resultados.append((token, "Número Natural", pos))
                    pos += 1
                    token = ""
                    tipo_token = None
                elif tipo_token == "variable" and not (char.isalnum() or char == '_'):
                    resultados.append((token, "Variable", pos))
                    pos += 1
                    token = ""
                    tipo_token = None
                elif tipo_token == "atomo" and not (char.isalnum() or char == '_'):
                    resultados.append((token, "Átomo", pos))
                    pos += 1
                    token = ""
                    tipo_token = None
                else:
                    token += char
                    i += 1
        elif char == '.':
            if token.isdigit() and i + 1 < longitud and codigo[i + 1].isdigit():
                token += '.'
                i += 1
                token += codigo[i]
                i += 1
                resultados.append((token, "Número Real", pos))
                pos += 1
                token = ""
                tipo_token = None
            else:
                if token != "":
                    resultados.append((token, categorizar_token(token), pos))
                    pos += 1
                    token = ""
                    tipo_token = None
                resultados.append(('.', "Símbolo", pos))
                pos += 1
                i += 1
        else:
            if token != "":
                resultados.append((token, categorizar_token(token), pos))
                pos += 1
                token = ""
                tipo_token = None
            if char.strip() != "":
                if char in simbolos_validos:
                    resultados.append((char, "Símbolo", pos))
                elif char.isdigit():
                    resultados.append((char, "Número Natural", pos))
                else:
                    resultados.append((char, "Token no reconocido", pos))
                pos += 1
            i += 1

    if token != "":
        resultados.append((token, categorizar_token(token), pos))

    return resultados

def categorizar_token(token: str) -> str:
    if es_numero_real(token):
        return "Número Real"
    elif es_numero_natural(token):
        return "Número Natural"
    elif es_variable(token):
        return "Variable"
    elif es_atomo(token):
        return "Átomo"
    else:
        return "Token no reconocido"
