import matplotlib.pyplot as plt    
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head(20).to_string())  # Exibe as primeiras 20 linhas do DataFrame para verificar os dados 

# Gráfico de barras
plt.figure(figsize=(10,6))
df['nivel_educacao'].value_counts().plot(kind='bar', color='#90ee70')#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas
plt.title('Divisão de Escolaridade - 1')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)  # Deixa os rótulos do eixo x na horizontal
plt.show()

x = df['nivel_educacao'].value_counts().index
y = df['nivel_educacao'].value_counts().values

plt.figure(figsize=(10,6))
plt.bar(x, y, color='#60aa65')
plt.title('Divisão de Escolaridade -2')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')

# Gráfico de pizza
plt.figure(figsize=(10,6))
plt.pie(y, labels=x, autopct='%1.1f%%', startangle=90)
plt.title('Distribuição de Nível de Educação -3')
plt.show()  # Exibe o gráfico de pizza

# Gráfico de dispersão
plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap='Blues')#https://matplotlib.org/stable/users/explain/colors/colormaps.html
plt.colorbar(label='Contagem dentro do bin')  # Adiciona uma barra de cores para indicar a densidade
plt.title('Dispersão de Idade e Salário')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.show()

# Criar Grafico de Pizza
plt.figure(figsize=(8,8))

