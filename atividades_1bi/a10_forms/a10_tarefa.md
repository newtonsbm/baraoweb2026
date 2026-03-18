# A10 - Formulários e Envio de Dados

## Atividade na Aula

### Parte 1:
- Instale as dependências necessárias para o projeto com o comando `uv sync` ou `pip install -r requirements.txt` na pasta do projeto
- Adicione um novo campo no formulário de contato para receber o telefone do usuário
- O campo deve ser do tipo `tel` e deve ser obrigatório
- Inclua o print do telefone no console quando o formulário for enviado
- Altere a view para processar o campo do telefone e exibir a mensagem de sucesso

### Parte 2: 
- Crie as páginas de listagem de padarias a partir do protótipo `padarias_list.html`, é necessário criar a view `padarias_list` e a rota para essa view corretamente para exibir a página de listagem de padarias. Nesse momento vamos mocar os dados de padarias na view para exibir a listagem de padarias no template `padarias_list.html` mas no futuro vamos substituir essa página com dados do banco de dados.

### Desafio
- Veja como funciona envio de emails em Django e configure esse processo para enviar um email de contato para o administrador do site com os dados do formulário de contato


## Resumo dos Conceitos Importantes

- Formulários são elementos HTML que permitem a coleta de informações dos usuários
- Existem vários tipos de elementos para entrada de dados tais como: `input`, `textarea`, `select`, `radio`, `checkbox`, `button`, etc
- Os formulários são enviados para o servidor por meio de requisições HTTP geralmente utilizando o método POST mas também pode ser utilizado o método GET
- Cada campo do formulário tem um nome (atributo `name`) que é enviado para o servidor como uma chave de um dicionário com o valor do campo como valor da chave
- Na `view` do Django, os dados do formulário são acessados por meio do objeto `request.POST` que é um dicionário com os dados do formulário
- O Django, assim como outros frameworks web, possui um sistema de formulários que facilita a criação, validação e processamento de formulários (ver mais sobre formulários em Django)
- Podemos enviar variáveis da `view` para o `template` para exibir mensagens de sucesso ou erro após o envio do formulário
- Isso é feito por meio do contexto do template que é um dicionário com as variáveis que queremos enviar para o template
- O método `render` é utilizado para renderizar um template e enviar o contexto para o template

## Passos realizados no projeto Café com Pão

### Enviando dados da View para os Componentes

- O método `render` do Django aceita um terceiro argumento chamado **contexto** (`context`), que é um dicionário Python com as variáveis que queremos disponibilizar no template
- As chaves do dicionário se tornam variáveis acessíveis dentro do template e de todos os componentes incluídos por ele
- Na view `padarias_list`, criamos uma lista de dicionários com dados "mocados" de padarias e passamos essa lista para o template via contexto:

```python
def padarias_list(request):
    padarias = [
        {
            'id': 1,
            'nome': 'Padaria do João',
            'endereco': 'Rua A, 123',
            'telefone': '(11) 98765-4321',
            'horario': '6h às 20h',
            'imagem': 'padaria1.png'
        },
        # ...
    ]
    return render(request, 'padarias_list.html', {'padarias': padarias})
```

- No template `templates/padarias_list.html`, acessamos a variável `padarias` usando a sintaxe `{{ variavel }}` do Django Template Language
- Para iterar sobre a lista de padarias utilizamos a tag `{% for padaria in padarias %}`, que permite percorrer cada item da lista e renderizar um bloco de HTML para cada um
- Dentro do loop, cada propriedade do dicionário é acessada com `{{ padaria.nome }}`, `{{ padaria.endereco }}`, etc:

```html
{% for padaria in padarias %}
<div class="card bg-base-100 shadow-xl">
  <div class="card-body">
    <h2 class="card-title">{{ padaria.nome }}</h2>
    <span>{{ padaria.endereco }}</span>
    <a href="tel:{{ padaria.telefone }}">{{ padaria.telefone }}</a>
    <span>{{ padaria.horario }}</span>
  </div>
</div>
{% endfor %}
```

- Esse padrão (view → contexto → template) é a base para tornar as páginas dinâmicas em Django: a view busca ou prepara os dados, e o template apenas os exibe

### Configurando a pagina de Contato

- Configurar o action e o method do formulário em `templates/contato.html` para enviar os dados para a view `contato`
- CSRF (Cross-Site Request Forgery) é um tipo de ataque que ocorre quando um invasor envia uma requisição maliciosa 
- CSRF pode acontecer por meio formulários que não possuem proteção contra CSRF
- O Django possui um sistema de proteção contra CSRF que é ativado por padrão
- Para utilizar o sistema de proteção CSRF, é necessário incluir o token CSRF no formulário
- O token CSRF é gerado dinamicamente pelo Django e é incluído no formulário por meio da template tag `{% csrf_token %}` 
- Foi incluso o token CSRF no formulário em `templates/contato.html`
- Alterar action do formulário para apontar para view 'contato' e o method para POST

