# Django Starter

Um template starter para projetos Django moderno com configurações otimizadas para desenvolvimento, componentes reutilizáveis e styling moderno.

## Features

- **Django 6.x+** - Framework web Python
- **UV** - Package manager rápido e moderno
- **Django Cotton** - Sistema de componentes reutilizáveis
- **Django Browser Reload** - Auto-reload do navegador durante desenvolvimento
- **Tailwind CSS** - Framework CSS utilitário
- **DaisyUI** - Componentes UI baseados em Tailwind
- **Configurações de Desenvolvimento** - Settings otimizados para dev local

## Tecnologias

### Backend
| Tecnologia | Descrição |
|-----------|-----------|
| Django 6.x | Framework web |
| UV | Package manager |
| Django Cotton | Componentes reutilizáveis |
| Django Browser Reload | Auto reload em desenvolvimento |
| Python 3.10+ | Linguagem base |

### Frontend
| Tecnologia | Descrição |
|-----------|-----------|
| Tailwind CSS | Framework CSS |
| DaisyUI | Componentes UI |
| HTML5 | Markup |

## Instalação

### 1) Clonar o repositório

```bash
git clone <url-do-repositorio>
cd django_starter
```

### 2) Criar ambiente virtual e instalar dependências

**Com UV (recomendado):**

```bash
uv sync
```

**Com pip:**

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3) Executar migrações

```bash
python manage.py migrate
```

### 4) Coletar arquivos estáticos (se necessário)

```bash
python manage.py collectstatic
```

### 5) Rodar servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000/

## Estrutura do Projeto

```
django_starter/
├── manage.py
├── requirements.txt
├── pyproject.toml           # Configuração UV
├── README.md
├── tailwind.config.js       # Config Tailwind + DaisyUI
├── config/                  # Configurações Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── app/                    # App principal
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── admin.py
├── static/                 # Arquivos CSS gerado
│   └── css/
│       └── style.css
├── templates/              # Templates HTML
│   ├── components/        # Cotton components
│       ├── layouts.html
│           ├── base.html
│   └── pages/
└── media/                 # Arquivos de usuários
```

## Comandos 

```bash
# Criar admin
python manage.py createsuperuser

# Fazer migrations
python manage.py makemigrations
python manage.py migrate

# Shell Django
python manage.py shell

# Coletar estáticos
python manage.py collectstatic

# Rodar testes
python manage.py test

```

## Autenticação JWT com Logout

Este projeto implementa autenticação JWT usando `django-ninja-jwt` com suporte a blacklist para invalidação de tokens no logout.

### Configuração

O app `ninja_jwt.token_blacklist` está habilitado em `INSTALLED_APPS` para gerenciar tokens invalidados.

### Fluxo de Autenticação

#### 1. Registrar Novo Usuário
```bash
POST /api/auth/register/
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "senha123",
  "first_name": "João",
  "last_name": "Silva"
}
```

**Resposta (201):**
```json
{
  "id": 1,
  "username": "user@example.com",
  "email": "user@example.com",
  "first_name": "João",
  "last_name": "Silva"
}
```

#### 2. Fazer Login (Obter Tokens)
```bash
POST /api/auth/token/pair/
Content-Type: application/json

{
  "username": "user@example.com",
  "password": "senha123"
}
```

**Resposta (200):**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

> **Importante:** Guarde tanto o `access` quanto o `refresh` token. O refresh será necessário para o logout.

#### 3. Acessar Rotas Protegidas
```bash
GET /api/perfil/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...
```

Use o **access token** no header Authorization.

#### 4. Fazer Logout (Invalidar Token)
```bash
POST /api/auth/logout/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...
Content-Type: application/json

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Resposta (200):**
```json
{
  "message": "Logout realizado com sucesso. Token invalidado."
}
```

> **Como funciona:** O refresh token é adicionado à blacklist do `ninja_jwt.token_blacklist`. Uma vez na blacklist, esse token não poderá mais ser usado para gerar novos access tokens.

### Testando com cURL

```bash
# 1. Registrar usuário
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"email":"teste@exemplo.com","password":"senha123","first_name":"Teste"}'

# 2. Fazer login e salvar tokens
RESPONSE=$(curl -s -X POST http://localhost:8000/api/auth/token/pair/ \
  -H "Content-Type: application/json" \
  -d '{"username":"teste@exemplo.com","password":"senha123"}')

ACCESS=$(echo $RESPONSE | jq -r '.access')
REFRESH=$(echo $RESPONSE | jq -r '.refresh')

# 3. Acessar rota protegida
curl http://localhost:8000/api/perfil/ \
  -H "Authorization: Bearer $ACCESS"

# 4. Fazer logout
curl -X POST http://localhost:8000/api/auth/logout/ \
  -H "Authorization: Bearer $ACCESS" \
  -H "Content-Type: application/json" \
  -d "{\"refresh\":\"$REFRESH\"}"

# 5. Tentar acessar novamente (deve falhar se o access token expirou ou foi renovado com o refresh invalidado)
curl http://localhost:8000/api/perfil/ \
  -H "Authorization: Bearer $ACCESS"
```

### Migrations

Após adicionar o `ninja_jwt.token_blacklist`, execute as migrations:

```bash
python manage.py migrate
```

Isso criará as tabelas necessárias para armazenar os tokens na blacklist.

### Administração

Os tokens invalidados podem ser visualizados e gerenciados no Django Admin em:
- **Home > Token Blacklist**

