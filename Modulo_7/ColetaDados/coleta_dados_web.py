import requests
import pandas as pd
from bs4 import BeautifulSoup # Manter BeautifulSoup para fins didáticos, mas pd.read_html pode fazer o trabalho sozinho aqui.
import time

# URL de um site mais amigável para web scraping tradicional com tabelas estáticas
# Exemplo: Lista de países por população na Wikipédia
url_amigavel = 'https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o'

# Cabeçalho User-Agent (ainda boa prática)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

print(f"Iniciando tentativa de web scraping tradicional para: {url_amigavel}")

try:
    # 1. Faz a requisição HTTP GET
    print("Fazendo requisição HTTP para a página...")
    response = requests.get(url_amigavel, headers=headers)
    response.raise_for_status() # Lança um erro para status HTTP ruins (4xx ou 5xx)

    print("\n--- Conteúdo HTML Recebido (primeiros 500 caracteres) ---")
    print(response.text[:500])

    # 2. Analisa o HTML com BeautifulSoup (Opcional para pd.read_html, mas bom para demonstração)
    print("\nAnalisando o HTML com BeautifulSoup (para fins de visualização)...")
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify()[:1000]) # Descomente para ver mais do HTML analisado

    # 3. Tenta encontrar todas as tabelas com pandas.read_html()
    print("\nTentando extrair tabelas com pandas.read_html()...")
    # A Wikipédia pode ter várias tabelas. Você pode precisar inspecionar a página
    # para saber qual índice da lista [0], [1], [2] etc. corresponde à tabela que você quer.
    tabelas_encontradas = pd.read_html(response.text, header=0, flavor='html5lib')

    print(f"Número de tabelas HTML detectadas por pandas.read_html(): {len(tabelas_encontradas)}")

    if len(tabelas_encontradas) > 0:
        print("\n--- Tabelas Encontradas (Primeiras 5 Linhas de Cada) ---")
        for i, df in enumerate(tabelas_encontradas):
            print(f"\n--- Tabela {i} ---")
            print(df.head())
            print(f"Colunas: {df.columns.tolist()}") # Mostra as colunas da tabela

            # Exemplo: A tabela de população pode ser a primeira ou a segunda
            # Tentativa de identificar a tabela de população (baseado em colunas esperadas)
            if 'País (ou dependência)' in df.columns and 'População' in df.columns:
                print(f"**Provável tabela de população encontrada no índice {i}**")
                print("\n--- Primeiras 10 linhas da provável Tabela de População ---")
                print(df.head(10).to_string())
                break # Sai do loop se encontrar uma tabela que parece ser a correta
        else:
            print("\nNenhuma tabela com as colunas esperadas ('País (ou dependência)', 'População') foi encontrada.")
    else:
        print("\nNenhuma tabela foi detectada por pandas.read_html() no HTML inicial.")

    print("\n--- Fim da tentativa de Web Scraping Tradicional ---")

except requests.exceptions.RequestException as e:
    print(f"\nOcorreu um erro na requisição HTTP: {e}")
    print("Possíveis causas:")
    print("- Problema de conexão com a internet.")
    print("- O servidor bloqueou a requisição.")
    print("- A URL está incorreta ou inacessível.")
    print("Tente esperar um pouco e executar novamente, ou verifique sua conexão/firewall.")
except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")
    print("Verifique se todas as bibliotecas estão instaladas (requests, pandas, beautifulsoup4, html5lib, lxml).")
    print("O erro também pode indicar que a estrutura da página HTML não contém tabelas da forma esperada.")