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
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from streamlit_lottie import st_lottie
st.set_option('deprecation.showPyplotGlobalUse', False)
from pydub import AudioSegment
from pydub.playback import play
import scipy.stats as ss





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
 <div class="centered-italic">José Guillermo Monterroso Marroquín, 202005689 y Shawn César Alejandro García Fernández, 201906567 </div>
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
                - Verificar la teoria de la distribución binomial
                - Verificar que los datos obtenidos experimentalmente sigan un comportamiento de distribución binomial
                """
                )
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


            st.title('Reproductor de Spotify')

# Enlace a la canción de Spotify
            spotify_link = st.text_input("Introduce el enlace de la canción de Spotify:")
            if spotify_link.startswith("https://open.spotify.com/"):
                st.write(f"Reproduciendo la canción desde {spotify_link}")
                st.write(f'<iframe src="https://open.spotify.com/embed/track/{spotify_link.split("/")[-1]}" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>', unsafe_allow_html=True)
            else:
                st.write("Introduce un enlace válido de Spotify.")
    

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
             <div class="big-title">Conclusiones</div>
            """, unsafe_allow_html=True)
             st.markdown(
                """
                - Elaborar un gráfico de barras que muestre cómo se distribuye el número de caras en los primeros 
                m lanzamientos de 10 monedas, donde  m  varía de 0 a 100, nos brinda la oportunidad de analizar 
                cómo evoluciona esta distribución conforme se incrementa la cantidad de lanzamientos verificando
                que la teoria de la distribución binomial es consistente con los resultado obtenidos esperimentalmente.
                """)
             st.markdown("""
              <style>
             .big-title {
              text-align: center;
             font-size: 36px;
             margin-top: 5px;
               }
             </style>
             <div class="big-title">Discusión de Resultados</div>""", unsafe_allow_html=True)
             st.markdown(
                """
                - A medida que el valor de m aumenta, la distribución adquiera mayor simetría y se asemeje más a una forma de campana, la cual es típica de la distribución binomial.
                - Aunque se consideraron los eventos de todas las parejas, no se pudieron obtener todos los casos.. Sin embargo, las gráficas siempre mostraron una tendencia hacia la media, lo cual es consistente con el comportamiento esperado de una distribución binomial en este escenario de tiros de moneda.
                """)
             
             




             st.markdown("""
  <style>
  .big-title {
    text-align: center;
    font-size: 36px;
    margin-top: 5px;
 }
 </style>
 <div class="big-title">Referencias</div>
 """, unsafe_allow_html=True)
             st.markdown(
                """
                - Taylor, John R. “An introduction to error analysis, The study of uncertainties in physical measure-
                ments”. Second edition. University science books. 1982. 
                - https://www.linode.com/docs/guides/how-to-choose-python-api-framework/
                - https://es.wikipedia.org/wiki/Coeficiente_binomial
                - https://tecnonovax.wordpress.com/reproducir-musica-en-spotify-con-python/
                
                """
                )

    


    
#Search Page
if selected=='Graficas':
    df = pd.read_csv("ConteosDeCarasPorPareja.csv")
    st.dataframe(df)
    st.write(f"The DataFrame has {len(df)} rows and {len(df.columns)} columns.")
    
