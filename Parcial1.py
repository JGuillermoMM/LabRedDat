#Estos son los paquetes que pense que utilizaria xD
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb
import plotly.express as px
import pandas as pd
#La función del st.marown es para ingresar texto en el streamlit, aunque el st.markdown de la linea 9 tiene cosas de htm para que se pudiera centrar el texto
st.markdown("<h1 style='text-align: center;'>Distribución Binomial</h1>", unsafe_allow_html=True)
st.markdown("Esta pagina es una graficadora de la distribución binomial, donde podrá elegir los valores de las constantes que necesite para ver en su grafica, estas constantes son:")
st.markdown("""
- Número de ensayos (n): Representa el número total de ensayos o experimentos. Este valor tiene que ser menores a 100 y positivos.
- Probabilidad de éxito (p): Es la probabilidad de que ocurra un éxito en un solo ensayo. Este valor tiene que ser menor a 1 y positivo.
- Número de éxitos (x): Es la variable discreta que representa el número de éxitos que se observan en los n ensayos. Esta estará dividida en Limite inferior y Limite superior  para poder observar en la grafica cual es el caso mínimo y el caso máximo de éxitos que desea calcular. El limite inferior tiene que ser un valor mayor o igual a 0 y tiene que ingresar un valor menor a 150 para el limite superior.
""")
st.markdown("también es posible elegir que tipo de grafica representará la distribución binomial con los datos elegidos. Puede seleccionar entre Histograma y grafica tipo Scattering")
#el st.ltex permite ingresar codigo en latex y presentarlo en nuestro streamlit
st.latex(r'''P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}''')
#el st.number son las cajas que presenta el streamlit done se ponen los datos y se guardan en estas variables
n = st.number_input("Introduzca el valor de n", value=1)
p = st.number_input("Introduzca el valor de p",value= 0.5)
Li = st.number_input("Introduzca el caso minimo de exitos que espera ")
Ls = st.number_input("Introduzca el caso maximo de exitos que espera ")
#Genera una variable con limites, en este aso las variables anteriores son sus limites
x = np.linspace(Li, Ls, num=15)
#se declara una función y entre parentesis se aclara de que variables dependera 
def verificar_valores(p,n,Ls,Li):
    #este if funciona para que el boton evalue los datos que se enuentran en las cajas
    if st.button("Verificar valores"):
    #Los siguientes if/else permite evalaur los datos que estan en las cajar y sacar un aviso que le indique al usuario si los datos son permitidos o los tiene que cambiar
        #los st.succes y st.error muestrar un mensaje de error o de exito en el streamlit
        if Ls <= 150:
            st.success("Los valores para el limite superior son correctos")
        else:
            st.error("Solo son permitidos valores menores a 150 para el limite superior")
        if Li >= 0:
            st.success("Los valores para el limite inferior son correctos")
        else:
            st.error("Solo son permitidos valores mayores a 0 para el limite inferior")           
        if p <= 1:
             st.success("Los valores para p son correctos")
        else:
            st.error("Ingrese un valor de probabilidad correcto, menor a 1 ")          
        if n <= 99:
           st.success("Los valores para n son correctos")
        else:
           st.error("Solo son permitidos valores menores a 100 para n") 
#se llama a la función que definimos antes para evaluar los datos de las cajas
verificar_valores(p,n,Ls,Li) 
#creo otra función para calcula la istribución binomial, aqui se utilizo una libreria para optimizar calculos :p
def db(n,p,x):
    coeficiente = comb(n, x)#aqui es done se aplico el paquete 
    probabilidad = coeficiente * (p*x) * ((1-p)*(n-x))
    return probabilidad
probabilidad = db(n, p, x)#esto me parecio interesante xd, porque las variables se pueden repetir porque estan afuera de la funciones definidas, incluyendo  si es algun tipo de ciclo, no se pueden llamar las viarables que se declararon adentro de estos, tuve muchos problemas por eso sjdjsdjsjd
# esa función permite mostrar en streamlit opcines y poder seleccionarlar
tgraf = st.radio(
    "Eliga de que manera quiere ver su grafica",
    ["Scattering", "Histograma"])
#dependiendo que opción se elegió con el st.radio este if grafica dicha opción, un histograma o el Scattering
if tgraf == 'Scattering':#Aqui si la respuesta fue tipo Scattering
    grafica = px.scatter(x=x,y=probabilidad, labels={'x': 'Casos de existo', 'y': 'Probabilidad que sucedan los casos'})
    #y desde aca es para cambiar los detalles de la grafica
    grafica.update_layout(
    title='Distribución Binomial',
    xaxis=dict(title='Casos de Exito'),
    yaxis=dict(title='Probabilidad de que sucedan los casos'),
    plot_bgcolor='#F5F5DC',
    legend=dict(title='Datos'))
    st.plotly_chart(grafica)
else:#Aqui si la respuesta fue tipo Scattering
    grafica = px.bar(x=x,y=probabilidad, labels={'x': 'Casos de existo', 'y': 'Probabilidad que sucedan los casos'})
    grafica.update_layout(#y desde aca es para cambiar los detalles de la grafica pero del histograma
   title='Distribución Binomial',
    xaxis=dict(title='Casos de Exito'),
    yaxis=dict(title='Probabilidad de que sucedan los casos'),
    plot_bgcolor='#F5F5DC',
    legend=dict(title='Datos'))
   #esto muestra la grafica en el streamlit 
    st.plotly_chart(grafica)