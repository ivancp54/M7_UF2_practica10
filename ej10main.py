import matplotlib.pyplot as plt
import ejercicio10 as ej10

def main():
    # Obtener los datos de las funciones
    dato1 = ej10.clock_speed()
    dato1.plot.bar()

    #dato2 = ej10.pixels()
    #dato3 = ej10.bateria()
    # Crear el gráfico de barras
    plt.show()
    return dato1

print(main())