# Datos de las caras de las monedas
    # Datos de las caras de las monedas
    listas = {
    "Guillermo y Shawn": [2, 4, 5, 3, 7, 3, 4, 6, 4, 4, 3, 5, 3, 2, 3, 4, 8, 6, 4, 2, 5, 5, 3, 8, 4, 7, 4, 6, 3, 5, 8, 7, 3, 3, 6, 5, 4, 4, 5, 2, 5, 3, 7, 6, 3, 6, 5, 2, 4, 6, 5, 4, 6, 3, 6, 5, 3, 7, 8, 7, 4, 4, 4, 8, 5, 4, 3, 5, 7, 5, 2, 2, 3, 5, 1, 6, 4, 6, 4, 4, 3, 3, 6, 6, 3, 4, 5, 5, 5, 7, 6, 7, 4, 3, 5, 4, 5, 7, 6, 5],
    "Lobsang y Rebeca": [6, 5, 5, 6, 5, 4, 6, 6, 5, 4, 6, 6, 5, 6, 9, 8, 1, 7, 5, 3, 5, 3, 3, 4, 3, 5, 4, 4, 6, 2, 5, 6, 7, 5, 5, 2, 3, 5, 7, 6, 5, 1, 6, 4, 4, 8, 5, 3, 6, 5, 6, 4, 5, 5, 3, 2, 6, 5, 2, 9, 7, 4, 7, 4, 3, 3, 6, 6, 4, 4, 6, 5, 5, 4, 6, 4, 9, 6, 4, 4, 8, 6, 4, 4, 8, 6, 8, 3, 6, 2, 5, 6, 2, 4, 5, 3, 4, 6, 5, 7],
    "Diego y Saul": [5, 6, 5, 5, 4, 4, 4, 3, 6, 5, 4, 7, 5, 7, 3, 5, 4, 7, 3, 4, 6, 3, 4, 5, 6, 2, 7, 3, 6, 2, 4, 7, 5, 5, 5, 3, 6, 6, 5, 4, 4, 7, 4, 7, 6, 5, 4, 4, 3, 5, 5, 4, 4, 7, 4, 5, 5, 4, 7, 6, 9, 5, 5, 5, 4, 5, 5, 7, 5, 4, 8, 3, 4, 4, 4, 8, 4, 9, 7, 7, 5, 5, 7, 5, 4, 4, 6, 7, 4, 2, 5, 5, 3, 6, 7, 5, 4, 4, 4, 7],
    "Giovanna y Mario": [5, 5, 5, 7, 7, 4, 7, 4, 6, 6, 6, 5, 5, 5, 6, 6, 6, 6, 7, 4, 5, 4, 5, 6, 5, 8, 7, 4, 3, 6, 4, 3, 6, 2, 7, 5, 8, 7, 6, 7, 4, 5, 5, 6, 4, 7, 4, 6, 4, 3, 4, 5, 5, 4, 3, 5, 6, 7, 5, 4, 5, 4, 4, 4, 6, 8, 6, 7, 5, 1, 3, 6, 4, 5, 4, 3, 5, 4, 3, 4, 6, 8, 5, 6, 5, 7, 5, 4, 6, 5, 4, 4, 10, 8, 3, 7, 5, 5, 4, 4],
    "Dessiré y Fabricio": [6, 4, 3, 6, 6, 6, 6, 7, 4, 4, 5, 4, 5, 3, 4, 8, 5, 3, 6, 6, 6, 5, 5, 5, 6, 4, 6, 6, 7, 6, 6, 6, 5, 4, 2, 5, 3, 6, 4, 4, 6, 5, 3, 4, 5, 5, 6, 5, 7, 5, 3, 3, 5, 5, 5, 4, 10, 5, 6, 4, 3, 5, 6, 4, 3, 4, 6, 5, 4, 6, 8, 5, 5, 5, 4, 5, 8, 4, 5, 5, 3, 3, 4, 5, 2, 7, 4, 5, 4, 6, 5, 6, 3, 6, 5, 7, 7, 9, 5, 3],
    "Jacobo y Cesar": [6, 6, 5, 3, 2, 5, 7, 8, 4, 5, 3, 4, 7, 6, 8, 4, 2, 3, 7, 2, 7, 6, 2, 5, 8, 2, 4, 4, 5, 5, 3, 6, 3, 5, 6, 6, 3, 6, 7, 3, 5, 4, 5, 4, 3, 5, 6, 4, 7, 4, 7, 6, 4, 6, 7, 6, 7, 4, 2, 4, 3, 4, 5, 5, 7, 4, 5, 4, 2, 4, 7, 5, 3, 5, 5, 4, 4, 6, 5, 4, 4, 4, 5, 4, 6, 6, 6, 8, 3, 5, 7, 3, 4, 8, 4, 6, 5, 4, 6, 4]
            }

# Función para plotear el histograma y el ajuste
    def plot_histogram_and_fit(data, m, hist_color, fit_color, mean_color, std_dev_color):
    # Obtener los datos
        data_selected = data[:m]
    
    # para la grafica y sus colores
        mean = np.mean(data_selected)
        std_dev = np.std(data_selected)
    
    # Calcular p
        n = len(data_selected)
        p = mean / n
    
    # Fit de la distribución binomial
        x = np.arange(0, max(data_selected)+1)
        y = binom.pmf(x, n, p)
        return data_selected, mean, std_dev, p, y

# Crear la interfaz de usuario 
    def main():
        st.title('Ajuste Binomial y Histograma Interactivo')
        dataset = st.selectbox('Selecciona un conjunto de datos:', ["Clase"] + list(listas.keys()))
        if dataset == "Clase":
            data_selected = [item for sublist in listas.values() for item in sublist]
            m = 500
        else:
            data_selected = listas[dataset]
            m = st.slider('Selecciona el valor de m:', 1, 100, 10)
        hist_color = st.color_picker('Color del histograma:', '#00f')
        fit_color = st.color_picker('Color del ajuste:', '#f00')
        mean_color = st.color_picker('Color del valor mínimo:', '#0f0')
        std_dev_color = st.color_picker('Color de la desviación estándar:', '#ffa500')
        data, mean, std_dev, p, y = plot_histogram_and_fit(data_selected, m, hist_color, fit_color, mean_color, std_dev_color)
        st.write('---')
        st.header('Valores obtenidos del ajuste y medidos experimentalmente:')
        st.write(f'Conteo medio de caras (ajuste binomial): {mean:.2f}')
        st.write(f'Desviación estándar (ajuste binomial): {std_dev:.2f}')
        st.write(f'Valor de p (ajuste binomial): {p:.2f}')
        st.write(f'Conteo medio de caras (experimental): {np.mean(data):.2f}')
        st.write('---')

    # Para el histograma
        plt.hist(data, bins=np.arange(min(data), max(data)+1)-0.5, density=True, alpha=0.6, color=hist_color, edgecolor='black', linewidth=1.2, label='Datos experimentales')
    
    # Para el ajuste
        plt.plot(np.arange(len(y)), y, 'r--', linewidth=1.5, label=f'Ajuste Binomial\nMedia: {mean:.2f}\nDesviación Estándar: {std_dev:.2f}')
    
    # Graficar la media y la desviación estándar
        plt.axvline(x=min(data), color=mean_color, linestyle='-', linewidth=2, label=f'Valor mínimo: {min(data)}')
        plt.axvline(x=mean, color=std_dev_color, linestyle='-', linewidth=2, label=f'Desviación estándar: {std_dev:.2f}')

    #plt.xlabel('Número de Caras')
    #plt.ylabel('Densidad de probabilidad')
    #plt.title(f'Histograma y Ajuste Binomial para los primeros {m} tiros del conjunto de datos')
        plt.legend()
        plt.grid(True)

    # Ajustar la posición del cuadro de texto
        plt.tight_layout()
        st.pyplot()

    if __name__ == '__main__':
        main()