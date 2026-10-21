import pandas as pd
import plotly.express as px

# Cargar el dataset, normalizar encabezados y eliminar filas duplicadas
df = pd.read_csv("dataset.csv", sep=";")
df.columns = df.columns.str.strip()
df = df.drop_duplicates()

# Definir la variable objetivo
fc = "Compressive Strength (28-day)(Mpa)"

# Crear el gráfico de línea para mostrar la serie o secuencia de ensayos
fig = px.line(
    df.reset_index(),
    x=df.reset_index().index,
    y=fc,
    title="Serie de Ensayos: Evolución secuencial de la resistencia a la compresión",
    labels={"x": "Número de Ensayo / Registro", fc: "Resistencia a la compresión (MPa)"}
)

# Estilizar la línea del gráfico
fig.update_traces(line=dict(color="#1f77b4", width=2))
fig.update_layout(
    xaxis_title="Secuencia de Muestras en Laboratorio",
    yaxis_title="Resistencia (MPa)",
    plot_bgcolor="white"
)

# Mostrar el gráfico interactivo
fig.show()