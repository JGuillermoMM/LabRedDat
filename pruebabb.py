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

# Layout
st.set_page_config(
    page_title="Practica 1",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Data Pull and Functions

# Options Menu
with st.sidebar:
    selected = st.radio('Menu', ["Intro", 'Graficas', 'Distribucion binomial', 'Info'], index=0)

# Intro Page
if selected == "Intro":
    # Header
    st.title('Distribución Binomial')
    st.subheader('*asdasdassssssssssssssssssssssssssssssssssss.*')
    st.divider()
    # Use Cases
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.header('Resumen')
            st.markdown("""
                asdasdasdsaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
            """)
            st.header('Objetivos')
            st.markdown("""
                asdddddddddddddddddddd
            """)
        with col2:
            st.header('Marco teorico')
            st.markdown("""
                asdasdasdsaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            """)
            st.header('Conclusiones')
            st.markdown("""
                asdddddddddddddddddddd
            """)
    
# Search Page
elif selected == 'Graficas':
    # Add a title to the app
    st.title("CSV File Viewer")
    # Add a file uploader to the app
    df = pd.read_csv("ConteosDeCarasPorPareja.csv")
    # Display the DataFrame in Streamlit
    st.dataframe(df)
    # Display some statistics about the DataFrame
    st.write(f"The DataFrame has {len(df)} rows and {len(df.columns)} columns.")

# Grafica
elif selected == 'Distribucion binomial':
    def leer_archivo_py():
        try:
            with open("Practica1.py", "r") as archivo:
                contenido = archivo.read()
                st.text_area("Contenido del archivo", contenido)
        except FileNotFoundError:
            st.error("El archivo no fue encontrado.")

    def main():
        st.title("aaaaa")
        st.write("sdasdasdasd.")

        leer_archivo_py()

   

# About Page
elif selected == 'Info': 
    st.title('Datos')
    st.markdown("""
        asdasdasdsaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    """)
     if __name__ == "__main__":
        main()
