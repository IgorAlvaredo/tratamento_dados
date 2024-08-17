import pandas as pd

df = pd.read_csv('/data/ecommerce_ex3.csv')

# Escreva seu código abaixo
# Calcular o intervalo interquartil (IQR)
Q1 = df['N_Avaliacoes'].quantile(0.25)
Q3 = df['N_Avaliacoes'].quantile(0.75)
IQR = Q3 - Q1

# Definir o limite superior para identificar outliers
limite_alto = Q3 + 1.5 * IQR

# Filtrar os produtos que possuem um número de avaliações maior que o limite superior
df_avaliados = df[(df['N_Avaliacoes'] > limite_alto)]