import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Definir la ruta para guardar los resultados
carpeta_resultados = os.path.join(os.getcwd(), "src", "pad", "carpeta_resultados")
os.makedirs(carpeta_resultados, exist_ok=True)

# Rutas de exportación
ruta_csv = os.path.join(carpeta_resultados, "resultados.csv")
ruta_excel = os.path.join(carpeta_resultados, "resultados.xlsx")

### Puntos de la tarea ###

# 1. Generar un array de NumPy con valores desde 10 hasta 29.
ej1 = np.arange(10, 30)
print("Punto 1:", ej1)

# 2. Calcular la suma de todos los elementos en un array de NumPy de tamaño 10x10 lleno de unos.
ej2 = np.ones((10, 10)).sum()
print("Punto 2:", ej2)

# 3. Producto elemento a elemento de dos arrays de tamaño 5 llenos de números aleatorios de 1 a 10.
ej3_a = np.random.randint(1, 11, 5)
ej3_b = np.random.randint(1, 11, 5)
ej3_result = ej3_a * ej3_b
print("Punto 3:", ej3_result)

# 4. Crear una matriz de 4x4, donde cada elemento es igual a i+j y calcular su pseudo-inversa.
i = np.arange(4).reshape(4, 1)
j = np.arange(4).reshape(1, 4)
ej4 = i + j  # Matriz generada con i+j
ej4_inv = np.linalg.pinv(ej4)  # Usamos la pseudo-inversa en lugar de la inversa
print("Punto 4: Matriz generada con i+j\n", ej4)
print("Punto 4: Pseudo-inversa de la matriz\n", ej4_inv)

# 5. Encontrar los valores máximo y mínimo en un array de 100 elementos aleatorios y mostrar sus índices.
ej5 = np.random.rand(100)
ej5_max, ej5_min = ej5.max(), ej5.min()
ej5_idx_max, ej5_idx_min = ej5.argmax(), ej5.argmin()
print("Punto 5: Max:", ej5_max, "(índice:", ej5_idx_max, ") Min:", ej5_min, "(índice:", ej5_idx_min, ")")

# 6. Crear un array de tamaño 3x1 y uno de 1x3, sumarlos con broadcasting para obtener un array de 3x3.
ej6_a = np.array([[1], [2], [3]])
ej6_b = np.array([1, 2, 3])
ej6_result = ej6_a + ej6_b
print("Punto 6:\n", ej6_result)

# 7. Extraer una submatriz 2x2 de una matriz 5x5 con números aleatorios.
ej7 = np.random.randint(1, 100, (5, 5))
ej7_submatriz = ej7[1:3, 2:4]
print("Punto 7:\n", ej7_submatriz)

# 8. Crear un array de ceros de tamaño 10 y cambiar los valores en los índices de 3 a 6 a 5.
ej8 = np.zeros(10)
ej8[3:7] = 5
print("Punto 8:", ej8)

# 9. Invertir el orden de las filas en una matriz 3x3.
ej9 = np.random.randint(1, 100, (3, 3))
ej9_inv = ej9[::-1]
print("Punto 9:\n", ej9_inv)

# 10. Seleccionar y mostrar elementos de un array aleatorio de tamaño 10 que sean mayores a 0.5.
ej10 = np.random.rand(10)
ej10_mayores = ej10[ej10 > 0.5]
print("Punto 10:", ej10_mayores)

### Gráficos ###

# 11. Gráfico de dispersión
plt.figure()
plt.scatter(np.random.rand(100), np.random.rand(100), alpha=0.7, color='blue')
plt.title("Punto 11: Gráfico de Dispersión")
ruta_dispersion = os.path.join(carpeta_resultados, "grafico_dispersion.png")
plt.savefig(ruta_dispersion)
plt.close()

# 12. Gráfico de dispersión con función y = sin(x) + ruido
x_12 = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y_12 = np.sin(x_12) + np.random.normal(0, 0.1, size=len(x_12))
plt.figure()
plt.scatter(x_12, y_12, alpha=0.7, color='red')
plt.title("Punto 12: Dispersión con función seno")
plt.savefig(os.path.join(carpeta_resultados, "grafico_seno.png"))
plt.close()

# 13. Gráfico de contorno
x_13 = np.linspace(-2, 2, 100)
y_13 = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x_13, y_13)
Z = np.cos(X) + np.sin(Y)
plt.figure()
plt.contour(X, Y, Z, levels=20, cmap="coolwarm")
plt.colorbar()
plt.title("Punto 13: Gráfico de Contorno")
plt.savefig(os.path.join(carpeta_resultados, "grafico_contorno.png"))
plt.close()

