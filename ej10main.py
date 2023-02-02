import matplotlib.pyplot as plt
import ejercicio10 as ej10

def main():
    # Obtener los datos de las funciones
    fig, ax = plt.subplots(3,1)
    id = [ '3','13','34','56','70','85','110','120','210','400']
    dato1 = ej10.clock_speed()
    ax[0].set_title('Reloj veloz')
    ax[0].legend(title='ID')
    ax[0].bar(id,dato1.clock_speed)
    dato2 = ej10.pixels()
    ax[1].set_title('Pixeles')
    ax[1].legend(title='ID')
    ax[1].bar(id, dato2.px_width)
    dato3 = ej10.bateria()
    ax[2].set_title('Bateria')
    ax[2].legend(title='ID')
    ax[2].bar(id,dato3.battery_power)
    # Crear el gráfico de barras
    plt.show()

print(main())
