from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Sucesso", "msg": "FastAPI rodando no Desafio 5!"}