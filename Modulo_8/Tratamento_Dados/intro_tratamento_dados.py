import pandas as pd

df = pd.read_csv('clientes.csv')

# Verificar os primeiros resgistros
print(df.head().to_string()) # MOstrar tudo em uma linha só, pra nao ficar aqueles 3 pontinhos, pois tem muita coisa escrito

# Verificar os últimos resgistros
print(df.tail().to_string())

# Verificar quantidade de linhas e colunas
print('Qtd', df.shape)

# Verificas os tipos de dados
print('Tipagem : \n' , df.dtypes)

# Checar valores nulos
print('Valores nulos : \n' , df.isnull().sum())