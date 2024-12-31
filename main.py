from fastapi import FastAPI, Query
import requests


# Criei uma instancia de FastAPI
app = FastAPI()

# Criei uma rota, ou um endpoint, que é a URL que eu vou acessar
@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que exibe uma mensagem de Hello World

    '''
    return {'Hello':'World'}

@app.get('/api/restaurantes')
# Recebe um argumento que sera uma string que vira de um Query, que por padrao nao vira nada 'None'
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint que mostrara o cardapio do restaurante escolhido
    ou se não for passado parametro nenhum, exibira o cardapio
    de todos os restaurantes

    Input:
    .Nome do restaurante

    Output:
    .Cardapio do restaurante
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        # Se nao for passado nenhum restaurante como parametro
        if restaurante is None:
            # Retorna a lista completa de todos os dados
            return {'Dados': dados_json}
        # Se for passado algum restaurante como paramentro
        # Aqui sera armazenado os dados do cardapio do restaurante 
        dados_do_restaurante = []
        # para cada item na lista json
        for item in dados_json:
            # Se o item ou VALOR na CHAVE Company for igual ao valor que recebemos de argumento 
            if item['Company'] == restaurante:
                dados_do_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurante': restaurante, 'Cardapio': dados_do_restaurante}
    else:
        return {'Erro': f'{response.status_code} - {response.text}'}
    
# uvicorn main:app --reload // para rodar