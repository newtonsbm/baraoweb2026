# A13 - Fixtures e List e Detail de Cestas

## Atividade
- Escolha continuar o projeto anterior ou utilizar o projeto cafe com pão disponível nessa pasta
- Caso escolha continuar o projeto anterior, criar as fixtures para carregar os dados iniciais. Caso escolha utilizar o projeto cafe com pão, as fixtures já estão criadas entao navegue entre os arquivos e crie novas registros nas fixtures para praticar a criação de fixtures.
- Rode a migration para criar as tabelas no banco de dados com o comando `uv run manage.py migrate` ou `python manage.py migrate`
- Carregar as fixtures no banco de dados com o comando `uv run manage.py loaddata <nome_da_fixture>` ou `python manage.py loaddata <nome_da_fixture>`
- Se optar por continuar o projeto anterior, criar a página de listagem do model que foi criado (criar a view, a rota e o template para a página de listagem)
- Se optar por utilizar o projeto cafe com pão, criar a página de listagem de padarias alterando a view `padarias_list` e o template `templates/padarias/padarias_list.html` para exibir as padarias cadastradas no banco de dados.

### Desafio
- Criar a página de detalhe da padaria, olhe o protótipo definido para se basear.
- Crie um component de card da padaria para reutilizar o código e deixar o template mais limpo. O componente deve ser criado na pasta `templates/components` e deve ser utilizado no template de listagem de padarias e no template de detalhes da padaria.

## Resumo dos Conceitos Importantes

- Fixtures são arquivos que contém dados iniciais para popular o banco de dados. Fixtures são úteis para popular o banco de dados com iniciais para a aplicação (dados de configuração) ou muitas vezes com dados de teste.
- Fixtures podem ser criadas em diversos formatos como JSON, XML e YAML. O Django possui suporte nativo para JSON. Outro nome para Fixtures é Seeders ou Seed Data. 
- Uma vez criada a fixture, podemos carregar os dados no banco de dados com o comando `python manage.py loaddata <nome_da_fixture>`
- No Django, as fixtures são armazenadas na pasta `fixtures` dentro do app. O Django procura por arquivos de fixture nessa pasta e carrega os dados no banco de dados.
- CRUD - Create, Retrieve, Update e Delete. São as operações básicas de manipulação de dados em um banco de dados. O Django possui suporte nativo para essas operações através do ORM.
- Vamos criar fixture para carregar os dados iniciais de `Categoria`, `Produto` e `Cesta` no banco de dados. Vamos criar um arquivo JSON com os dados iniciais e carregar os dados no banco de dados com o comando `python manage.py loaddata <nome_da_fixture>`

##  Passo a passo do que foi realizado no projeto

### Carregar Fixtures

- Instale as dependências necessárias para o projeto com o comando `uv sync` ou `pip install -r requirements.txt`
- Verificar as fixtures disponíveis na pasta `padarias/fixtures`
- Carregar as fixtures com o comando `python manage.py loaddata <nome_da_fixture>`
- A ordem de carregamento das fixtures é importante. O Django carrega as fixtures na ordem em que foram criadas. Portanto, se uma fixture depende de outra, a fixture dependente deve ser carregada depois da fixture que ela depende.
- Essa dependência é feita por meio de chaves estrangeiras. Por exemplo, se a fixture de `Produto` depende da fixture de `Categoria`, a fixture de `Produto` deve ser carregada depois da fixture de `Categoria`
- Vamos carregar nessa ordem: `categorias`, `produtos`, `cestas`, `padarias` e `enderecos`

```bash
python manage.py loaddata categorias produtos cestas padarias enderecos
```

- Verificar se os dados foram carregados corretamente no banco de dados abrindo o admin do Django em `http://localhost:8000/admin/` após iniciar o servidor com o comando `python manage.py runserver` 
- As imagens referente aos produtos e cestas estão na pasta `media` que foi criada na raiz do projeto. O Django serve os arquivos estáticos da pasta `media` automaticamente. Isso é feito a partir da configuração `MEDIA_URL` e `MEDIA_ROOT` no arquivo `settings.py` e, no ambiente de desenvolvimento, no arquivo `urls.py` do projeto. 

