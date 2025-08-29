import pandas as pd
from scipy import stats

pd.set_option('display.width', None)
df = pd.read_csv('Clientes_limpeza.csv')

df_filtro_basico = df[df['idade'] > 100]
print('Filtro básico \n', df_filtro_basico[['nome', 'idade']])

# Identificar Outliers com Z-score
z_scores = stats.zscore(df['idade'].dropna())
outliers_z = df[z_scores >= 3]
print('Outliers pelo Z-score: \n', outliers_z)

# Filtrar Outliers com Z-score
df_zscore = df[(stats.zscore(df['idade']) < 3)]

# Identificar Outliers com IQR
Q1 = df['idade']. quantile(0.25)
Q3 = df['idade']. quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR

print('Limites IQR: ', limite_baixo, limite_alto)

outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)]
print('Outliers pelo IQR:', outliers_iqr)

# Filtrar Outliers com IQR
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

# Filtrar endereços inválidos 
df['endereco'] = df['endereco'].apply(lambda x: 'Endereco Inválido' if len(x.split('\n')) <3 else x)

# Tratar campos de texto
df['nome'] = df['nome'].apply(lambda x: 'Nome Inválido' if isinstance(x, str) and len(x) < 50 else x)
print('Qtd registros com nomes grandes:', (df['nome'] == 'Nome Inválido').sum())

print('Dados com Outliers tratados: \n', df)

# Salvar DataFrame
df.to_csv('clientes_remove_outliers.csv', index=False)