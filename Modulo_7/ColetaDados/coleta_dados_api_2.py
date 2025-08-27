import requests 

def enviar_arquivo():
    # Caminho do arquivo para upload
    caminho = 'C:/Users/PC/Desktop/EBAC_Cientista_De_Dados/Modulo_7/produtos_informatica.xlsx.xlsx'
    
    # Enviar o arquivo (post),(rb = read binario)->Serve para ficar mais leve o arquivo. Economiza memória
    requisicao = requests.post(url='https://upload.gofile.io/uploadFile', files={'file': open(caminho, 'rb')})
    saida_requisicao = requisicao.json()
    # Dentro desse arquivo .Json tem varios atributos e o que agente vai usar é o 'link' 

    print(saida_requisicao)
    url = saida_requisicao['data']['downloadPage']
    print("Arquivo enviado. Link para acesso: ", url)

def enviar_arquivo_chave():
   # Caminho do Arquivo e chave para upload
   caminho = 'C:/Users/PC/Desktop/EBAC_Cientista_De_Dados/Modulo_7/produtos_informatica.xlsx.xlsx'
   chave_acesso = 'JHjiEPJGxDQaw56SZLMP8HAoUG9YFrKX' # API Key

   # Enviar o arquivo 
   requisicao = requests.post( # type: ignore
      url='https://upload.gofile.io/uploadFile',
      files={'file': open(caminho, 'rb')},
      headers={'Authorization': chave_acesso}
      
   )

def receber_arquivo(file_url: str):
    # Receber o arquivo (get)
    requisicao = requests.get(file_url)

    # Salvar o arquivo
    if requisicao.ok:
     with open('arquivo_baixado.xlsx', 'wb') as file:
            file.write(requisicao.content)
            print("Arquivo baixado com sucesso")
    else:
        print("Erro ao baixar o arquivo", requisicao.json())


enviar_arquivo()
enviar_arquivo_chave()
receber_arquivo('https://gofile.io/d/lNgmoz')