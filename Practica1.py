import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.optimize import curve_fit
#para los widgets
from ipywidgets import interact, ColorPicker




# para el histograma y los valores de m
 # Para cambiar colores https://stackoverflow.com/questions/42172440/how-to-set-color-in-matplotlib-histograms

caras = [
    2, 4, 5, 3, 7, 3, 4, 6, 4, 4, 3, 5, 3, 2, 3, 4, 8, 6, 4, 2, 5, 5, 3, 8, 4,
    7, 4, 6, 3, 5, 8, 7, 3, 3, 6, 5, 4, 4, 5, 2, 5, 3, 7, 6, 3, 6, 5, 2, 4, 6,
    5, 4, 6, 3, 6, 5, 3, 7, 8, 7, 4, 4, 4, 8, 5, 4, 3, 5, 7, 5, 2, 2, 3, 5, 1,
    6, 4, 6, 4, 4, 3, 3, 6, 6, 3, 4, 5, 5, 5, 7, 6, 7, 4, 3, 5, 4, 5, 7, 6, 5
]

def plot_histogram(m, hist_color, fit_color, mean_color, std_dev_color):
    num = caras

    # calcular la media y la desviación estándar
    valor_min= np.mean(num)
    std_dev = np.std(num)

   # histograma
    plt.figure(figsize=(10, 6))
    plt.hist(num, bins=np.arange(0, m+2)-0.5, edgecolor='black', alpha=0.7, density=True, color=hist_color, label='Datos experimentales')



   # para el fit binomial
    def gaussian(x, mu, sigma):
        return 1/(sigma*np.sqrt(2*np.pi)) * np.exp(-(x - mu)**2 / (2*sigma**2))

    # para los valores de m y p
    v_m = m
    v_p = 0.5

    # fit de la curva
    bin_centers = 0.5*(np.arange(0, m+1) + np.arange(1, m+2))
    params, cov = curve_fit(gaussian, bin_centers, np.histogram(num, bins=np.arange(0, m+2)-0.5, density=True)[0])


    # para graficar la curva
    x_values = np.linspace(0, m+1, 1000)
    plt.plot(x_values, gaussian(x_values, *params), color=fit_color, linestyle='--', label=' Fit de la distribución gaussiana')

   # Graficar la media y la desviación estándar
    plt.axvline(x=valor_min, color=mean_color, linestyle='-', linewidth=2, label=f'Valor mínimo: {valor_min:.2f}')
    plt.axvline(x=valor_min + std_dev, color=std_dev_color, linestyle='-', linewidth=2, label=f'Desviación estándar: {std_dev:.2f}')

 # para los textos de la grafica
    plt.xlabel('Número de caras')
    plt.ylabel('Probabilidad')
    plt.title('Conteo de caras')
    plt.xticks(np.arange(0, m+2))
    plt.legend()
    plt.grid(True)
    plt.show()

    print(" Parámetros del fit de distribución binomial: ", params)

# widgets
interact(plot_histogram,
         m=(0, 100, 1),
         hist_color=ColorPicker(value='blue', description='Color del histograma'),
         fit_color=ColorPicker(value='red', description='Color del fit'),
         mean_color=ColorPicker(value='green', description='Color del valor mínimo'),
         std_dev_color=ColorPicker(value='orange', description='Color de la desviación estándar'))