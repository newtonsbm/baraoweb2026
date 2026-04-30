from fastapi import FastAPI
import random

app = FastAPI(
    title="API para Rolar Dados",
    description="Uma API super simples e didática para aprender conceitos de Web Services",
    version="1.0.0"
)

@app.get("/rolar/")
def rolar_dado(faces: int = 6):
    """
    **GET /rolar/**
    
    Rola um dado com o número de faces especificado e retorna um valor aleatório.
    
    ### Parâmetros:
    - `faces` (opcional): Número de faces do dado. **Padrão: 6**
    
    ### Respostas (200 OK):
    Retorna um JSON com o resultado do dado
    
    ### Exemplos:
    
    **Exemplo 1 - Dado padrão (6 faces):**
    ```
    GET /rolar/
    ```
    Resposta:
    ```json
    {
        "resultado": 4
    }
    ```
    
    **Exemplo 2 - Dado com 20 faces:**
    ```
    GET /rolar/?faces=20
    ```
    Resposta:
    ```json
    {
        "resultado": 17
    }
    ```
    
    """
    # Gerar um número aleatório entre 1 e o número de faces
    resultado = random.randint(1, faces)
    
    return {
        "resultado": resultado
    }


# ============================================================
# Para rodar: uv run uvicorn main:app --reload
# Documentação interativa: http://localhost:8000/docs
# ============================================================

