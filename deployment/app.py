import streamlit as st
from transformers import pipeline
import requests
import joblib
import io
import pandas as pd
import numpy as np
import textblob
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
import re
import string
import sklearn
import emoji
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import math
from num2words import num2words
from sklearn.preprocessing import StandardScaler

import warnings
warnings.filterwarnings('ignore')


#################################################################
## Eliminando stopwords
import nltk
# Descargar recursos de NLTK (solo la primera vez)
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords = stopwords.words('english')

#################################################################
## Buscamos reducir a su forma base las palabras
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

#################################################################
## Analizando cantidad de palabras positivas-negativas-neutras en la frase
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()


#################################################################
## cargar modelos entrenados en colab
@st.cache_resource
def cargar_modelo_vectorizer():
    # URL del archivo en GitHub (en formato "raw")
    url = "https://github.com/davidcarrillo10288/Sentiment_analysis_ia/raw/master/countvectorizer.pkl"
    
    # Descargar el archivo
    response = requests.get(url)
    response.raise_for_status()  # Verifica que la descarga fue exitosa
    
    # Cargar el modelo desde el contenido descargado
    modelo = joblib.load(io.BytesIO(response.content))
    return modelo

@st.cache_resource
def cargar_modelo_clasificador():
    # URL del archivo en GitHub (en formato "raw")
    url = "https://github.com/davidcarrillo10288/Sentiment_analysis_ia/raw/master/modelo_entrenado_countvectorizer.pkl"
    
    # Descargar el archivo
    response = requests.get(url)
    response.raise_for_status()  # Verifica que la descarga fue exitosa
    
    # Cargar el modelo desde el contenido descargado
    modelo = joblib.load(io.BytesIO(response.content))
    return modelo

# Cachear el modelo desde Hugging face
@st.cache_resource
def cargar_modelo():
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

@st.cache_resource
def emotion_model():
    # Cargar un modelo preentrenado de análisis de emociones
    return pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

#################################################################

# Cargar los modelos a utilizar
classifier = cargar_modelo()
vectorizer = cargar_modelo_vectorizer()
clasificador = cargar_modelo_clasificador()
emotion_m = emotion_model()

#################################################################


#################################################################
######################FUNCIONES A UTILIZAR#######################
#################################################################
from clean_text import clean_text
from sentiment_analysis_score import neg, pos, neu
from emotion_classification import split_text_into_chunks, detect_emotion_chunks
#################################################################
######################FUNCIONES A UTILIZAR#######################
#################################################################


def prediccion(texto, vectorizador, stemmer, neg, neu, pos, detect_emotion_chunks):
    texto_limpio = clean_text(texto)
    texto_limpio_2 = ' '.join([word for word in texto_limpio.split() if word not in (nltk.corpus.stopwords.words('english'))])
    texto_limpio_3 = ' '.join([stemmer.stem(word) for word in texto_limpio_2.split()])
    bolsa_frases = vectorizer.transform([texto_limpio_3])
    matriz_frases = pd.DataFrame.sparse.from_spmatrix(bolsa_frases, columns=vectorizador.get_feature_names_out())
    matriz_frases['num_palabras'] = len(texto_limpio_3.split())
    matriz_frases['palabras_unicas'] = len(set(texto_limpio_3.split()))
    matriz_frases['polaridad'] = TextBlob(texto_limpio_3).sentiment.polarity
    matriz_frases['subjetividad'] = TextBlob(texto_limpio_3).sentiment.subjectivity
    matriz_frases['neg_words'] = neg(texto_limpio_3)
    matriz_frases['neu_words'] = neu(texto_limpio_3)
    matriz_frases['pos_words'] = pos(texto_limpio_3)
    matriz_frases['emotion'] = detect_emotion_chunks(texto_limpio_3, emotion_m, split_text_into_chunks)
    matriz_frases = pd.get_dummies(matriz_frases, columns=['emotion'])
    matriz_frases = matriz_frases.astype(int)

    ## Asegurandome tener las mismas columnas que en el modelo cargado
    emociones_completas = [
        "emotion_anger",
        "emotion_fear",
        "emotion_joy",
        "emotion_love",
        "emotion_sadness",
        "emotion_surprise"
    ]
    existing_columns = matriz_frases.columns
    existing_emotions = [emotion for emotion in emociones_completas if emotion in existing_columns]

    matriz_frases = matriz_frases.reindex(columns=matriz_frases.drop(columns=existing_emotions).columns.tolist() + emociones_completas, fill_value=0)

    return clasificador.predict(matriz_frases)


###################################################################################################################
########################################################-STREAMLIT-################################################
###################################################################################################################

# Configurar el tamaño de la ventana de Streamlit
# st.set_page_config(
#     page_title="Analizador de Sentimientos",
#     page_icon="��",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# URL de la imagen en GitHub (en formato "raw")
image_principal = "https://github.com/davidcarrillo10288/Sentiment_analysis_ia/raw/master/principal_image.jpg"
image_url_negative = "https://github.com/davidcarrillo10288/Sentiment_analysis_ia/raw/master/negative.png"
image_url_positive = "https://github.com/davidcarrillo10288/Sentiment_analysis_ia/raw/master/positive.jpg"

# Interfaz de Streamlit
st.title("SENTIMENT ANALYSIS IN COMMENTS")
st.image(image_principal)
texto = st.text_input("Write a phrase:")

if texto:

    # Crear dos columnas para mostrar los resultados
    col1, col2 = st.columns(2)

    with col1:
        resultado = classifier(texto)
        st.subheader("Hugging Face Model:")
        if resultado[0]['label'].lower() == 'positive' or resultado[0]['label'].lower() == 'positivo':
            st.write("Sentiment:", resultado[0]['label'])
            st.image(image_url_positive, caption="Github image", width=300)
        else:
            st.write("Sentiment:", resultado[0]['label'])
            st.image(image_url_negative, caption="Github image", width=300)

    with col2:
        resultado_2 = prediccion(texto, vectorizer, stemmer, neg, neu, pos, detect_emotion_chunks)
        st.subheader("Machine Learning Model:")
        if resultado_2[0].lower() == 'positive' or resultado_2[0].lower() =='positivo':
            st.write("Sentiment:", (resultado_2[0]).upper())
            st.image(image_url_positive, caption="Github image", width=300)
        else:
            st.write("Sentiment:", (resultado_2[0]).upper())
            st.image(image_url_negative, caption="Github image", width=300)
        
