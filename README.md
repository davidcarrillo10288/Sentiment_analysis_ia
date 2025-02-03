# ANÁLISIS DE SENTIMIENTO

Link: https://sentiment-analysis-comments.streamlit.app/

El objetivo de este proyecto es realizar un análisis de sentimientos en los comentarios, clasificándolos en categorías de positivos o negativos, para comprender mejor las emociones y opiniones expresadas en los textos.

## Descripción:

Este proyecto es una aplicación web desarrollada con Streamlit que permite analizar el sentimiento de comentarios escritos por los usuarios. Utiliza modelos preentrenados de Hugging Face y modelos personalizados cargados desde un repositorio en GitHub para determinar si un comentario es positivo o negativo. Además, incorpora análisis de emociones mediante distilbert-base-uncased-emotion.

## Características:

  * Clasificación de sentimiento: Predice si un texto es positivo o negativo.

  * Análisis de emociones: Identifica emociones como alegría, tristeza, miedo, amor, sorpresa o ira.

  * Limpieza de texto: Preprocesamiento avanzado de texto, eliminando URLs, menciones, emojis y más.

  * Modelos personalizados: Carga y uso de modelos entrenados previamente almacenados en GitHub.

  * Interfaz interactiva con Streamlit.

## Tecnologías utilizadas:

  ### Librerías principales:
  
  * streamlit - Para la interfaz interactiva.
  
  * transformers - Modelos de Hugging Face.
  
  * sklearn - Para la vectorización y clasificación del texto.
  
  * textblob - Análisis de polaridad y subjetividad.
  
  * nltk - Procesamiento de lenguaje natural.
  
  * vaderSentiment - Análisis de sentimiento basado en reglas.
  
  * num2words - Conversión de números a palabras.
  
  * emoji - Eliminación de emojis en el texto.
  
  * joblib - Carga de modelos serializados.
  
  * requests - Descarga de modelos desde GitHub.

![image](https://github.com/user-attachments/assets/cf3ac285-bb2a-41db-9e61-5fd1f4400e5a)

### DEPLOYMENT

![image](https://github.com/user-attachments/assets/5e2e5bb6-dddf-4697-9862-d94058c4c6eb)


