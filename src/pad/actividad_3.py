# ========================================================
# ANALÍTICA CON PANDAS - VISUALIZACIÓN PUNTO POR PUNTO
# ========================================================

import pandas as pd
import os

# ===========================
# Punto 1
# ===========================
df = pd.DataFrame({'Granadilla': [55], 'Tomates': [105]})
print("Punto 1 - DataFrame con Granadilla y Tomates:")
print(df)
print("\n" + "-" * 50 + "\n")

# ===========================
# Punto 2
# ===========================
ventas_frutas = pd.DataFrame({
    "Granadilla": [30, 59],
    "Tomates": [100, 150]
}, index=["ventas 2021", "ventas 2022"])
print("Punto 2 - Ventas de Frutas:")
print(ventas_frutas)
print("\n" + "-" * 50 + "\n")

# ===========================
# Punto 3
# ===========================
utensilios = pd.Series(
    ["3 unidades", "2 unidades", "4 unidades", "5 unidades"],
    index=["Cuchara", "Tenedor", "Cuchillo", "Plato"],
    name="Cocina"
)
print("Punto 3 - Utensilios de Cocina:")
print(utensilios)
print("\n" + "-" * 50 + "\n")

# ===========================
# Archivo a utilizar
# ===========================
file_path = "dataset_kaggle.csv"  # Asegúrate de que esté en la misma carpeta del script
# ===========================
# Punto 4 - Mostrar primeras filas del dataset original
# ===========================
try:
    review_temp = pd.read_csv("dataset_kaggle.csv")
    print("Punto 4 - Primeras filas del dataset (Pandas):")
    print(review_temp.head())
    print("\n" + "-" * 50 + "\n")

    # Si estás usando Jupyter Notebook, puedes descomentar esto:
    # from IPython.display import display
    # pd.set_option("display.max_columns", None)
    # pd.set_option("display.width", 1000)
    # styled_df = review_temp.head().style.set_properties(**{
    #     'background-color': 'black',
    #     'color': 'white',
    #     'border-color': 'white'
    # })
    # display(styled_df)

except FileNotFoundError:
    print("Punto 4 - ⚠ El archivo dataset_kaggle.csv no fue encontrado.")
except Exception as e:
    print(f"Punto 4 - ❌ Error al cargar el archivo: {e}")

# ===========================
# Punto 5 al 12 (manejo con try/except)
# ===========================
def cargar_dataset():
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta: {file_path}")
    except Exception as e:
        print(f"Ocurrió un error al cargar el archivo: {e}")
    return None

review = cargar_dataset()
if review is not None:
    # Punto 5
    print("Punto 5 - Primeras filas del dataset:")
    print(review.head())
    print("\n" + "-" * 50 + "\n")

    # Punto 6
    print("Punto 6 - Información del dataset:")
    review.info()
    print("\n" + "-" * 50 + "\n")

    # Punto 7
    average_price = review["price"].mean()
    print(f"Punto 7 - El precio promedio del vino es: {average_price:.2f}")
    print("\n" + "-" * 50 + "\n")

    # Punto 8
    max_price = review["price"].max()
    print(f"Punto 8 - El precio más alto pagado por un vino es: {max_price:.2f}")
    print("\n" + "-" * 50 + "\n")

    # Punto 9
    california_wines = review[review["province"] == "California"]
    print("Punto 9 - Vinos de California:")
    print(california_wines.head())
    print("\n" + "-" * 50 + "\n")

    # Punto 10
    max_price_index = california_wines["price"].idxmax()
    most_expensive_wine = california_wines.loc[max_price_index]
    print("Punto 10 - El vino más caro de California es:")
    print(most_expensive_wine)
    print("\n" + "-" * 50 + "\n")

    # Punto 11
    grape_varieties = california_wines["variety"].value_counts()
    print("Punto 11 - Tipos de uva más comunes en California:")
    print(grape_varieties)
    print("\n" + "-" * 50 + "\n")

    # Punto 12
    top_10_grape_varieties = grape_varieties.head(10)
    print("Punto 12 - Top 10 tipos de uva más comunes en California:")
    print(top_10_grape_varieties)
    print("\n" + "-" * 50 + "\n")

    # ===========================
    # Guardar resultados en carpeta_resultados_3
    # ===========================
    try:
        carpeta_resultados = os.path.join("src", "pad", "carpeta_resultados_3")
        os.makedirs(carpeta_resultados, exist_ok=True)

        ruta_csv = os.path.join(carpeta_resultados, "resultados_analitica_vinos.csv")
        ruta_excel = os.path.join(carpeta_resultados, "resultados_analitica_vinos.xlsx")

        resultados = [
            pd.DataFrame({'Sección': ['Punto 1'], 'Descripción': ['DataFrame con Granadilla y Tomates'], 'Resultado': [df.to_string(index=False)]}),
            pd.DataFrame({'Sección': ['Punto 2'], 'Descripción': ['Ventas de Frutas'], 'Resultado': [ventas_frutas.to_string()]}),
            pd.DataFrame({'Sección': ['Punto 3'], 'Descripción': ['Serie de Utensilios de Cocina'], 'Resultado': [utensilios.to_string()]}),
            pd.DataFrame({'Sección': ['Punto 7'], 'Descripción': ['Precio promedio del vino'], 'Resultado': [f"{average_price:.2f}"]}),
            pd.DataFrame({'Sección': ['Punto 8'], 'Descripción': ['Precio más alto del vino'], 'Resultado': [f"{max_price:.2f}"]}),
            pd.DataFrame({'Sección': ['Punto 10'], 'Descripción': ['Vino más caro de California'], 'Resultado': [most_expensive_wine.to_string()]}),
            pd.DataFrame({'Sección': ['Punto 11'], 'Descripción': ['Tipos de uva más comunes en California'], 'Resultado': [grape_varieties.to_string()]}),
            pd.DataFrame({'Sección': ['Punto 12'], 'Descripción': ['Top 10 tipos de uva más comunes en California'], 'Resultado': [top_10_grape_varieties.to_string()]})
        ]

        resultados_df = pd.concat(resultados, ignore_index=True)
        resultados_df.to_csv(ruta_csv, index=False)
        resultados_df.to_excel(ruta_excel, index=False)

        print(f"✔ Resultados guardados correctamente en:\nCSV: {ruta_csv}\nExcel: {ruta_excel}")

    except Exception as e:
        print(f"Error al guardar los resultados: {e}")

