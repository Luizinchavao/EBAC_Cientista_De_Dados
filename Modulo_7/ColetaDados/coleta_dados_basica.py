import requests 
from bs4 import BeautifulSoup  
import pandas as pd

# URL da página de DADOS HISTÓRICOS do Ibovespa no Yahoo Finance (URL do professor)
url = 'https://br.financas.yahoo.com/quote/%5EBVSP/history/'

# Cabeçalho User-Agent para simular um navegador e evitar bloqueio
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


try:
    # Faz a requisição HTTP GET para a URL, enviando o cabeçalho User-Agent
    print(f"Fazendo requisição para: {url}")
    response = requests.get(url, headers=headers)
    response.raise_for_status() # Verifica se houve algum erro na requisição (ex: 404, 500)

    # Imprime uma parte do conteúdo HTML recebido (primeiros 500 caracteres, como no exemplo do professor)
    print("\n--- Conteúdo HTML Recebido (primeiros 500 caracteres) ---")
    print(response.text[:500])
    soup = BeautifulSoup(response.text, 'html.parser')  # BealtifulSoup é umas classe que tem suas propriedades 
    print(soup.prettify()[:1000])


    print('pandas: ')
    url_dados = pd.read_html('https://br.financas.yahoo.com/quote/%5EBVSP/history/')
    # URL da API de download de dados históricos (retorna CSV)
    # Esta é a URL que o Pandas *vai* acessar para ler os dados.
    api_url = f"https://query1.finance.yahoo.com/v7/finance/download/%5EBVSP?period1={period1}&period2={period2}&interval=1d&events=history&includeAdjustedClose=true"
    print(f"Tentando API para dados históricos: {api_url}")

    response_api = session.get(api_url, headers=headers)
    response_api.raise_for_status()

    # Pandas lê o CSV diretamente da URL da resposta da API
    df_historico_ibovespa = pandas.read_csv(response_api.url)
   

    print(url_dados[0].head(10))

except Exception as e:
    print(f"\nOcorreu um erro: {e}")
    print("Possíveis causas:")
    print("- Problema de conexão com a internet.")
    print("- O Yahoo Finance ainda está bloqueando a requisição (tente novamente após um tempo).")
    print("- A URL ou a estrutura da página podem ter mudado.")