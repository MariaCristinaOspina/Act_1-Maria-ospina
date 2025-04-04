# Importar librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import re
import os

# ---------------- CARGAR LOS DATOS ---------------- #
# Primero, cargamos el dataset que contiene información sobre los K-Dramas.
# La ruta del archivo debe estar en la misma carpeta del script.
file_path = "/workspaces/Act_1-Maria-ospina/src/pad/kdrama_DATASET.csv"


# Verificamos si el archivo existe
if not os.path.exists(file_path):
    print(f"Error: No se encontró el archivo '{file_path}'. Asegúrate de que está en la misma carpeta que este script.")
    exit()

df = pd.read_csv(file_path)

# ---------------- ENTENDIENDO EL DATASET ---------------- #
# Vamos a revisar cómo luce la información en las primeras filas.
print(df.head())

# Ahora, vemos información general del dataset, como cuántos datos hay y qué tipos de valores tiene.
df.info()

# Revisamos si hay valores nulos en el dataset. Esto nos ayuda a saber qué datos faltan.
print("\nValores nulos:")
print(df.isnull().sum())

# Revisamos si hay filas repetidas para evitar información duplicada.
print("\nFilas duplicadas:", df.duplicated().sum())

# Por último, vemos un resumen estadístico de los datos numéricos.
print(df.describe())

# ---------------- LIMPIEZA DE DATOS ---------------- #
# Ahora toca limpiar los datos para que sean más fáciles de analizar.

# Eliminamos las filas duplicadas para que no haya información repetida.
df = df.drop_duplicates()

# Rellenamos los valores vacíos con información más útil en lugar de dejarlos en blanco.
df.fillna({
    'Description': 'No description available',  # Si falta la descripción, ponemos un mensaje por defecto.
    'Rating': df['Rating'].mean(),  # Si falta la calificación, usamos el promedio.
    'Genre': 'Unknown',
    'Actors': 'Unknown',
    'Tags': 'Unknown'
}, inplace=True)

# Eliminamos filas que estén completamente vacías.
df.dropna(how='all', inplace=True)

# Algunas columnas pueden tener errores en los nombres, los corregimos.
df.rename(columns={'Titile': 'Title', 'Year of release': 'Year of Release'}, inplace=True)

# Convertimos algunos datos a números enteros para que sean más fáciles de manejar.
df['Year of Release'] = df['Year of Release'].fillna(0).astype(int)
df['Number of Episodes'] = df['Number of Episodes'].fillna(0).astype(int)

# A veces, hay caracteres raros en los textos. Los eliminamos para que sean más fáciles de leer.
text_columns = ['Title', 'Description', 'Genre', 'Actors', 'Tags']
for col in text_columns:
    df[col] = df[col].astype(str).apply(lambda x: re.sub(r'[^a-zA-Z0-9, ]', '', x))

# Revisamos nuevamente la información para confirmar que los cambios se hicieron bien.
df.info()

# ---------------- VISUALIZACIÓN DE DATOS ---------------- #
# Ahora vamos a hacer gráficos para entender mejor la información.

# Distribución de calificaciones
plt.figure(figsize=(10,5))
sns.histplot(df['Rating'], bins=20, kde=True, color="blue")
plt.title("Distribución de Calificaciones", fontsize=14)
plt.xlabel("Calificación", fontsize=12)
plt.ylabel("Cantidad", fontsize=12)
plt.show()

# Número de dramas lanzados por año
df['Year of Release'] = df['Year of Release'].astype(str)  # Convertimos a texto para graficar
plt.figure(figsize=(12,6))
sns.countplot(y=df['Year of Release'], order=df['Year of Release'].value_counts().index, palette="coolwarm")
plt.title("Número de Dramas Estrenados por Año", fontsize=14)
plt.xlabel("Cantidad", fontsize=12)
plt.ylabel("Año", fontsize=12)
plt.show()

# Géneros más comunes
genre_counts = df['Genre'].str.split(', ').explode().value_counts().head(10)
plt.figure(figsize=(12,6))
sns.barplot(x=genre_counts.values, y=genre_counts.index, palette="mako")
plt.title("Los 10 Géneros Más Comunes", fontsize=14)
plt.xlabel("Cantidad", fontsize=12)
plt.ylabel("Género", fontsize=12)
plt.show()

# ---------------- ANÁLISIS DE DATOS ---------------- #
# Finalmente, sacamos algunas conclusiones interesantes sobre los K-Dramas.

