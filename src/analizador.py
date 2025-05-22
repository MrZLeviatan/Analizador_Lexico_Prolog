# analizador.py
# English: Lexical analyzer to detect natural and real numbers
# Español: Analizador léxico para detectar números naturales y reales

from tokens.numeros_naturales import es_numero_natural
from tokens.numero_reales import es_numero_real

def analizar_codigo(codigo: str):
    """
    Analiza el código línea por línea y detecta números naturales y reales.
    """
    resultados = []
    palabras = codigo.replace('\n', ' ').split()

    for pos, palabra in enumerate(palabras):
        if es_numero_natural(palabra):
            resultados.append((palabra, "Número Natural", pos))
        elif es_numero_real(palabra):
            resultados.append((palabra, "Número Real", pos))
        else:
            resultados.append((palabra, "Token no reconocido", pos))
    
    return resultados
