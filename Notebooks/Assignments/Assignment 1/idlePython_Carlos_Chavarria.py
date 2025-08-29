import matplotlib.pyplot as plt
import pandas as pd

data: pd.DataFrame = pd.read_csv("Tareas/Tarea 1/datos/datos.csv")

print(data.head())

data.plot(x = 'Mes', y='Ventas', kind = 'line')

plt.show()
