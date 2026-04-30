# A15 - Serviços Web e API 

## Atividades
- Seguindo o padrão no projeto cafe com pao na pasta `cafecompao` implemente os endpoints de listagem e detalhe de padarias baseado no que foi feito para cestas
- Olhe principalmente os arquivos `app/api/views.py` e `app/api/schemas.py` para entender como criar os endpoints e os schemas de validação
- Teste os endpoints usando o Swagger (http://localhost:8000/api/docs/) 
- Se desejar pode usar o cafecompao_estruturado e seguir o padrao de divisão das rotas por dominio

### Desafio
- Crie uma outra API em outro framework como FAST API ou Flask ou Express JS

## Resumo dos Conceitos Importantes
- Serviço Web (ou Web API) é um sistema que permite a comunicação entre diferentes aplicações através da internet 
- Geralmente utiliza o protocolo HTTP para comunicação e troca de dados entre aplicações
- Frequentemente utiliza o formato JSON para troca de dados entre aplicações
- API REST é um tipo de serviço web que utiliza os princípios da arquitetura REST (Representational State Transfer) para comunicação entre aplicações
- APIs RESTful são projetadas para serem escaláveis e fáceis de usar, permitindo a integração entre diferentes sistemas

### Principal diferença entre Serviço Web e Aplicação Web Fullstack
- A principal diferença entre um serviço web e uma aplicação web fullstack é que o serviço web é projetado para fornecer dados e funcionalidades para outras aplicações, enquanto a aplicação web fullstack é projetada para fornecer uma interface de usuário completa e interativa para os usuários finais.
- Do ponto de vista do servidor, os serviços web geralmente respondem a requisições HTTP com dados em formato JSON ou XML, enquanto as aplicações web fullstack respondem a requisições HTTP com páginas HTML completas que podem incluir scripts, estilos e outros recursos.

### API Rest
- A API Rest possui diversas boas práticas que devem ser seguidas para garantir a escalabilidade e a facilidade de uso da API
- Algumas dessas boas práticas incluem:
- Usar os métodos HTTP corretos para cada operação (GET, POST, PUT, DELETE) 
- O CRUD em uma api REST geralmente utiliza os métodos HTTP da seguinte forma e com as seguintes tipos de rotas:
- **GET**: Para recuperar dados (ex: listar usuários, obter detalhes de um usuário)
- **POST**: Para criar novos dados (ex: adicionar um novo usuário)
- **PUT**: Para atualizar dados existentes (ex: editar informações de um usuário)
- **DELETE**: Para remover dados (ex: excluir um usuário)
- Usar URLs descritivas e significativas para identificar recursos (ex: `/users/` para listar usuários, `/users/{id}/` para obter detalhes de um usuário)
- Usar códigos de status HTTP apropriados para indicar o resultado da operação (ex: 200 OK, 201 Created, 204 No Content, 400 Bad Request, 404 Not Found, 500 Internal Server Error)
- Documentar a API de forma clara e acessível, incluindo exemplos de requisições e respostas para cada endpoint.

### Open API (Swagger)
- OpenAPI é uma especificação para descrever APIs RESTful de forma padronizada e legível por máquinas
- Permite que desenvolvedores e ferramentas entendam como a API funciona, quais endpoints estão disponíveis, quais parâmetros são necessários e quais respostas podem ser esperadas
- O Swagger é uma ferramenta que utiliza a especificação OpenAPI para gerar documentação interativa para APIs RESTful, permitindo que desenvolvedores testem os endpoints diretamente na documentação

### REST Clients - Postman, Insomnia e Bruno
- Postman, Insomnia e Bruno são ferramentas populares para testar APIs RESTful
- Cada uma delas possui características únicas que podem ser vantajosas dependendo do contexto de uso.
- Utilizamos essas ferramentas para testar as APIs RESTful que criamos 

## Passo a passo realizado no projeto Café com Pão

### 1. Implementação da Busca de Receitas com Spoonacular API

#### 1.1 Configuração Inicial
1. **Instalação de dependências**
   - Adicionamos a biblioteca `requests` ao `requirements.txt` para realizar requisições HTTP
   - A biblioteca `requests` permite fazer chamadas a APIs externas de forma fácil e intuitiva

2. **Configuração da API Key**
   - Adicionamos a `SPOONACULAR_API_KEY` no arquivo `.env`
   - A chave é importada no `settings.py` usando `environ.get()` para manter a segurança
   - Exemplo: `SPOONACULAR_API_KEY = environ.get('SPOONACULAR_API_KEY')`

3. **Imports necessários no views.py**
   - `import requests` - Para fazer requisições HTTP
   - `from django.conf import settings` - Para acessar a API key configurada

#### 1.2 Criação da View de Busca
A view `recipe_search()` em [app/views.py](app/views.py) implementa a funcionalidade:

```python
def recipe_search(request):
    recipes = []
    query = request.GET.get('query', '')
    error_message = None
    
    if query:
        try:
            api_key = settings.SPOONACULAR_API_KEY
            url = "https://api.spoonacular.com/recipes/complexSearch"
            params = {
                'apiKey': api_key,
                'query': query,
                'number': 12,  # Número de resultados
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()  # Lança exceção para status 4XX/5XX
            
            data = response.json()
            recipes = data.get('results', [])
            total_results = data.get('totalResults', 0)
            
        except requests.RequestException as e:
            error_message = f"Não foi possível buscar receitas: {str(e)}"
    
    context = {
        'recipes': recipes,
        'query': query,
        'error_message': error_message,
    }
    
    return render(request, 'recipes/search.html', context)
```

#### 1.3 Template de Busca
Criamos o template [templates/recipes/search.html](templates/recipes/search.html) que:
- Exibe um formulário de busca com input para query
- Mostra resultados em grid responsivo (1 a 4 colunas dependendo da tela)
- Cada card exibe imagem, título e link para a receita completa
- Trata erros e mensagens vazias adequadamente

#### 1.4 Rota URL
Adicionamos a rota em [config/urls.py](config/urls.py):
```python
path('receitas/buscar/', views.recipe_search, name='recipe_search'),
```

---

### 2. Criação da API REST com Django Ninja

#### 2.1 O que é Django Ninja?
- Django Ninja é um framework moderno para construir APIs REST em Django
- Utiliza type hints do Python para validação automática de dados
- Gera documentação Swagger automaticamente
- Possui suporte integrado para JWT authentication
- Oferece melhor performance em relação a outras alternativas

#### 2.2 Estrutura da API

A pasta [app/api/](app/api/) contém toda a implementação:

```
app/api/
├── __init__.py          # Inicialização e configuração da API
├── auth.py              # Endpoints de autenticação
├── cestas.py            # Endpoints de cestas
├── contato.py           # Endpoints de contato
├── padarias.py          # Endpoints de padarias
├── perfil.py            # Endpoints de perfil
├── assinaturas.py       # Endpoints de assinaturas
└── schemas.py           # Schemas de validação
```

#### 2.3 Configuração Inicial em app/api/__init__.py

```python
from ninja import NinjaAPI
from ninja_extra import exceptions
from ninja_jwt.routers.obtain import obtain_pair_router
from ninja_jwt.routers.verify import verify_router

# Importar routers
from app.api.auth import router as auth_router
from app.api.padarias import router as padarias_router
from app.api.cestas import router as cestas_router
from app.api.contato import router as contato_router
from app.api.assinaturas import router as assinaturas_router
from app.api.perfil import router as perfil_router

# Criar instância da API
api = NinjaAPI(
    title="Café com Pão API",
    version="1.0.0",
    description="API do projeto Café com Pão - Padarias, Cestas e Assinaturas",
)

# Registrar routers
api.add_router("/auth/token", tags=["Auth"], router=obtain_pair_router)
api.add_router("/auth", auth_router)
api.add_router("/padarias", padarias_router)
api.add_router("/cestas", cestas_router)
api.add_router("/contato", contato_router)
api.add_router("/assinaturas", assinaturas_router)
api.add_router("/perfil", perfil_router)
```

#### 2.4 Exemplo de um Router - Cestas

```python
# app/api/cestas.py
from ninja import Router, Query
from app.models import Cesta
from .schemas import CestaSchema

router = Router()

@router.get("/", response=list[CestaSchema], tags=['Cestas'])
def list_cestas(request, skip: int = Query(0), limit: int = Query(10)):
    return Cesta.objects.all()[skip : skip + limit]

@router.get("/{cesta_id}", response=CestaSchema, tags=['Cestas'])
def retrieve_cesta(request, cesta_id: int):
    return Cesta.objects.get(id=cesta_id)

@router.post("/", response=CestaSchema, tags=['Cestas'])
def create_cesta(request, payload: CestaSchema):
    cesta = Cesta.objects.create(**payload.dict())
    return cesta
```

#### 2.5 Schemas de Validação

Os schemas definem a estrutura dos dados que a API aceita e retorna:

```python
# app/api/schemas.py
from ninja import Schema
from datetime import datetime

class CestaSchema(Schema):
    id: int = None
    nome: str
    descricao: str
    preco: float
    ativa: bool = True

class PadariaSchema(Schema):
    id: int = None
    nome: str
    endereco: str
    telefone: str
    horario: str
```

#### 2.6 Registrar a API no urls.py

```python
# config/urls.py
from app.api import api

urlpatterns = [
    # ... outras rotas ...
    path('api/', api.urls),  # Registra todos os endpoints da API
] + static(...)
```

#### 2.7 Documentação Automática

Com Django Ninja, a documentação Swagger é gerada automaticamente:
- Acesse `http://localhost:8000/api/docs/` para visualizar
- Acesse `http://localhost:8000/api/redoc/` para visualização alternativa
- Todos os endpoints, parâmetros e tipos são documentados automaticamente

#### 2.8 Métodos HTTP Utilizados

| Método | Rota | Operação |
|--------|------|----------|
| GET | `/api/cestas/` | Listar todas as cestas |
| GET | `/api/cestas/{id}/` | Obter detalhes de uma cesta |
| POST | `/api/cestas/` | Criar uma nova cesta |
| PUT | `/api/cestas/{id}/` | Atualizar uma cesta |
| DELETE | `/api/cestas/{id}/` | Deletar uma cesta |

---

### 3. Integração e Testes

#### 3.1 Testando a Busca de Receitas
- Acessar `http://localhost:8000/receitas/buscar/`
- Digitar um termo de busca (ex: "pasta", "frango")
- A API Spoonacular retorna até 12 receitas com imagem e título

#### 3.2 Testando a API REST
- Usar ferramentas como Postman, Insomnia ou Bruno
- Fazer requisições para `http://localhost:8000/api/cestas/`
- Testar CRUD completo (Create, Read, Update, Delete)

#### 3.3 Tratamento de Erros
- Exceções em `recipe_search()` são capturadas e exibidas ao usuário
- A API retorna códigos HTTP apropriados (200, 201, 400, 404, 500)
- Mensagens de erro são fornecidas em formato JSON

