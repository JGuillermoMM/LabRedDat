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


#Layout
st.set_page_config(
    page_title="Practica 1",
    layout="wide",
    initial_sidebar_state="expanded")

#Data Pull and Functions
st.markdown("""
<style>
.big-font {
    font-size:80px !important;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)

@st.cache_data
def pull_clean():
    master_zip=pd.read_csv('ConteoDeCarasPorParejas.csv',dtype={'ZCTA5': str})
    return master_zip



#Options Menu
with st.sidebar:
    selected = option_menu('Menu', ["Intro", 'Graficas', 'Distribucion binomial', 'Info'], 
        icons=['comment-alt','stats','info-circle'],menu_icon='intersect', default_index=0)
    lottie = load_lottiefile("digglet.json")
    st_lottie(lottie,key='loc')

#Intro Page
if selected=="Intro":
    #Header
    st.title('Distribución Binomial')
    st.latex(r'''    P(X = k) = \binom{n}{k} \cdot p^k \cdot (1 - p)^{n - k}    ''')
                 

    st.divider()

    #Use Cases
    with st.container():
        col1,col2=st.columns(2)
        with col1:
            st.header('Resumen')
            st.markdown(
                """
                Una distribución binomial es un modelo matemático que representa la probabilidad de obtener cierta cantidad de
                éxitos en un número fijo de intentos independientes, donde cada intento solo puede tener dos resultados posibles: éxito o fracaso.
                Cada intento se considera independiente entre sí y la probabilidad de éxito en cada uno permanece constante.
                """
                )
     st.header('Objetivos')
            st.markdown(
                """
                asdddddddddddddddddddd
                """
                )




      with col2:
            st.header('Marco teorico')
            st.markdown(
                """
                asdasdasdsaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                """
                )
            st.header('Conclusiones')
            st.markdown(
                """
                asdddddddddddddddddddd
                """)

    



    
#Search Page
if selected=='Graficas':
    # Set up the Streamlit ap

 # Add a title to the app
 st.title("CSV File Viewer")

# Add a file uploader to the app
 

 df = pd.read_csv("ConteosDeCarasPorPareja.csv")
  # Display the DataFrame in Streamlit
 st.dataframe(df)

   # Display some statistics about the DataFrame
 st.write(f"The DataFrame has {len(df)} rows and {len(df.columns)} columns.")



#---------------------------------------------------------------
# Grafica
#if selected=='Distribucion binomial':

#def leer_archivo_py():
#    try:
 #       with open("Practica1.py", "r") as archivo:
 #           contenido = archivo.read()
#            st.text_area("Contenido del archivo", contenido)
#    except FileNotFoundError:
#        st.error("El archivo no fue encontrado.")

#def main():
 #   st.title("aaaaa")
#    st.write("sdasdasdasd.")

 #   leer_archivo_py()
#if __name__ == "__main__":
 #   main()

#-----------------------------------------------------------------
    
  

 
#About Page
if selected=='Info': 
    st.title('Datos')
    st.markdown(
                """
                asdasdasdsaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                """)

