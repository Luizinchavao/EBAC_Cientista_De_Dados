# -*- coding: utf-8 -*-
# Importa a biblioteca pandas para manipulação de dados
import pandas as pd

# Lê o arquivo CSV para um DataFrame do Pandas
df = pd.read_csv('clientes.csv')

# Ativa a largura do display para mostrar todas as colunas
pd.set_option('display.width', None)

# Mostra as primeiras 5 linhas do DataFrame
print("DataFrame Original:")
print(df.head())

# --- REMOVER DADOS ---
# Remove a coluna 'pais' (axis=1) e a linha de índice 2 (axis=0)
# 'inplace=True' faz a alteração diretamente no DataFrame
df.drop('pais', axis=1, inplace=True) # Remove a coluna 'pais'
df.drop(2, axis=0, inplace=True)     # Remove a linha com índice 2

# --- NORMALIZAR CAMPOS DE TEXTO ---
# Converte a coluna 'nome' para o formato de título
df['nome'] = df['nome'].str.title()
# Converte a coluna 'endereco' para minúsculas
df['endereco'] = df['endereco'].str.lower()
# Remove espaços e converte a coluna 'estado' para maiúsculas
df['estado'] = df['estado'].str.strip().str.upper()

# --- CONVERTER TIPOS DE DADOS ---
# Converte a coluna 'idade' para o tipo inteiro
df['idade'] = df['idade'].astype(int)

print('\nNormalizar Textos:', df.head())

# --- TRATAR VALORES NULOS (AUSENTES) ---
df_fillna = df.fillna(0)
df_dropna = df.dropna()
df_dropna4 = df.dropna(thresh=4)
df = df.dropna(subset=['cpf']) # Remove registros com CPF nulo

print('\nValores nulos:\n', df.isnull().sum())
print('Qtd de registros nulos com fillna:', df_fillna.isnull().sum().sum())
print('Qtd de registros nulos com dropna:', df_dropna.isnull().sum().sum())
print('Qtd de registros nulos com dropna4:', df_dropna4.isnull().sum().sum())
print('Qtd de registros nulos com CPF :', df.isnull().sum().sum())

df.fillna({'estado': 'Desconhecido'}, inplace=True)
df['endereco'] = df['endereco'].fillna('Endereço não informado')
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean())

# --- TRATAR FORMATO DE DADOS ---
# Use o formato correto da data: '%d/%m/%Y' para datas como 06/12/1933
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

# --- TRATAR DADOS DUPLICADOS ---
print('\nQtd de Registro atual:', df.shape[0])
df.drop_duplicates(subset='cpf', inplace=True)
print('Qtd de registros removendo as duplicadas:', len(df))

print('\nDados Limpos: \n', df)

# --- SALVAR DATAFRAME ---
# Cria as colunas 'data' e 'idade' com os valores corrigidos
df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']

# Seleciona as colunas a serem salvas
df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'estado']]

# Salva o DataFrame limpo em um NOVO arquivo CSV.
# Isso evita sobrescrever o arquivo original.
df_salvar.to_csv('clientes_limpos.csv', index=False)

# Tenta ler o arquivo que você acabou de salvar.
# O nome do arquivo tem que ser o mesmo que você usou para salvar.
print('Novo Dataframe: \n', pd.read_csv('clientes_limpos.csv'))
