import pandas as pd
import random
from faker import Faker

faker = Faker('pt_BR')

dados_pessoas = []

for _ in range (10):
    nome = faker.name()
    cpf = faker.cpf()
    idade = random.randint(18, 60)
    data = faker.date_of_birth(minimum_age = idade, maximum_age = idade).strftime("%d/%m/%Y")
    endereço = faker.address()
    estado = faker.state()
    pais = ('Brasil')

    pessoa = {
        'nome': nome,
        'cpf' : cpf, 
        'idade' : idade,
        'data' : data,
        'endereço' : endereço,
        'estado' : estado, 
        'pais' : pais
    }

    dados_pessoas.append(pessoa) # type: ignore

    df_pessoas = pd.DataFrame(dados_pessoas)
    print(df_pessoas)

    #pd.set_option('display.max_columns', None) # Mostrar o máximo de colunas
    #pd.set_option('display.max_rows', None)  # Mostrar o máximo de linhas
    #pd.set_option('display.max_colwidth', None) # Mostrar o máximo da largura de coluna
    #pd.set_option('display.width', None) # Mostrar o máximo da largura de display

    print(df_pessoas.to_string())  # head(), tail()

    df_pessoas.to_csv('clientes.csv')
