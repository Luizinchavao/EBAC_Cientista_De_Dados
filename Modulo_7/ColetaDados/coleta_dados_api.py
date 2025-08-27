import requests


def enviar_arquivo():
    # Caminho do arquivo
    caminho = 'C:/Users/PC/Desktop/EBAC_Cientista_De_Dados/produtos_informatica.xlsx.xlsx'
    
    try:
        # Tenta abrir o arquivo para envio
        with open(caminho, 'rb') as arquivo:
            # Envia o arquivo
            requisicao = requests.post(
                url='https://api.gofile.io/uploadFile',
                files={'file': arquivo}
            )

        # Verifica se a requisição foi bem-sucedida (código 200)
        if requisicao.status_code == 200:
            saida_requisicao = requisicao.json()
            print("Resposta da API:")
            print(saida_requisicao)
            
            # Pega o link de download
            url = saida_requisicao.get('data', {}).get('downloadPage', 'Link não encontrado')
            if url != 'Link não encontrado':
                print("Arquivo enviado com sucesso. Link para acesso:", url)
            else:
                print("O upload pode ter falhado. A API não retornou um link de download.")
        else:
            print(f"Erro na requisição. Código de status: {requisicao.status_code}")
            print(f"Resposta da API (pode não ser JSON): {requisicao.text}")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Chamada da função
enviar_arquivo()