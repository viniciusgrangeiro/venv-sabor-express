import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_do_restaurante = {}
    
    # para cada item na lista json
    for item in dados_json:
        # Recebe o nome do restaurante do item
        nome_do_restaurante = item['Company']
        # Se o nome ainda não estiver na lista de dados dos restaurantes
        if nome_do_restaurante not in dados_do_restaurante:
            # Cria uma lista para serem adicionados as informações a um restaurante em especifico

            # ex:
            # dados_restaurante
            # [
            #     [
                    # McDonalds //nome_do_restaurante
            #         [
            #             item: item,
            #             price: preco,
            #             description: description
            #         ]
            #     ],
            # ]
            dados_do_restaurante[nome_do_restaurante] = []
        # Adciona os valores as chaves que criamos usando o append()
        dados_do_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })
else:
    print(f'O erro foi {response}')

# Para cada nome de restaurante em dados_do_restaurante, em intem, faça:
for nome_do_restaurante, dados in dados_do_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    # para criar um arquivo, 'w' de escrever
    with open(nome_do_arquivo,'w') as arquivo_restaurante:
        # json.dump para criar um arquivo json
        # 3 parametros, dados que eu vou inserir, nome do arquivo, e identacao
        json.dump(dados, arquivo_restaurante, indent=4)