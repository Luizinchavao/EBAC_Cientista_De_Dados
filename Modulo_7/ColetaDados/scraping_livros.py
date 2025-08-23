import requests
from bs4 import BeautifulSoup

# URL da página
url = "https://books.toscrape.com/"
response = requests.get(url)

# Cria o objeto soup
soup = BeautifulSoup(response.text, "html.parser")

# Encontra todos os livros da página
livros = soup.find_all("article", class_="product_pod")

# Loop para extrair dados de cada livro
for livro in livros:
    # Título do livro
    titulo = livro.h3.a["title"] # type: ignore
    
    # Preço
    preco = livro.find("p", class_="price_color").text
    
    # Avaliação (está no nome da classe, ex: "star-rating Three")
    estrelas = livro.p["class"][1]  # Segundo item da lista de classes

    print(f"📖 {titulo} | 💲 {preco} | ⭐ Avaliação: {estrelas}")
