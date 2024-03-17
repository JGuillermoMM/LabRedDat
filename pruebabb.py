import streamlit as st
import pandas as pd
from urllib.request import urlopen
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
import json

from streamlit_lottie import st_lottie




# Función para leer y mostrar el contenido del archivo Practica1.py
def leer_archivo_py():
    try:
        with open("Practica1.py", "r") as archivo:
            contenido = archivo.read()
            st.text_area("Contenido del archivo Practica1.py", contenido)
    except FileNotFoundError:
        st.error("El archivo no fue encontrado.")

# Función principal de la aplicación Streamlit
def main():
    st.set_page_config(
        page_title="Practica 1",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Opciones del menú en la barra lateral
    with st.sidebar:
        selected = st.radio('Menú', ["Intro", 'Gráficas', 'Distribución binomial', 'Info'], index=0)

    # Páginas de la aplicación
    if selected == "Intro":
        st.title('Distribución Binomial')
        st.subheader('*asdasdassssssssssssssssssssssssssssssssssss.*')
        st.divider()
        # Aquí puedes agregar el contenido de la página de introducción
    elif selected == 'Gráficas':
        st.title("CSV File Viewer")
        df = pd.read_csv("ConteosDeCarasPorPareja.csv")
        st.dataframe(df)
        st.write(f"El DataFrame tiene {len(df)} filas y {len(df.columns)} columnas.")
    elif selected == 'Distribución binomial':
        leer_archivo_py()
    elif selected == 'Info': 
        st.title('Datos')
        st.markdown("""
            asdasdasdsaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        """)

if __name__ == "__main__":
    main()
