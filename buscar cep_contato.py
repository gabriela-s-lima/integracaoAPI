import sys

import requests
# Tipos de lista de contatos
clientes = []
fornecedores = []

def buscar_cep():
    while True:
        cep = input("Digite o CEP para buscar: ")
        url = f"https://viacep.com.br/ws/{cep}/json/"

        resposta = requests.get(url=url)

        status_code = resposta.status_code
        if status_code == 400:
            print("Erro. Verifique se está digitando somente "
                  "numeros ou se está digitando os 8 digitos de CEP.")
            continue

        resposta = resposta.json()

        if "erro" in resposta:
            print("CEP inválido. Tente novamente.")
            continue
        else:
            return resposta

def aplicar_funcao(funcao_escolhida):
    resposta = input("Qual lista você quer visualizar? 'fornecedores' ou 'clientes': ")
    if resposta == "clientes":
        return funcao_escolhida(clientes)
    elif resposta == "fornecedores":
        return funcao_escolhida(fornecedores)
    else:
        print("Opção de lista inválida. Tente novamente.")
        return None


def menu():
    print("\nMenu de opções:")
    print("""
    0 - Sair
    1 - Cadastrar novo contato
    2 - Editar um contato
    3 - Deletar um contato
    4 - Mostrar todos os contatos cadastrados
    """)
    return input("Escolha uma opção: ")


def cadastrar_contato(lista_tipo_contato):
    contato = {}
    contato["codigo"] = len(lista_tipo_contato)
    contato["nome"] = input("Digite o nome: ")
    contato["email"] = input("Digite o email: ")
    contato["telefone"] = input("Digite o telefone: ")
    contato["endereço"] = buscar_cep()
    lista_tipo_contato.append(contato)
    print("Contato cadastrado com sucesso!")


def editar_contato(lista_tipo_contato):
    codigo = int(input("Digite o código do contato que deseja editar: "))
    if 0 <= codigo < len(lista_tipo_contato):
        print("Contato atual:", lista_tipo_contato[codigo])
        nome = input("Digite o novo nome (ou deixe em branco para manter o mesmo): ")
        email = input("Digite o novo email (ou deixe em branco para manter o mesmo): ")
        telefone = input("Digite o novo telefone (ou deixe em branco para manter o mesmo): ")
        endereço = input("Quer trocar de endereço? (Digite qualquer tecla "
                         "ou deixe em branco pra manter o mesmo: ")

        if nome:
            lista_tipo_contato[codigo]["nome"] = nome
        if email:
            lista_tipo_contato[codigo]["email"] = email
        if telefone:
            lista_tipo_contato[codigo]["telefone"] = telefone
        if endereço:
            lista_tipo_contato[codigo]["endereço"] = buscar_cep()

        print("Contato atualizado com sucesso!")
    else:
        print("Código inválido.")


def deletar_contato(lista_tipo_contato):
    codigo = int(input("Digite o código do contato que deseja deletar: "))
    if codigo >= 0 and codigo < len(lista_tipo_contato):
        lista_tipo_contato.pop(codigo)
        # Atualiza os códigos após remoção
        for i in range(len(lista_tipo_contato)):
            lista_tipo_contato[i]["codigo"] = i
        return "Contato deletado com sucesso!"
    else:
        return "Código inválido."

def mostrar_contatos(lista_tipo_contato):
    if lista_tipo_contato:
        print("\nLista de contatos:")
        for contato in lista_tipo_contato:
            print(contato)
    else:
        print("Nenhum contato cadastrado.")


buscar_cep()

# Loop principal
while True:
    opcao = menu()

    if opcao == "0":
        print("Saindo do programa.")
        break
    elif opcao == "1":
        aplicar_funcao(cadastrar_contato)

    elif opcao == "2":
        aplicar_funcao(editar_contato)

    elif opcao == "3":
        aplicar_funcao(deletar_contato)

    elif opcao == "4":
        aplicar_funcao(mostrar_contatos)
    else:
        print("Opção inválida.")
