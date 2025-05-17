import requests
import os
from dotenv import load_dotenv

def buscar_imagens_de_gatos(limit=10):
    # Carrega variáveis de ambiente do arquivo .env
    load_dotenv()

    api_key = os.getenv("API_KEY_CAT")

    if not api_key:
        raise ValueError("API Key não encontrada nas variáveis de ambiente.")

    url = "https://api.thecatapi.com/v1/images/search"

    headers = {
        'x-api-key': api_key
    }

    params = {
        "limit": limit
    }

    resposta = requests.get(url=url, headers=headers, params=params)
    print(f"Status code: {resposta.status_code}")

    if resposta.status_code == 200:
        return resposta.json()
    else:
        raise Exception(f"Erro ao buscar imagens: {resposta.status_code}")

# Exemplo de uso:
if __name__ == "__main__":
    imagens = buscar_imagens_de_gatos()
    print(imagens)