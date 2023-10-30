Sistema de Recomendación de Videojuegos para Steam


Este proyecto es un Sistema de Recomendación de Videojuegos desarrollado como parte del trabajo de un Data Scientist en Steam, 
una plataforma multinacional de videojuegos. 
El objetivo de este sistema es recomendar juegos a los usuarios en función de sus preferencias y reseñas.

Contenido
Descripción
Requerimientos
Transformaciones
Desarrollo de la API
Deployment
Análisis Exploratorio de los Datos (EDA)
Modelo de Aprendizaje Automático
Funcionalidades de la API


1. Descripción
Este proyecto se creó para abordar la necesidad de Steam de proporcionar recomendaciones de videojuegos personalizadas a sus usuarios.
El ciclo de vida de un proyecto de Machine Learning abarca desde la recolección y el tratamiento de datos hasta el entrenamiento y el mantenimiento
del modelo a medida que llegan nuevos datos.

3. Requerimientos
Para llevar a cabo este proyecto, se establecieron los siguientes requerimientos:

Transformaciones: Se trabajó en la lectura del dataset en el formato correcto y en la eliminación de las columnas innecesarias para optimizar el rendimiento de la API 
y el entrenamiento del modelo.

Desarrollo de la API: Se implementó una API utilizando el framework FastAPI que proporciona varias funcionalidades, como la obtención del año con más horas jugadas 
para un género, la identificación del usuario con más horas jugadas para un género, la recomendación de los juegos más recomendados y no recomendados por los usuarios, 
y el análisis de sentimiento de reseñas por año.

Machine Learning de Recomendación: Se desarrolló un sistema de recomendación de videojuegos que incluye dos enfoques: el sistema de recomendación Item-Item, 
que recomienda juegos similares a un juego dado, y el sistema de recomendación User-Item, que recomienda juegos a un usuario basándose en usuarios similares y 
sus preferencias de juego.

3. Transformaciones
La sección de "Transformaciones" describe las acciones realizadas para asegurarse de que los datos se ajusten a las necesidades del proyecto.
Esto incluye la preparación de los datos para su uso en el desarrollo de la API y el modelo de recomendación.

5. Desarrollo de la API
La API resultante se puede implementar en una variedad de servicios, como Render, Railway o cualquier otro que permita el acceso a la API desde la web.

6. Deployment
7. Análisis Exploratorio de los Datos (EDA)
Antes de entrenar el modelo, se realizó un análisis exploratorio de los datos para investigar relaciones entre las variables, identificar outliers y buscar patrones
interesantes. Esto se hizo manualmente para comprender mejor los datos.

9. Modelo de Aprendizaje Automático
Se creó un modelo de recomendación de videojuegos basado en dos enfoques:

Sistema de Recomendación Item-Item: Recomienda juegos similares a un juego dado utilizando la similitud del coseno.

Sistema de Recomendación User-Item: Recomienda juegos a un usuario basándose en usuarios similares y sus preferencias de juego.

Ambos sistemas de recomendación se implementaron y se agregaron a la API.

8. Funcionalidades de la API
La API ofrece las siguientes funcionalidades:

recomendacion_juego(id de producto): Devuelve una lista con 5 juegos recomendados similares al juego ingresado.

recomendacion_usuario(id de usuario): Devuelve una lista con 5 juegos recomendados para el usuario ingresado.

Además, se han agregado las siguientes funciones:

PlayTimeGenre(genero: str): Devuelve el año con más horas jugadas para un género dado.

UserForGenre(genero: str): Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

UsersRecommend(año: int): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado .

UsersNotRecommend(año: int): Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado .

sentiment_analysis(año: int): Según el año de lanzamiento, devuelve una lista con la cantidad de registros de reseñas de usuarios categorizados con un análisis de sentimiento.

La API es accesible según los criterios de API REST o RESTful y puede ser consumida desde cualquier dispositivo conectado a Internet.

Este proyecto ha permitido mejorar la experiencia de juego para los usuarios de Steam al proporcionar recomendaciones personalizadas basadas en sus preferencias y reseñas, 
destacando la transformación de datos como un elemento clave en su éxito.
