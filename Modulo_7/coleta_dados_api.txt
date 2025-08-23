import requests
from bs4 import BeautifulSoup 

url = 'https://wiki.python.org/moin/'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

# Exibir o texto
# print(extracao.text.strip()) # .strip -> Remover os espaços em branco

# Filtrar o exibição pela tag
#for linha_texto in extracao.find_all('h2'):
#     titulo = linha_texto.text.strip()
#      print('Titulo: ', titulo)



#  DESAFIO: 
#  Filtrar tags ['h2', 'p']
# Contar quantos 'h2' e 'p' existem no documento (linha_texto.name == tag)

# Contar a quantidade de títulos e paragrafos

contar_titulos = 0
contar_paragrafos = 0

for linha_texto in extracao.find_all(['h2','p']):
    if linha_texto.name == 'h2': 
        contar_titulos += 1  # -> contar_titulos = contar_titulos + 1
    elif linha_texto.name == 'p': 
         contar_paragrafos += 1
  
print('Total de Títulos', contar_titulos)

print('Total de Paragrafos', contar_paragrafos)

# Exibir somente os textos das tags h2 e p
#for linha_texto in extracao.find_all(['h2', 'p']):
 #   if linha_texto.name == 'h2': # type: ignore
 #       titulo = linha_texto.text.strip()
 #        print('Titulo: \n', titulo)
 #   elif linha_texto.name == 'p': # type: ignore
 #       paragrafo = linha_texto.text.strip()
 #       print('Paragrafo: \n', paragrafo)