# 14. Gráfico de dispersión con 1000 puntos y colores según densidad
x_14 = np.random.rand(1000)
y_14 = np.random.rand(1000)
colors_14 = np.sqrt(x_14**2 + y_14**2)  # Mejor representación de densidad

plt.figure()
plt.scatter(x_14, y_14, c=colors_14, cmap="viridis", alpha=0.7)
plt.colorbar(label="Densidad")
plt.title("Punto 14: Dispersión con Densidad")
plt.savefig(os.path.join(carpeta_resultados, "grafico_densidad.png"))
plt.close()

# 15. Contorno lleno
plt.figure()
plt.contourf(X, Y, Z, levels=20, cmap="coolwarm")
plt.colorbar()
plt.title("Punto 15: Gráfico de Contorno Lleno")
plt.savefig(os.path.join(carpeta_resultados, "grafico_contorno_lleno.png"))
plt.close()

# 16. Dispersión con etiquetas y leyenda
plt.figure()
plt.scatter(x_12, y_12, alpha=0.7, color='red', label='y = sin(x) + ruido')
plt.plot(x_12, np.sin(x_12), color='black', linestyle='dashed', label='y = sin(x)')
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Punto 16: Dispersión con etiquetas y leyenda")
plt.legend()
plt.savefig(os.path.join(carpeta_resultados, "grafico_etiquetas.png"))
plt.close()

# 17. Histograma con datos distribuidos normalmente
data_17 = np.random.randn(1000)
plt.figure()
plt.hist(data_17, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.xlabel("Valores de la distribución")  # Etiqueta del eje X
plt.ylabel("Frecuencia")  # Etiqueta del eje Y
plt.title("Punto 17: Histograma de distribución normal")
plt.savefig(os.path.join(carpeta_resultados, "histograma_normal.png"))
plt.close()

# 18. Histogramas combinados
data_18a = np.random.randn(1000) * 0.5 + 2
data_18b = np.random.randn(1000) * 0.5 + 5
plt.figure()
plt.hist(data_18a, bins=30, alpha=0.5, color='blue', label="Grupo 1")
plt.hist(data_18b, bins=30, alpha=0.5, color='red', label="Grupo 2")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.legend()
plt.title("Punto 18: Histogramas combinados")
plt.savefig(os.path.join(carpeta_resultados, "histogramas_combinados.png"))
plt.close()

# 19. Histograma con diferentes bins
plt.figure()
plt.hist(data_17, bins=[10, 30, 50], alpha=0.7, color='purple', edgecolor='black')
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.title("Punto 19: Histogramas con diferentes bins")
plt.savefig(os.path.join(carpeta_resultados, "histograma_bins.png"))
plt.close()

# 20. Histograma con línea de media
plt.figure()
plt.hist(data_17, bins=30, alpha=0.7, color='green', edgecolor='black')
plt.axvline(data_17.mean(), color='black', linestyle='dashed', linewidth=2)
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.title("Punto 20: Histograma con media")
plt.savefig(os.path.join(carpeta_resultados, "histograma_media.png"))
plt.close()

# 21. Histogramas superpuestos para los dos sets de datos
plt.figure()
plt.hist(data_18a, bins=30, alpha=0.5, color='blue', label="Grupo 1")
plt.hist(data_18b, bins=30, alpha=0.5, color='red', label="Grupo 2")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.legend()
plt.title("Punto 21: Histogramas Superpuestos")
plt.savefig(os.path.join(carpeta_resultados, "histograma_superpuesto.png"))
plt.close()


print("Todos los resultados han sido guardados correctamente.")

# Guardar los resultados en un DataFrame y exportarlos a CSV y Excel
datos = {
    "Punto 1": [ej1.tolist()],
    "Punto 2": [ej2],
    "Punto 3": [ej3_result.tolist()],
    "Punto 4 - Matriz Original": [ej4.tolist()],
    "Punto 4 - Pseudo-Inversa": [ej4_inv.tolist()],
    "Punto 5 - Máximo": [ej5_max],
    "Punto 5 - Mínimo": [ej5_min],
    "Punto 5 - Índice Máx": [ej5_idx_max],
    "Punto 5 - Índice Mín": [ej5_idx_min],
    "Punto 6": [ej6_result.tolist()],
    "Punto 7": [ej7_submatriz.tolist()],
    "Punto 8": [ej8.tolist()],
    "Punto 9": [ej9_inv.tolist()],
    "Punto 10": [ej10_mayores.tolist()]
}

df = pd.DataFrame.from_dict(datos, orient='index', columns=["Resultado"])
df.to_csv(ruta_csv, index=True)
df.to_excel(ruta_excel, index=True)

print("Resultados guardados en CSV y Excel correctamente.")
