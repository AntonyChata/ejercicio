import streamlit as st
import pandas as pd
import plotly.graph_objs as go

# Incorporar datos
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Diseño de la aplicación
st.title('Exploración de Datos Mundiales')

# Agregar controles para la interacción
col_chosen = st.radio('Selecciona una columna para visualizar', ['pop', 'lifeExp', 'gdpPercap'])

# Gráfico de dispersión interactivo
st.subheader('Gráfico de Dispersión')
x_variable = st.selectbox('Selecciona variable para eje X', ['gdpPercap', 'lifeExp'])
y_variable = st.selectbox('Selecciona variable para eje Y', ['pop', 'lifeExp'])

# Crear la figura de Plotly
scatter_fig = go.Figure()

# Agregar trazas de dispersión a la figura
for continent in df['continent'].unique():
    df_continent = df[df['continent'] == continent]
    scatter_fig.add_trace(go.Scatter(x=df_continent[x_variable], y=df_continent[y_variable], mode='markers', name=continent))

# Actualizar el diseño y los ejes
scatter_fig.update_layout(title=f'{y_variable} vs {x_variable}', xaxis_title=x_variable, yaxis_title=y_variable)

# Mostrar el gráfico de Plotly
st.plotly_chart(scatter_fig)

# Mostrar datos en tabla
st.subheader('Datos')
st.write(df)
