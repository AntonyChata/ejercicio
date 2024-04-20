import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Generar datos de ejemplo para diferentes tipos de gráficos
np.random.seed(0)
n_points = 100
data_scatter = {
    'x': np.random.randn(n_points),
    'y': np.random.randn(n_points),
    'category': np.random.choice(['A', 'B', 'C'], size=n_points)
}
data_histogram = {
    'value': np.random.randn(n_points)
}
data_boxplot = {
    'category': np.random.choice(['X', 'Y', 'Z'], size=n_points),
    'value': np.random.exponential(size=n_points)
}
df_scatter = pd.DataFrame(data_scatter)
df_histogram = pd.DataFrame(data_histogram)
df_boxplot = pd.DataFrame(data_boxplot)

# Definir la aplicación Streamlit
def main():
    st.title("Visualizaciones Interactivas")

    # Gráfico de Dispersión
    st.subheader("Gráfico de Dispersión")
    scatter_plot = px.scatter(df_scatter, x='x', y='y', color='category', title='Gráfico de Dispersión')
    st.plotly_chart(scatter_plot)

    # Histograma
    st.subheader("Histograma")
    histogram = px.histogram(df_histogram, x='value', title='Histograma')
    st.plotly_chart(histogram)

    # Diagrama de Caja
    st.subheader("Diagrama de Caja")
    boxplot = px.box(df_boxplot, x='category', y='value', color='category', title='Diagrama de Caja')
    st.plotly_chart(boxplot)

if __name__ == '__main__':
    main()
