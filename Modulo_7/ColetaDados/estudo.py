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