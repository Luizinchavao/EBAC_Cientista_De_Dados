import requests 
from bs4 import BeautifulSoup  


print('Request: ')
response = requests.get('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/')
print(response.text[:600])

print('BeautifulSoup: ')
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:1000])

