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
    selected = option_menu('Menu', ["Intro", 'Graficas','Info'], 
        icons=['comment-alt','stats','info-circle'],menu_icon='intersect', default_index=0)
    lottie = load_lottiefile("digglet.json")
    st_lottie(lottie,key='loc')

#Intro Page
if selected=="Intro":
    #Header
    st.title('Distribución Binomial')
    st.subheader('*asdasdassssssssssssssssssssssssssssssssssss.*')

    st.divider()

    #Use Cases
    with st.container():
        col1,col2=st.columns(2)
        with col1:
            st.header('Resumen')
            st.markdown(
                """
                asdasdasdsaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
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

    st.divider()


    
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
#About Page
 if selected=='Info':
    st.title('Data')
    #st.subheader('All data for this project was publicly sourced from:')
    col1,col2,col3=st.columns(3)
    col1.subheader('Source')
    col2.subheader('Description')
    col3.subheader('Link')
    with st.container():
        col1,col2,col3=st.columns(3)
        #col1.image('census_graphic.png',width=150)
        col1.write(':blue[U.S. Census Bureau]')
        col2.write('Demographic, housing, industry at zip level')
        #col2.write('American Community Survey, 5-Year Profiles, 2021, datasets DP02 - DP05')
        col3.write('https://data.census.gov/')
    
    with st.container():
        col1,col2,col3=st.columns(3)
        #col1.image('cdc.png',width=150)
        col1.write(':blue[Centers for Disease Control and Prevention]')
        col2.write('Environmental factors at county level')
        col3.write('https://data.cdc.gov/')
    
    with st.container():
        col1,col2,col3=st.columns(3)
        #col1.image('hud.png',width=150)\
        col1.write(':blue[U.S. Dept Housing and Urban Development]')
        col2.write('Mapping zip to county')
        col3.write('https://www.huduser.gov/portal/datasets/')

    with st.container():
        col1,col2,col3=st.columns(3)
        #col1.image('ods.png',width=150)
        col1.write(':blue[OpenDataSoft]')
        col2.write('Mapping zip to USPS city')
        col3.write('https://data.opendatasoft.com/pages/home/')
    
    st.divider()
    
    st.title('Creator')
    with st.container():
        col1,col2=st.columns(2)
        col1.write('')
        col1.write('')
        col1.write('')
        col1.write('**Name:**    Kevin Soderholm')
        col1.write('**Education:**    M.S. Applied Statistics')
        col1.write('**Experience:**    8 YOE in Data Science across Banking, Fintech, and Retail')
        col1.write('**Contact:**    kevin.soderholm@gmail.com or [linkedin](https://www.linkedin.com/in/kevin-soderholm-67788829/)')
        col1.write('**Thanks for stopping by!**')
        col2.image('kevin8.png')