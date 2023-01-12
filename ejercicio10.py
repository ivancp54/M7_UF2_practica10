import pandas as pd

# importar el archivo CSV
df = pd.read_csv("test.csv")
# IDs a seleccionar
ids = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]
# seleccionar las filas con esos ids
df_sel = df.loc[df["id"].isin(ids)]
# imprimir los datos de las filas seleccionadas
print(df_sel)
def clock_speed():
    df_clock_speed = df_sel["clock_speed"]
    print(df_clock_speed)

def pixels():
    df_px = df_sel[["px_height","px_width"]]
    print(df_px)

def bateria():
    df_bat = df_sel["battery_power"]
    print(df_bat)


print(bateria())