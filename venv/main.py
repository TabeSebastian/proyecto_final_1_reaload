from fastapi import FastAPI
import pandas as pd
import json

app = FastAPI()

# Carga el DataFrame con los datos fuera de la función

df_PlayTimeGenre = pd.read_csv('/venv/Include/def PlayTimeGenre_final_listo.csv')

ruta_archivo_json = '/venv/Include/def UserForGenre.json'
with open(ruta_archivo_json, 'r') as archivo_json:
    datosUserForGenre = json.load(archivo_json)

df_UsersRecommend = pd.read_csv('/venv/Include/def UsersRecommend.csv')

df_UsersNotRecommend = pd.read_csv('/venv/Include/bottom_3_por_anio.csv')

df_sentiment_analysis = pd.read_csv('/venv/Include/def sentiment_analysis.csv')


#instanciamos las api y sus rutas

@app.get('/')
def main():
    return {"mensaje": "BIENVENIDOS"}

@app.get('/PlayTimeGenre/{genero}')
def PlayTimeGenre(genero: str):

    # Filtrar el DataFrame por género específico
    df_genero = df_PlayTimeGenre[df_PlayTimeGenre['Genre'] == genero]
    
    if df_genero.empty:
        # Obtener la lista de géneros disponibles en el DataFrame
        generos_disponibles = df_PlayTimeGenre['Genre'].unique().tolist()
        return {"mensaje": "Género inexistente, por favor ingrese un género válido", "generos_disponibles": generos_disponibles}
                
    # Encontrar el año con las horas máximas para el género
    max_year = df_genero[df_genero['Total Hours'] == df_genero['Total Hours'].max()]['Year'].values[0]

    return {"Año de lanzamiento con más horas jugadas para " + genero: int(max_year)}



@app.get('/UserForGenre/{genero}')
def UserForGenre(genero: str):
    if 'Usuario con más horas jugadas para ' + genero not in datosUserForGenre[0]:
        generos_disponibles = list(datosUserForGenre[0].keys())
        return {"mensaje": "Género no encontrado en los datos", "generos_disponibles": generos_disponibles}

    # Busca el usuario con más horas jugadas para el género dado
    usuario_con_mas_horas = datosUserForGenre[0]['Usuario con más horas jugadas para ' + genero]

    # Obtiene la lista de acumulación de horas jugadas por año
    acumulacion_horas_por_anio = datosUserForGenre[0]['Horas jugadas']

    return {
        "Usuario con más horas jugadas para " + genero: usuario_con_mas_horas,
        "Acumulación de horas jugadas por año": acumulacion_horas_por_anio
    }


@app.get('/UsersRecommend/{anio}')
def UsersRecommend(anio: int):
    # Filtra el DataFrame para el año especificado
    df_filtrado = df_UsersRecommend[df_UsersRecommend['Unnamed: 0'] == anio]

    if df_filtrado.empty:
        # Si el filtrado está vacío, devuelve todos los datos de la columna 'Unnamed: 0'
        datos_anios = df_UsersRecommend['Unnamed: 0'].tolist()
        return {"Todos los anios disponibles son ": datos_anios}

    # Si se encontraron datos para el año especificado, selecciona los juegos recomendados
    juegos_recomendados = df_filtrado[['Puesto 1', 'Puesto 2', 'Puesto 3']].iloc[0]

    # Elimina valores NaN si los hubiera
    juegos_recomendados = juegos_recomendados.dropna()

    if juegos_recomendados.empty:
        return {"mensaje": "No se encontraron juegos recomendados para el año especificado"}

    # Convierte la serie de juegos recomendados en una lista
    top_3_juegos = juegos_recomendados.tolist()

    return {"Top 3 juegos recomendados para " + str(anio): top_3_juegos}

@app.get('/UsersNotRecommend/{anio}')
def UsersRecommend(anio: int):
    # Filtra el DataFrame para el año especificado
    df_filtrado = df_UsersNotRecommend[df_UsersNotRecommend['Unnamed: 0'] == anio]

    if df_filtrado.empty:
        # Si el filtrado está vacío, devuelve todos los datos de la columna 'Unnamed: 0'
        datos_anios = df_UsersNotRecommend['Unnamed: 0'].tolist()
        return {"Todos los anios disponibles son ": datos_anios}

    # Si se encontraron datos para el año especificado, selecciona los juegos recomendados
    juegos_recomendados = df_filtrado[['Puesto 1', 'Puesto 2', 'Puesto 3']].iloc[0]

    # Elimina valores NaN si los hubiera
    juegos_recomendados = juegos_recomendados.dropna()


    # Convierte la serie de juegos recomendados en una lista
    top_3_juegos = juegos_recomendados.tolist()

    return {"Top 3 juegos recomendados para " + str(anio): top_3_juegos}

@app.get('/SentimentAnalysis/{anio}')
def sentiment_analysis(anio: int):
    # Filtra el DataFrame para el año especificado
    df_filtrado = df_sentiment_analysis[df_sentiment_analysis['Unnamed: 0'] == anio]

    if df_filtrado.empty:
        # Si el filtrado está vacío, devuelve todos los datos de la columna 'Unnamed: 0'
        datos_anios = df_sentiment_analysis['Unnamed: 0'].tolist()
        return {"Todos los años disponibles son": datos_anios}

    # Si se encontraron datos para el año especificado, selecciona el análisis de sentimiento
    analisis_sentimiento = df_filtrado[['Positive', 'Negative']].iloc[0]

    # Elimina valores NaN si los hubiera
    analisis_sentimiento = analisis_sentimiento.dropna()

    if analisis_sentimiento.empty:
        return {"mensaje": "No se encontró análisis de sentimiento para el año especificado"}

    # Convierte la serie de análisis de sentimiento en un diccionario
    analisis_dict = analisis_sentimiento.to_dict()

    return {"Análisis de sentimiento para el año " + str(anio): analisis_dict}
