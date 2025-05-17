'''import requests

resposta_unique = requests.get("https://jsonplaceholder.typicode.com/posts/1")
resposta_lista = requests.get("https://jsonplaceholder.typicode.com/posts")

posts = resposta_lista.json()
post_1 = resposta_unique.json()
print("Tipo lista (vários posts): ", type(posts))
print("Tipo unico (um só post): ", type(post_1))

for post in posts[:10]:
    print("\nTitulo: ", post["title"])
    print("Conteúdo: ", post["body"])

'''
import requests

def obter_posts(url_lista, url_unico, limite=10):
    resposta_unique = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    resposta_lista = requests.get("https://jsonplaceholder.typicode.com/posts")

    posts = resposta_lista.json()
    post_1 = resposta_unique.json()

    print("Tipo lista (vários posts):", type(posts))
    print("Tipo único (um só post):", type(post_1))

    for post in posts[:limite]:
        print("\nTítulo:", post["title"])
        print("Conteúdo:", post["body"])
