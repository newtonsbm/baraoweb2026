# A9 - Composição de Templates e Componentes e Arquivos Estáticos

## Atividade na Aula

- Vamos criar o layout de acordo o prototipo da página café com pão que esta na pasta `docs` do projeto `cafecompao`
- Altere o header para representar o header do `protótipo`
- A partir do protótipo, criar o componente de `footer.html` na pasta `templates/components` e incluir esse componente no layout base `base.html` para que ele seja exibido em todas as páginas do site
- Alterar o `index.html` para incluir o conteúdo do main que esta na página do protótipo
- Copiar as imagens do protótipo para a pasta `static/images`
- Fazer o mesmo processo feito para home porém para a página `contato.html`
  - Criar template `contato.html` que herda do componente de layout base 
  - Alterar a view para retornar o template `contato.html`
  - Criar a rota para a view `contato` em `urls.py`
  - Alterar o menu principal em `templates/components/header.html` para incluir o link para a página de contato
- Alterar as rotas das imagens e das URLs corretamente usando a tag `{% static %}` e `{% url %}`

### Dicas 

- Rota nova em `urls.py`

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contato/', views.contato, name='contato'), # Nova rota para a página de contato
] 
```

## Resumo dos Conceitos Importantes

Existem diferentes libs e frameworks que permitem a composição de templates e componentes. Essas libs permitem que os desenvolvedores criem templates reutilizáveis e componentes que podem ser utilizados em diferentes partes da aplicação. Um componente é um bloco de código que pode ser reutilizado em diferentes partes da aplicação. Um componente pode ser um cabeçalho, um rodapé, um menu, um formulário, etc. A composição de templates e componentes é uma técnica poderosa que permite a reutilização de código e a criação de interfaces consistentes. 
Frameworks de desenvolvimento web em geral implementam sistemas de templating que usam de duas abordagens principais para construção das páginas web: composição (por meio da inclusão de componentes) e herança (por meio da extensão desses componentes ou templates). 
Os sistemas de template e componentização variam muito em termos de complexidade indo desde de formas simples como componentes web nativos, passando por sistemas de template que criam componentes de baixa/média complexidade (como é o caso do Django) até sistemas de componentização com JSX que permitem incorporar diversos comportamentos diretamente no componente (como é o caso do React e Svelte).
No Django, a composição de templates é feita através de tags e filtros que permitem a inclusão de componentes dentro de outros templates. Além disso, o Django possui um sistema de herança de templates que permite a criação de templates base e a extensão desses templates em outros templates. [Ver mais sobre templates em Django.](https://docs.djangoproject.com/en/6.0/topics/templates/)

## Alterações no Projeto Django Starter

- Analise as mudanças feitas no projeto Django Starter para criar a página inicial (home) utilizando o sistema de templates do Django e compondo a página com componentes reutilizável de header.
- Vamos utilizar como base os protótipos HTML criados anteriormente que estão na pasta `cafecompao/docs/prototipos`
- Cria componente de `header.html` na pasta `templates/components` 
- Criado o layout base `base.html` na pasta `templates/components/layouts` para incluir o header e definir o slot de conteúdo principal
- Criar o template `home.html` que herda do layout base e inclui o conteúdo específico da página inicial
- Colocar link para a página inicial no menu do header utilizando a template tag `{% url 'home' %}` para gerar a URL correta para a rota da página inicial
- A `{% url 'home' %}` é uma tag especial do Django que é utilizada para gerar a URL correta para a rota especificada. No caso do desenvolvimento local a URL será `http://localhost:8000/home` e em produção a URL será algo como `http://www.cafecompao.com/home`
- Essa tag é muito útil para evitar hardcoding de URLs no código e para garantir que as URLs sejam geradas corretamente dependendo do ambiente de execução (desenvolvimento ou produção)

## Explicação Extra

### Arquivos Estáticos - Imagens e CSS

- No desenvolvimento local, os arquivos estáticos são servidos pelo servidor de desenvolvimento. Em produção, os arquivos estáticos são servidos por um servidor de arquivos estáticos como o `whitenoise`, um bucket (S3 ou GCP) ou uma CDN (Content Delivery Network). Neste caso a template tag `static` irá gerar a URL correta para o arquivo estático dependendo do ambiente de execução.
- A tag `{% load static %}` é utilizada para carregar os arquivos estáticos como imagens, css e js dinamicamente
- Isso significa que cada arquivo estático terá uma rota específica que será gerada dinamicamente pelo Django
- Essa rota pode estar no próprio servidor de desenvolvimento ou em um servidor de arquivos estáticos em produção ou em um bucket ou CDN
- Outro tipo de arquivo estático são arquivos de mídia como imagens, vídeos, áudios, etc
- Geralmente esses arquivos são armazenados em um diretório específico chamado `media` e são servidos por um servidor de arquivos estáticos ou por um servidor de mídia
- Vamos carregar dinamicamente as rotas estáticas e de arquivos de mídia em `urls.py` 

```python	
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', padarias_views.home, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- A função `static` é utilizada para carregar as rotas estáticas e de arquivos de mídia dinamicamente
- Vamos configurar as váriaveis `STATIC_URL`, `STATIC_ROOT`, `MEDIA_URL` e `MEDIA_ROOT` no arquivo `settings.py`

```python
STATIC_URL = '/static/'
STATIC_ROOT =  BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

- A variável `BASE_DIR` é utilizada para definir o diretório base do projeto Django
- O diretório `static` é utilizado para armazenar arquivos estáticos do projeto todo como imagens, css e js
- O diretório `media` é utilizado para armazenar arquivos de mídia relacionados aos model do projeto como imagens, vídeos, áudios, etc
- Copiar as imagens que estão em `doc/prototipos/images` para a pasta `static/images` do projeto

- Ajustar a url para imagens usando a tag `{% static 'caminho_da_imagem_na_pasta_static' %}`


- Arquivo `home.html`

```html
{% extends 'base.html' %}

{% load static %}

{% block content %}  

<h1> Página Home </h1>
<img src="{% static 'images/cafe.jpg' %}" alt="Café com Pão" />

{% endblock %}
```
- A tag `{% static 'images/cafe.png' %}` é utilizada para carregar a URL correta para a imagem 'cafe.png' que está na pasta `static/images` do projeto
- A mesma coisa podemos fazer para outros arquivos estáticos como css e js
