import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY_CLIMA")

def obter_dados_clima(cidade, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        return {
            'cidade': cidade,
            'temperatura': dados['main']['temp'],
            'descricao': dados['weather'][0]['description']
        }
    else:
        return {
            'cidade': cidade,
            'erro': f"Não foi possível obter dados para '{cidade}' (Status {resposta.status_code})"
        }


def exibir_resultados(cidades_info):
    print("\n=== Resultados ===")
    for info in cidades_info:
        if 'erro' in info:
            print(f"[{info['cidade']}] -> Erro: {info['erro']}")
        else:
            print(f"[{info['cidade']}] -> {info['temperatura']}°C, {info['descricao'].capitalize()}")

    cidades_validas = [c for c in cidades_info if 'erro' not in c]
    if cidades_validas:
        mais_quente = max(cidades_validas, key=lambda x: x['temperatura'])
        print(f"\n🔥 A cidade mais quente é {mais_quente['cidade']} com {mais_quente['temperatura']}°C.")
    else:
        print("\nNenhuma cidade válida para comparar temperaturas.")


def main():
    api_key = os.getenv("API_KEY_CLIMA")
    cidades = input("Digite ao menos 3 cidades separadas por vírgula: ").split(',')

    if len(cidades) < 3:
        print("Você deve informar pelo menos 3 cidades.")
        return

    cidades = [cidade.strip() for cidade in cidades]
    dados = [obter_dados_clima(cidade, api_key) for cidade in cidades]
    exibir_resultados(dados)


if __name__ == "__main__":
    main()

