# ANÁLISIS DE SENTIMIENTO

Link: https://sentiment-analysis-comments.streamlit.app/

## DESCRIPCIÓN:

Este proyecto es una aplicación web desarrollada con Streamlit que permite analizar el sentimiento de comentarios escritos por los usuarios. Utiliza modelos preentrenados de Hugging Face y modelos personalizados cargados desde un repositorio en GitHub para determinar si un comentario es positivo o negativo. Además, incorpora análisis de emociones mediante distilbert-base-uncased-emotion.

![image](https://github.com/user-attachments/assets/cf3ac285-bb2a-41db-9e61-5fd1f4400e5a)

## CARACTERÍSTICAS:

```plaintext
Sentiment_analysis_ia/
│
├── deployment/
│   ├── .streamlit/
│   ├── app.py
│   ├── clean_text.py
│   ├── emotion_classification.py
│   ├── requirements.txt
│   ├── sentiment_analysis_score.py
```

  * <ins>Clasificación de sentimiento:</ins> Predice si un texto es positivo o negativo.

  * <ins>Análisis de emociones:</ins> Identifica emociones como alegría, tristeza, miedo, amor, sorpresa o ira.

  * <ins>Limpieza de texto:</ins> Preprocesamiento avanzado de texto, eliminando URLs, menciones, emojis y más.

  * <ins>Modelos personalizados:</ins> Carga y uso de modelos entrenados previamente almacenados en GitHub.

  * Interfaz interactiva con Streamlit.

## TECNOLOGÍAS UTILIZADAS:

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

## INSTALACIÓN: 

Para ejecutar este proyecto en tu máquina local, sigue estos pasos:

 * Clona el repositorio:
  ```bash
  git clone https://github.com/davidcarrillo10288/Sentiment_analysis_ia.git
  ```
 * Instala las dependencias necesarias:
  ```bash
  pip install -r requirements.txt
  ```
 * Ejecuta la aplicación:
  ```bash
  streamlit run app.py
  ```
## USO:

  * Escribe una frase en el cuadro de texto de la aplicación.
  
  * Se analizará el sentimiento utilizando el modelo de Hugging Face.
  
  * Se mostrará la predicción del modelo personalizado entrenado.
  
  * Se desplegará la emoción dominante en el texto ingresado.

## MODELOS UTILIZADOS: 

 * <ins>Clasificador de sentimientos:</ins> distilbert-base-uncased-finetuned-sst-2-english (Hugging Face)
 
 * <ins>Modelo de emociones:</ins> bhadresh-savani/distilbert-base-uncased-emotion
 
 * <ins>Modelo personalizado:</ins> modelo_entrenado_countvectorizer.pkl (entrenado previamente y almacenado en GitHub)

### DEPLOYMENT: 

 * POSITIVO

![image](https://github.com/user-attachments/assets/db35f1af-0dba-468a-b8e8-701cf2837ac7)

 * NEGATIVO

![image](https://github.com/user-attachments/assets/a95a8698-6379-470c-b3d9-415b9ee575f4)





