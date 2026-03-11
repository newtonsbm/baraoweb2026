# A8 - Projeto Django e Rotas

## Atividade - Adicionando Novas Rotas

**Iniciar o ambiente de desenvolvimento**
- Certifique-se de que o ambiente virtual está ativado e as dependências instaladas
- Garanta que esta na pasta do projeto `django_starter` onde esta o arquivo `manage.py`
```bash
cd django_starter
```

Utilizando `uv`:
- inicie o ambiente de desenvolvimento com o comando:
```bash
uv sync
```
- Verifique que o servidor de desenvolvimento está rodando corretamente:
```bash
uv run manage.py runserver
```

Utilizando `pip`:
- Instalte as dependências do projeto:
```bash
pip install -r requirements.txt
```
- inicie o ambiente de desenvolvimento com o comando:
```bash
python manage.py runserver
```


Agora Para criar uma nova página, siga estes passos:

**1. Crie a view em `app/views.py`:**

```python
def sobre(request):
    return render(request, 'sobre.html')
```

**2. Adicione a rota em `config/urls.py`:**

```python
urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),  # Nova rota
    path('admin/', admin.site.urls),
]
```

**3. Crie o template `templates/sobre.html`:**

```html
<c-layouts.base>
  <h1>Sobre o Projeto</h1>
</c-layouts.base>
```

**4. Acesse** `http://localhost:8000/sobre/`

**5. Crie outras 3 notas páginas seguindo o mesmo processo (views, urls e templates)**
- Exemplos de páginas: `/contato/`, `/produtos/`, `/servicos/`, `/portfolio/`, etc.

## Plus - Muito Recomendado 

- Verifique o arquivo `templates/components/header.html` para ver como funciona os links entre páginas usando a tag `{% url 'nome_da_rota' %}`
- Adicione links para as novas páginas no header


## Resumo dos Conceitos Importantes

Nesta atividade vamos explorar de uma aplicação web fullstack. Diversos frameworks fullstack utilizam o padrão [MVC (Model-View-Controller)](https://developer.mozilla.org/en-US/docs/Glossary/MVC) que no caso particular do django utiliza uma variação desse modelo chamado [MVT (Model-View-Template)](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction). 

Todo framework de desenvolvimento web terá uma estrutura de pastas e arquivos que são necessários para o funcionamento do projeto. No caso do Django, temos a pasta do projeto principal que contém as configurações gerais (settings.py). Além disso todo framework também terá ferramentas de linha de comando (cli tools) que facilitam a criação de novos componentes do projeto além de outros utilitários. No caso do django essas ferramentas são o django-admin e o manage.py.

Um conceito importante é o de *roteamento* das requisições. As rotas são responsáveis por mapear as URLs acessadas pelo usuário para o código que irá tratar dessa requisiçao. No django, as views são responsáveis por processar as requisições e retornar uma resposta ao usuário. No caso do Django, as views são funções que recebem um objeto `request` e retornam um objeto `response`.

Vamos utilizar como referência o projeto django-starter já configurado para explorar alguns conceitos fundamenteis de frameworks web, no contexto do Django. Vamos explorar a estrutura do projeto e o sistema de rotas e como funcionam na prática com views, templates e urls.

## Explicaçao - Django Starter

A estrutura do projeto Django Starter está organizada da seguinte forma:

```
django_starter/
├── manage.py                 # CLI principal do Django
├── pyproject.toml           # Dependências (UV)
├── requirements.txt         # Dependências (pip)
├── config/                  # Pasta de configurações do projeto
│   ├── settings.py         # Configurações gerais
│   ├── urls.py             # Rotas principais (URLconf raiz)
│   ├── wsgi.py             # Servidor WSGI para produção
│   └── asgi.py             # Servidor ASGI para async
├── app/                     # App Django (módulo de funcionalidades)
│   ├── views.py            # Views (controladores de requisições)
│   ├── urls.py             # Rotas do app (opcional)
│   ├── models.py           # Models (banco de dados)
│   └── admin.py            # Configuração do Django Admin
├── templates/               # Templates HTML
│   ├── index.html          # Página inicial
│   ├── components/         # Componentes reutilizáveis (Cotton)
│   │   ├── header.html
│   │   └── layouts/
│   │       └── base.html   # Layout base
└── static/                  # Arquivos estáticos (CSS, JS, imagens)
    ├── css/
    └── images/
```

## Sistema de Roteamento (URLs)

O Django usa um sistema de roteamento baseado em URLconf (URL configuration). O fluxo de uma requisição funciona assim:

**Fluxo da Requisição:** `Browser → urls.py → views.py → template.html → Response`

### 1) URLconf Raiz: `config/urls.py`

Este é o **ponto de entrada** para todas as rotas do projeto. Fica na pasta de configurações.

```python
from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.index, name='index'),           # Rota raiz
    path('admin/', admin.site.urls),                # Django Admin
    path('__reload__/', include('django_browser_reload.urls')),
]
```

**Conceitos importantes:**
- `path('', views.index, name='index')` - Define que a URL raiz (`/`) chama a view `index`
- `name='index'` - Nome da rota, usado para referência em templates e código
- `path('admin/', ...)` - Rota para o painel administrativo
- `include()` - Inclui rotas de outros apps/módulos

### 2) Views: `app/views.py`

As views são **funções Python** que processam requisições HTTP e retornam respostas.

```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

**Conceitos importantes:**
- Toda view recebe um objeto `request` (requisição HTTP)
- `render()` renderiza um template HTML e retorna uma resposta
- Você pode passar dados para o template: `render(request, 'index.html', {'nome': 'João'})`

### 3) Templates / Componentes: `templates/index.html`

Templates são páginas HTML que podem conter **variáveis e lógica** usando a linguagem de templates do Django.

```html
{% load static %}
<c-layouts.base>
  <div class="hero bg-base-200 h-screen">
    <h1>Django Starter</h1>
  </div>
</c-layouts.base>
```

**Conceitos importantes:**
- `{% load static %}` - Carrega a tag para arquivos estáticos
- `{% static 'images/logo.png' %}` - Referencia arquivos em `/static/`
- `<c-layouts.base>` - Componente pai que representa o layout base (herança de templates)

## Fluxo Completo de uma Requisição

1. **Usuário acessa** `http://localhost:8000/`
2. **Django consulta** `config/urls.py` e encontra `path('', views.index)`
3. **Django executa** a função `index()` em `app/views.py`
4. **View renderiza** o template `templates/index.html`
5. **Django retorna** o HTML gerado como resposta HTTP
6. **Browser exibe** a página renderizada

## Principais Arquivos de Roteamento

| Arquivo | Função |
|---------|--------|
| `config/urls.py` | URLconf raiz - define todas as rotas do projeto |
| `app/views.py` | Views - processam requisições e retornam respostas |
| `config/settings.py` | Define o URLconf raiz em `ROOT_URLCONF` |
| `app/urls.py` | URLconf do app (opcional, para organização) |

