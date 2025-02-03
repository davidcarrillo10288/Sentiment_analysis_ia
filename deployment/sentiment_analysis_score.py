from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Inicializar el analizador de sentimientos
analyzer = SentimentIntensityAnalyzer()

def neg(text):
    """
    Calcula la puntuación negativa de un texto.
    
    :param text: Texto a analizar.
    :return: Puntuación negativa multiplicada por la cantidad de palabras.
    """
    scores = analyzer.polarity_scores(text)
    return round(scores['neg'] * len(text.split()))

def neu(text):
    """
    Calcula la puntuación neutral de un texto.
    
    :param text: Texto a analizar.
    :return: Puntuación neutral multiplicada por la cantidad de palabras.
    """
    scores = analyzer.polarity_scores(text)
    return round(scores['neu'] * len(text.split()))

def pos(text):
    """
    Calcula la puntuación positiva de un texto.
    
    :param text: Texto a analizar.
    :return: Puntuación positiva multiplicada por la cantidad de palabras.
    """
    scores = analyzer.polarity_scores(text)
    return round(scores['pos'] * len(text.split()))