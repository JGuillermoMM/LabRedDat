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
    selected = option_menu('Menu', ["Intro", 'Graficas'], 
        icons=['comment-alt','stats'],menu_icon='intersect', default_index=0)
    lottie = load_lottiefile("digglet.json")
    st_lottie(lottie,key='loc')

#Intro Page
if selected=="Intro":
    #Titulo Distribución binomial centrado con html
 st.markdown("""
<style>
.big-title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    margin-top: 50px;
}
</style>
<div class="big-title">Laboratorio 1 Distribución Binomial</div>
""", unsafe_allow_html=True)
 st.markdown("""
<style>
.centered-italic {
    text-align: center;
    font-style: italic;
    font-size: 20px;
    margin-top: 5px;
}
</style>
<div class="centered-italic">This is some centered and italicized content.</div>
""", unsafe_allow_html=True)

 st.divider()

    #Use Cases
 with st.container():
        col1,col2=st.columns(2)
#Columna 1 de introducción        
        with col1:
            st.markdown("""
<style>
.big-title {
    text-align: center;
    font-size: 36px;
    margin-top: 5px;
}
</style>
<div class="big-title">Resumen</div>
""", unsafe_allow_html=True)
            st.markdown(
                """
                La distribución binomial es una función que describe la probabilidad de obtener un número específico de éxitos
                  en un número fijo de casos independientes. La distribuión binomial es ideal en casos en donde se analice el resultado de un número pequeño de posibles estados finales"""
                )
            st.markdown("""
<style>
.big-title {
    text-align: center;
    font-size: 36px;
    margin-top: 5px;
}
</style>
<div class="big-title">Objetivos</div>
""", unsafe_allow_html=True)
            st.subheader('Generales')
            st.markdown(
                """
                - Comprobar experimental y teóricamente el conoimiento de probabilidades 
                
                """
                )
            st.subheader('Específicos')
            st.markdown(
                """
                - Verificar le toeria de la distribución binomial
                - Verificar que los datos obtenidos experimentalmente sigan un comportamiento ¿binomial? xd
                """
                )
#Columna dos de introducción       
        with col2:
             st.markdown("""
              <style>
             .big-title {
             text-align: center;
              font-size: 36px;
               margin-top: 5px;
               }
              </style>
             <div class="big-title">Marco teorico</div>
            """, unsafe_allow_html=True)
             st.subheader('Coeficiente Binomial')
             st.markdown(
                """
                El coeficiente binomial indica el numero de subconjuntos 
                de k elementos escogidos de un conjunto de n elementos totales. Puede ser calculado de la siguiene manera
                """
                )
             st.latex(r'''\binom{n}{k}= \frac{n!}{k!(n-k)!}''')
             st.subheader('Distribución Binomial')
             st.markdown("La distribución Binomial, llamada así por el coeficiente binomial, permite describir la probabilidad de observar una cantidad de éxitos en una cantidad de intentos, considerando la probabilidad individual de éxito de cada intento. Específicamente, estas características se dividen en las siguientes variables: ")
             st.markdown(""" 
                        - Número de ensayos (n): Representa el número total de ensayos o experimentos. 
                        - Probabilidad de éxito (p): Es la probabilidad de que ocurra un éxito en un solo ensayo. 
                        - Número de éxitos (x): Es la variable discreta que representa el número de éxitos que se observan en los n ensayos.
""")
             st.latex(r'''P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}''')

             st.markdown("""
              <style>
             .big-title {
              text-align: center;
             font-size: 36px;
             margin-top: 5px;
               }
             </style>
             <div class="big-title">Conclusiones</div>
            """, unsafe_allow_html=True)
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
