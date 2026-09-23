from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend funcionando"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

# Função auxiliar para os testes
def soma(valores):
    """Recebe uma lista de números e retorna a soma."""
    return sum(valores)