### Listando Cestas

- Vamos alterar a view `cestas_list` em `padarias/views.py` para carregar todas as padarias do banco de dados e exibir na página `templates/cestas/cestas_list.html` 
- No arquivo `padarias/views.py`:

```python
# no inicio do arquivo importar os models
from .models import Padaria, Cesta

def cestas_list(request):
    cestas = Cesta.objects.all()
    context = {
        'cestas': cestas,
    }
    return render(request, 'cestas/cestas_list.html', context=context)
```

- Agora vamos alterar o template `templates/cestas/cestas_list.html` para exibir as padarias no lugar dos dados mocados
- No template poderemos acessar a lista de cestas por meio da variável `cestas` que foi passada no contexto da view
- Como essa variavel é uma lista, podemos iterar sobre ela com o comando `{% for cesta in cestas %}` e exibir os dados de cada padaria
- Também podemos verificar se existem cestas na lista com o comando `{% if cestas %}` e exibir uma mensagem caso não existam cestas cadastradas 

Alguns pontos importantes a se destacar:
- Verifique que estamos acessando a imagem da cesta com `{{ cesta.imagem.url }}`
- Podemos acessar os atributos de um objeto com o ponto. Por exemplo, para acessar o nome da cesta, utilizamos `{{ cesta.nome }}`
- Criamos um link para a página de detalhes da cesta com o comando `{% url 'cestas_detail' cesta.pk %}`. O `cesta.pk` é o id da cesta que foi gerado automaticamente pelo Django. O Django gera um id único para cada objeto criado no banco de dados. Esse id é chamado de `pk` (primary key) e é utilizado para identificar o objeto no banco de dados.
- Se rodarmos o servidor teremos um erro pois não criamos ainda a view e a rota para a página de detalhes da cesta. Vamos criar a view e a rota para a página de detalhes da cesta.

### Criar View e Rota para Detalhes da Cesta

- Precisamos criar a `view`, a rota em `urls.py` e o template na pasta `templates/cesta`
- Criar a view `cestas_detail` em `padarias/views.py` para exibir os detalhes da cesta. Essa view deve receber o `pk`(id) da cesta como parâmetro e carregar a cesta no banco de dados. Em seguida, deve passar a cesta para o template `templates/cestas/cestas_detail.html`.
- No arquivo `padarias/views.py`:

```python
def cestas_detail(request, pk):
    cesta = get_object_or_404(Cesta, pk=pk)
    context = {
        'cesta': cesta,
    }
    return render(request, 'cestas/cestas_detail.html', context)
```

- Vamos criar a rota para receber o `pk` da cesta em `padarias/urls.py`:

```python
urlpatterns = [
    ...
    path('cestas/<int:pk>/', padarias_views.cestas_detail, name='cestas_detail'), # INCLUIR ESSA ROTA
    ...
]
```

### Criar Template de Detalhes da Cesta

- Criar o template `templates/cestas/cestas_detail.html` para exibir os detalhes da cesta. Esse template deve exibir o nome, descrição, preço e imagem da cesta. Além disso, deve exibir os produtos que fazem parte da cesta.
- Utilizar como base o protótipo `prototipo/cestas_detail.html` e o template `templates/cestas/cestas_list.html` para criar o template de detalhes da cesta
- O template de detalhes da cesta exibe o nome, descrição, preço e imagem da cesta. Além disso, exibe os produtos que fazem parte da cesta em uma tabela. Para isso, utilizamos o comando `cesta.produtos.all` que retorna todos os produtos que fazem parte da cesta. Esse comando é gerado automaticamente pelo Django e utiliza o relacionamento de muitos para muitos entre os models `Cesta` e `Produto`.

