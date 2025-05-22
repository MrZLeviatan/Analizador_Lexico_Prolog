# analizador.py
# English: Lexical analyzer for Prolog numbers and identifiers
# Español: Analizador léxico para números e identificadores de Prolog

from tokens.numeros_naturales import es_numero_natural
from tokens.numero_reales import es_numero_real
from tokens.identificadores import es_variable, es_atomo

def analizar_codigo(codigo: str):
    """
    Analiza el código y detecta números y identificadores de Prolog.
    """
    resultados = []
    palabras = codigo.replace('\n', ' ').split()

    for pos, palabra in enumerate(palabras):
        if es_numero_natural(palabra):
            resultados.append((palabra, "Número Natural", pos))
        elif es_numero_real(palabra):
            resultados.append((palabra, "Número Real", pos))
        elif es_variable(palabra):
            resultados.append((palabra, "Variable", pos))
        elif es_atomo(palabra):
            resultados.append((palabra, "Átomo", pos))
        else:
            resultados.append((palabra, "Token no reconocido", pos))
    
    return resultados

