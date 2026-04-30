# � API de Dados (Dice) - Exemplo Didático

Uma API **extremamente simples** e didática para ensinar conceitos fundamentais de **Web Services e REST API** para alunos de graduação.

Rola um dado virtual com número de faces configurável! 🎯

## 📚 O que é um Web Service?

Um **Web Service** (ou API Web) é um sistema que permite que diferentes aplicações se comuniquem através da internet usando o protocolo HTTP.

### Características principais:
- ✅ Comunica-se via **HTTP** (usando métodos GET, POST, PUT, DELETE)
- ✅ Troca dados em formato **JSON**
- ✅ Segue princípios **REST** (Representational State Transfer)
- ✅ Independente de linguagem de programação
- ✅ Escalável e fácil de usar

---

## 🚀 Como Rodar a API

### 1. Instalar dependências
```bash
uv sync
```

### 2. Rodar o servidor
```bash
uvicorn main:app --reload
```

### 3. Acessar a API
- **Documentação Interativa (Swagger):** http://localhost:8000/docs
- **Documentação Alternativa (ReDoc):** http://localhost:8000/redoc
- **API Base:** http://localhost:8000

> A documentação interativa permite testar todos os endpoints diretamente no navegador! 🎉

---

## 📖 Como Usar

### Rolar um Dado Padrão (6 faces)
```bash
GET http://localhost:8000/rolar/
```

**Resposta:**
```json
{
  "resultado": 4
}
```

### Rolar um Dado com Número Customizado de Faces
```bash
# Dado com 20 faces (D20)
GET http://localhost:8000/rolar/?faces=20
```

**Resposta:**
```json
{
  "resultado": 17
}
```

### Mais Exemplos
```bash
# Dado com 100 faces
GET http://localhost:8000/rolar/?faces=100

# Dado com 2 faces (moeda)
GET http://localhost:8000/rolar/?faces=2

# Dados com 12 faces
GET http://localhost:8000/rolar/?faces=12
```

---

## 🧪 Testando a API

### Opção 1: Com Postman
1. Baixe [Postman](https://www.postman.com/download/)
2. Crie uma nova requisição GET
3. Digite a URL: `http://localhost:8000/rolar/?faces=6`
4. Clique em "Send"

### Opção 2: Com cURL (Terminal)
```bash
# Dado padrão
curl http://localhost:8000/rolar/

# Dado com 20 faces
curl http://localhost:8000/rolar/?faces=20

# Dado com 100 faces
curl http://localhost:8000/rolar/?faces=100
```

### Opção 3: Com Python
```python
import requests

# GET - Rolar dado com 6 faces
response = requests.get('http://localhost:8000/rolar/')
print(response.json())
# Output: {"resultado": 4}

# GET - Rolar dado com 20 faces
response = requests.get('http://localhost:8000/rolar/?faces=20')
print(response.json())
# Output: {"resultado": 17}
```

### Opção 4: No Navegador
- Abra: http://localhost:8000/rolar/
- Abra: http://localhost:8000/rolar/?faces=20
- Abra: http://localhost:8000/rolar/?faces=100

---

## 🎯 Conceitos Aprendidos

Esta API ensina:

### 1. **Query Parameters**
```
/rolar/?faces=20
         ↑ Query parameter
```
Permite passar dados pela URL para configurar o comportamento da API.

### 2. **Parâmetros com Valores Padrão**
```python
def rolar_dado(faces: int = 6):
    # Se não enviar 'faces' na query, usa 6 como padrão
```

### 3. **Resposta em JSON**
```json
{
  "resultado": 17
}
```
A API retorna dados estruturados em JSON que qualquer aplicação pode ler.

### 4. **Métodos HTTP**
- **GET** - Recuperar dados (rolar o dado e obter resultado)

### 5. **Status HTTP**
- **200 OK** - Sucesso na requisição

---

## 📊 Endpoints Disponíveis

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Informações da API |
| GET | `/rolar/` | Rolar um dado (padrão 6 faces) |
| GET | `/rolar/?faces=20` | Rolar um dado com 20 faces |

---

## 💡 Por Que Esta API é Didática?

✅ **Simplicidade Máxima** - Apenas 1 endpoint de negócio
✅ **Sem Complexidade** - Sem banco de dados, autenticação ou validações complexas
✅ **Fácil de Testar** - Pode testar direto no navegador ou com uma linha de cURL
✅ **Documentação Automática** - Swagger gera docs automaticamente
✅ **Código Legível** - Fácil entender o que o código faz
✅ **Resultado Visível** - Cada chamada produz um resultado diferente (aleatório)

---

## 🎮 Casos de Uso para Ensino

### Para Alunos Iniciantes:
> "Veja como uma API retorna dados em JSON que você pode usar em qualquer linguagem!"

### Para Entender Query Parameters:
```bash
# Mesmo endpoint, resultados diferentes
/rolar/        # 1-6
/rolar/?faces=20   # 1-20
/rolar/?faces=100  # 1-100
```

### Para Simular Comportamentos Aleatórios:
```bash
# Simular um jogo de RPG
/rolar/?faces=20  # Ataque com D20
/rolar/?faces=12  # Defesa com D12
```

### Para Integração com Frontend:
```javascript
// JavaScript
fetch('http://localhost:8000/rolar/?faces=6')
  .then(response => response.json())
  .then(data => console.log(`Tirou ${data.resultado}`))
```

---

## 🚀 Próximos Passos (Evoluindo a API)

Se quiser evoluir este conceito:
1. ➕ Adicionar histórico de jogadas
2. 📊 Adicionar estatísticas (média, máximo)
3. 👥 Adicionar multi-jogador
4. 💾 Usar banco de dados para persistir dados
5. 🎮 Integrar com um frontend

---

## 📚 Conceitos Explicados

### Como a Chamada Funciona:

```
CLIENTE                           SERVIDOR
  │                                  │
  │─── GET /rolar/?faces=6 ────────→│
  │                                  │
  │                         gera número aleatório
  │                         entre 1 e 6
  │                                  │
  │←─ {"resultado": 4} ─────────────│
  │                                  │
```

1. Client faz requisição GET
2. Server recebe parâmetro `faces=6`
3. Server gera número aleatório entre 1 e 6
4. Server retorna JSON com resultado
5. Client recebe e pode usar o dado

---

## 🎓 Conclusão

Esta é a API mais simples possível de um Web Service! Com apenas ~30 linhas de código, conseguimos:
- ✅ Criar um endpoint funcional
- ✅ Receber parâmetros (query parameters)
- ✅ Usar valores padrão
- ✅ Retornar JSON
- ✅ Gerar documentação automática
- ✅ Ser testável no navegador

**Agora você já sabe criar um Web Service! 🎉**



