import pandas as pd
import matplotlib.pyplot as plt
# Importamos el DataFrame
df = pd.read_csv("SPX.csv")

# ------------------------------------
# --- ANÁLISIS EXPLORATORIO BÁSICO ---  
# ------------------------------------
print("Nulos de cada variable:\n", df.isnull().sum())
print("Filas duplicadas: ", df.duplicated().sum())

# Convertimos la columna Date a formato Fecha
df["Date"] = pd.to_datetime(df["Date"])

print(df.describe())

plt.plot