import matplotlib.pyplot as plt

def GraficarDistribucionTStudent(x,y,t_critical,t_value, gradosLibertad):
    #Tamaño de gui
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, y, 'b-', label=f'Distribución t de Student con df={gradosLibertad:.2f}')
    
    # Dibujar las regiones de rechazo
    ax.fill_between(x, 0, y, where=(x > t_critical), color='red', alpha=0.3, label='Región de rechazo (positiva)')
    ax.fill_between(x, 0, y, where=(x < -t_critical), color='red', alpha=0.3, label='Región de rechazo (negativa)')
    
    # Dibujar la línea vertical de la estadística t
    ax.axvline(x=t_value, color='green', linestyle='--', label=f'Estadística T ={t_value:.2f}')

    # Dibujar las líneas verticales de los valores críticos
    ax.axvline(x=t_critical, color='purple', linestyle='--', label=f'Valor crítico positivo = {t_critical:.2f}')
    ax.axvline(x=-t_critical, color='orange', linestyle='--', label=f'Valor crítico negativo = {-t_critical:.2f}')
    
    # Añadir título, etiquetas y leyenda
    ax.set_title('Gráfico de la prueba t de Student')
    ax.set_xlabel('Valor t')
    ax.set_ylabel('Densidad de probabilidad')
    ax.legend()
    ax.grid(True)
    plt.show()