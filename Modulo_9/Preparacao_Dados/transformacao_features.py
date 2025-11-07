import pandas as pd
import numpy as np
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

# Transformação Logarítima
df['salario_log'] = np.log1p(df['salario']) # Loglp é usado para evitar problemas com valores Zero

print("\nDataFrame após transformação logarítmica no 'salário': \n", df.head())

# Transformação Box-Cox
df['salario_boxcox'], _ = stats.boxcox(df['salario'] + 1)

print("\nDataFrame após transformação BoxCox no 'salário:\n", df.head())

# Codificação de Frequência para 'estado'
estado_freq = df['estado'].value_counts() / len(df)
df['estado_freq'] = df['estado'].map(estado_freq)

print("\nDataFrame após codificação de Frequência para 'estado':\n", df.head())

# Interações
df['interacao_idade_filhos'] = df['idade'] * df['numero_filhos']

print("\nDataFrame após criação de interações entre 'idade' e 'numero_filhos:\n", df.head())