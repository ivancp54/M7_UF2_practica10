import matplotlib.pyplot as plt
from ejercicio10 import *

def main():
    # Obtener los datos de las funciones
    dato1 = clock_speed()
    dato2 = pixels()
    dato3 = bateria()
    # Crear el gráfico de barras
    plt.bar(range(len(dato1)), dato1, label="clock_speed")
    plt.bar(range(len(dato2)), dato2, label="pixels")
    plt.bar(range(len(dato3)), dato3, label="bateria")

    # Establecer las opciones del gráfico
    plt.xlabel("Data")
    plt.ylabel("Value")
    plt.title("Graph")
    plt.legend()

    # Mostrar el gráfico
    plt.show()


if __name__ == "__main__":
    main()