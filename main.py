from fastapi import FastAPI

# Criei uma instancia de FastAPI
app = FastAPI()

# Criei uma rota, ou um endpoint, que é a URL que eu vou acessar
@app.get('/api/hello')

def hello_world():
    return {'Hello':'World'}

# uvicorn main:app --reload // para rodar