# Estudo_Dataframe
import pandas as pd
# Lista - Uma coleção ordenada de elementos que podem ser de qualquer tipo
lista_nomes = ['Luiz', 'Rafaella', 'Hector']
print('Lista de nomes: \n', lista_nomes)
print('Primeiro Elemento da lista \n',lista_nomes[0])

# Dicionário: Estrutura composta de pares chave-valor
dicionario_pessoa= { # type: ignore
    'nome':'Luizin',
    'idade': 34 ,
    'cidade': 'São Paulo'
}
print('Dicionário de uma pessoa: \n', dicionario_pessoa) # type: ignore
print( ' Atributo do dicionário: \n', dicionario_pessoa.get('nome')) # type: ignore

# Listas de dicionários: Estrutura de dados que combina listas e dicionários
dados = [ # type: ignore
    {'nome': 'Luizin', 'idade': 34, 'cidade':'São Paulo'},
    {'nome': 'Rafaella', 'idade': 21, 'cidade':'São José'},
    {'nome': 'Hector', 'idade': 20, 'cidade':'São Paulo'}
]

# DataFrame: Estrutura de dados bidimensional
df = pd.DataFrame(dados)
print('DataFrame \n', df)

# Selecionar coluna
print(df['nome'])

# Selecionar várias colunas 
print(df[['nome', 'idade']])

# Selecionar linhas pelo índice
print('Primeira linha \n', df.iloc[0])

# Adicionar uma nova coluna
df['salario'] = [9200, 7400, 5000]

# Adicionar um novo registro
df.loc[len(df)] = {
    'nome': 'Maribel',
    'idade': 38,
    'cidade': 'Ribeirão Preto',
    'salario': 6200
}
print('DataFrame Atual \n', df)

# Removendo uma coluna
df.drop('salario', axis=1, inplace=True)

# Filtrnado pessoas com mais de 29 anos
filtro_idade = df[df['idade'] >= 30]  # Fazendo um filtro dentro da chamada dele
print('Filtro \n', filtro_idade)

# Salvando o DataFrame em um arquivo CSV
df.to_csv('dados.csv', index=False)

# Lendo um arquivo CSV em um DataFrame
df_lido = pd.read_csv('dados.csv') # type: ignore
print('\n Leiruta do CSV\n', df_lido)

# Diferenças entre listas, dicionarios e dataFrame e quando vamos usar cada um deles 