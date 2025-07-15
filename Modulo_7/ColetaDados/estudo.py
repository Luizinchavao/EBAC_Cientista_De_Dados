# ENTNDIMENTO DA LINHA -> print(response.text[:500]) = SLICE é o fatiamento, é obter uma parte

# texto = 'Extrair msg de texto' # 'Extrair mensagem de texto' -> Isso é chamado de sequência

texto = list(range(1,20))

subtexto = texto[:11]# Começa no 0 vai até o 11
print(subtexto)

subtexto = texto[8:] # Começa no 8 e vai até o final 
print(subtexto)

subtexto = texto[-5:] # Vai começar de trás para frente com número negativo -5
print(subtexto)

subtexto = texto[8:11] # INtervalo - Quero iniciar no 8 ir até o 11
print(subtexto)


# MÓDULO -> É um conjunto onde vai ter seus códigos, suas funçoes, variáveis vai estar tudo lá.
# CLASSE -> Uma classe é uma estrutura de dados (inteiro, float, boleanos.)
# Nao é interessante trabalhar assim: import bs4 e depois utilizar ele soup = bs4.BeautifulSoup()
# Porque você está carregando o MÓDULO INTEIRO (bs4) para estar utilizando apenas uma CLASSE BeautifulSoup
# É interessante você digitar somente essa classe pq qdo alguém for olhar seu código ja vai ssaber quais classes vc está utilizando 
# Ex: soup = bss4.BeautifulSoup- Esstá carregando o módulo inteiro mais só está utilizando uma clase a:BeautifulSoup