def split_text_into_chunks(text, max_tokens=512):
    """
    Divide un texto en fragmentos de un tamaño máximo de tokens.
    
    :param text: Texto a dividir.
    :param max_tokens: Número máximo de tokens por fragmento (por defecto 512).
    :return: Lista de fragmentos de texto.
    """
    words = text.split()  # Dividimos el texto en palabras
    chunks = [" ".join(words[i:i + max_tokens]) for i in range(0, len(words), max_tokens)]
    return chunks

def detect_emotion_chunks(text, emotion_m, split_text_into_chunks):
    """
    Detecta la emoción dominante en un texto dividiéndolo en fragmentos.
    
    :param text: Texto a analizar.
    :return: Emoción dominante en el texto.
    """
    # Dividir en fragmentos
    chunks = split_text_into_chunks(text, max_tokens=512)

    # Procesar cada fragmento y obtener emociones
    emotions = [emotion_m(chunk, truncation=True)[0]['label'] for chunk in chunks]

    # Combinar emociones: la más frecuente (puedes usar otras reglas)
    dominant_emotion = max(set(emotions), key=emotions.count)
    return dominant_emotion