# Top 5 dramas con mejor calificación
top_dramas = df[['Title', 'Rating']].sort_values(by='Rating', ascending=False).head(5)
print("Top 5 dramas mejor calificados:\n", top_dramas)

print("\nConclusiones:")

# Datos generales
print(f"Total de Dramas: {df.shape[0]}")
print(f"Títulos Únicos: {df['Title'].nunique()}")
print(f"Calificación Promedio: {df['Rating'].mean():.2f}")

# Género más popular
most_common_genre = df['Genre'].str.split(', ').explode().mode()[0]
print(f"Género Más Popular: {most_common_genre}")

# Año más antiguo y más reciente
print(f"Drama Más Antiguo: {df['Year of Release'].min()}")
print(f"Drama Más Reciente: {df['Year of Release'].max()}")

# Drama con mejor calificación
top_drama = df.loc[df['Rating'].dropna().idxmax()]
print(f"Drama Mejor Calificado: {top_drama['Title']} ({top_drama['Rating']})")

# ---------------- GUARDAR RESULTADOS ---------------- #

# Crear carpeta si no existe
output_folder = "/workspaces/Act_1-Maria-ospina/src/pad/resultados_proyecto_integrador"
os.makedirs(output_folder, exist_ok=True)

# Guardar el dataframe limpio completo
df.to_csv(os.path.join(output_folder, "kdrama_limpio.csv"), index=False)

# Guardar el top 5 de dramas mejor calificados
top_dramas.to_csv(os.path.join(output_folder, "top_5_dramas.csv"), index=False)

# Guardar las gráficas como imágenes
# Gráfico 1: Distribución de calificaciones
plt.figure(figsize=(10,5))
sns.histplot(df['Rating'], bins=20, kde=True, color="blue")
plt.title("Distribución de Calificaciones", fontsize=14)
plt.xlabel("Calificación", fontsize=12)
plt.ylabel("Cantidad", fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "grafico_calificaciones.png"))
plt.close()

# Gráfico 2: Número de dramas lanzados por año
df['Year of Release'] = df['Year of Release'].astype(str)
plt.figure(figsize=(12,6))
sns.countplot(y=df['Year of Release'], order=df['Year of Release'].value_counts().index, palette="coolwarm")
plt.title("Número de Dramas Estrenados por Año", fontsize=14)
plt.xlabel("Cantidad", fontsize=12)
plt.ylabel("Año", fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "grafico_dramas_por_año.png"))
plt.close()

# Gráfico 3: Géneros más comunes
genre_counts = df['Genre'].str.split(', ').explode().value_counts().head(10)
plt.figure(figsize=(12,6))
sns.barplot(x=genre_counts.values, y=genre_counts.index, palette="mako")
plt.title("Los 10 Géneros Más Comunes", fontsize=14)
plt.xlabel("Cantidad", fontsize=12)
plt.ylabel("Género", fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "grafico_generos_comunes.png"))
plt.close()

print(f"\n✅ Todos los resultados y gráficos han sido guardados en:\n{output_folder}")


# ---------------- GUARDAR CONCLUSIONES ---------------- #

# Obtener los datos clave para las conclusiones
total_dramas = df.shape[0]
titulos_unicos = df['Title'].nunique()
calificacion_promedio = df['Rating'].mean()
genero_mas_popular = df['Genre'].str.split(', ').explode().mode()[0]
anio_mas_antiguo = df['Year of Release'].min()
anio_mas_reciente = df['Year of Release'].max()
drama_top = df.loc[df['Rating'].idxmax()]
titulo_top = drama_top['Title']
calificacion_top = drama_top['Rating']

# Crear el texto de conclusiones
conclusiones = f"""Conclusiones:
Total de Dramas: {total_dramas}
Títulos Únicos: {titulos_unicos}
Calificación Promedio: {calificacion_promedio:.2f}
Género Más Popular: {genero_mas_popular}
Drama Más Antiguo: {anio_mas_antiguo}
Drama Más Reciente: {anio_mas_reciente}
Drama Mejor Calificado: {titulo_top} ({calificacion_top})
"""

# Guardar en archivo .csv
conclusiones_path = os.path.join(output_folder, "conclusiones.csv")
with open(conclusiones_path, "w", encoding="utf-8") as f:
    f.write(conclusiones)

print("\n✅ Conclusiones guardadas correctamente en 'conclusiones.csv'")