```html
<form action="{% url 'contato' %}" method="post" class="my-10">
    {% csrf_token %}

```

- No arquivo `padarias/views.py` alteramos a view `contato` para processar o formulário enviado pelo usuário
- Caso a requisição não for do tipo POST, retornar o template `contato.html` com o formulário vazio
- Caso a requisição for do tipo POST, acessar os dados do formulário por meio do objeto `request.POST`, printar os valores no console e retornar o template `contato.html` com uma mensagem de sucesso
- Para enviar uma mensagem de sucesso para o template, podemos utilizar o método `render` que recebe um dicionário com os dados que queremos enviar para o template como contexto
- Essa é uma forma de enviar variáveis da `view` para o `template` de modo a tornar o template dinâmico
- O método `render` recebe o objeto `request`, o nome do template e um dicionário com os dados que queremos enviar para o template como contexto

```python

def contato(request):

    form_message = None

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        rating = request.POST.get('rating')
        message = request.POST.get('message')

        # Simular o processamento do email printando no console
        print(f"Email de {name} ({email})")
        print(f"Assunto: {subject}")
        print(f"Avaliação: {rating} estrelas")
        print(f"Mensagem: {message}")

        form_message = f"Obrigado pelo seu feedback, {name}! Recebemos sua mensagem e em breve entraremos em contato."

    context = {
        'form_message': form_message
    }
    return render(request, 'contato.html', context)

```

- Adicionamos um feedback para o usuário após o envio do formulário, exibindo uma mensagem de sucesso personalizada com o nome do usuário
- Verifique que isso foi feito por meio do contexto do template, onde a variável `form_message` é enviada para o template e exibida dinamicamente no template `contato.html`
- No arquivo `templates/contato.html` adicionar um bloco de código para exibir a mensagem de sucesso

```html
  <!-- INICIO DO MAIN HOME -->
  <main class="max-w-4xl mx-auto my-20 p-2">
    {% if form_message %}
      <div class="p-10 mb-4 text-green-800 bg-green-50 border-l-4 border-green-300 rounded-lg shadow-md" role="alert">
        <h2 class="text-2xl font-bold">Muito Obrigado!</h2>
        <p class="text-lg">{{ form_message }}</p>
        <div class="text-center text-9xl">
          🎉
        </div>
        <a class="btn mt-4" href="{% url 'contato' %}">Enviar nova mensagem</a>
      </div>
    {% else %}
      <h1 class="text-4xl">Fale Conosco</h1>
      <form action="{% url 'contato' %}" method="post" class="my-10">
        {% csrf_token %}
        <fieldset class="fieldset">
          <legend class="fieldset-legend">Qual seu nome?</legend>
          <input type="text" class="input" name="name" placeholder="Digite aqui" required />
        </fieldset>

        <fieldset class="fieldset">
          <legend class="fieldset-legend">Qual seu email?</legend>
          <input type="email" class="input" name="email" placeholder="Digite um email válido" required />
        </fieldset>

        <fieldset class="fieldset">
          <legend class="fieldset-legend">Qual o assunto?</legend>
          <input type="text" class="input" name="subject" placeholder="Digite o assunto" required />
        </fieldset>
        
        <fieldset class="fieldset">
          <legend class="fieldset-legend">Qual a sua avaliação da nossa proposta?</legend>
          <div class="rating">
            <input type="radio" name="rating" class="mask mask-star-2 bg-orange-400" aria-label="1 star" value="1" required />
            <input type="radio" name="rating" class="mask mask-star-2 bg-orange-400" aria-label="2 star" value="2" required />
            <input type="radio" name="rating" class="mask mask-star-2 bg-orange-400" aria-label="3 star" value="3" required />
            <input type="radio" name="rating" class="mask mask-star-2 bg-orange-400" aria-label="4 star" value="4" required />
            <input type="radio" name="rating" class="mask mask-star-2 bg-orange-400" aria-label="5 star" value="5" required />
          </div>
        </fieldset>

        <fieldset class="fieldset">
          <legend class="fieldset-legend">Mensagem</legend>
          <textarea maxlength="512" class="textarea h-24" name="message" placeholder="Mensagem" required></textarea>
        </fieldset>

        <button class="btn btn-primary my-4">Enviar</button>
      </form>
    {% endif %}
  </main>
  <!-- FIM DO MAIN HOME -->
```

### Execute e Verifique

- Rodar o servidor de desenvolvimento `uv run manage.py runserver` ou `python manage.py runserver` e acessar a página `http://localhost:8000/contato` no navegador
- Preencher o formulário e enviar
- Verifique se os dados do formulário são exibidos corretamente no console do servidor
- Verifique se a página de contato é exibida corretamente com o formulário e a mensagem de sucesso
