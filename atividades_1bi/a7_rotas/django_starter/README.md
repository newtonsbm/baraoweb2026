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
| Python 3.13+ | Linguagem base |

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
