import requests
import os
from dotenv import load_dotenv


def buscar_imagens_de_gatos(limit):
    load_dotenv()
    api_key = os.getenv("API_KEY_CAT")

    if not api_key:
        raise ValueError("API Key não encontrada nas variáveis de ambiente.")

    url = "https://api.thecatapi.com/v1/images/search"
    headers = {'x-api-key': api_key}
    params = {"limit": limit}

    resposta = requests.get(url=url, headers=headers, params=params)

    if resposta.status_code == 200:
        return resposta.json()
    else:
        raise Exception(f"Erro ao buscar imagens: {resposta.status_code}")


def solicitar_quantidade():
    while True:
        try:
            qtd = int(input("Quantos gatos você deseja buscar? (máximo 5): "))
            if 1 <= qtd <= 5:
                return qtd
            else:
                print("Por favor, digite um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")


def exibir_resultados(lista_de_gatos):
    print("\n🐱 Imagens de gatos encontradas:")
    for i, gato in enumerate(lista_de_gatos, start=1):
        print(f"{i}. ID: {gato.get('id', 'N/A')}")
        print(f"   URL: {gato.get('url', 'URL não encontrada')}\n")


if __name__ == "__main__":
    quantidade = solicitar_quantidade()
    imagens = buscar_imagens_de_gatos(quantidade)
    exibir_resultados(imagens)