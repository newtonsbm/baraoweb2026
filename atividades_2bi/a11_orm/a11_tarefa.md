# A11 - Bancos de Dados e ORM - Introdução

## Atividade em Aula
- Instale as dependências necessárias para o projeto com o comando `uv sync` ou `pip install -r requirements.txt` na pasta do projeto
- Em grupo pensar pensar em um modelo de dados novo 
- Pode ser referente a qualquer contexto, por exemplo, um modelo de dados para representar produtos, jogos, séries, pacientes, medicamentos, personagens de rpg, etc
- No projeto django_starter da pasta da ativiadade, criar esse modelo de dados em `app/models.py`, criar a migration para esse modelo e aplicar a migration para criar a tabela no banco de dados
- Verificar a tabela criada no banco de dados utilizando o sqlite browser 

### Desafios Opcionais
- Crie uma view e template para cadastrar um novo objeto do modelo de dados criado na atividade em aula e salve os dados no banco de dados utilizando o ORM do Django
- Siga o modelo de cadastro de que vimos Feedback

## Resumo dos Conceitos Importantes

Nesta atividade vamos trabalhar com bancos de dados e o ORM (Object Relational Mapping). O ORM é uma técnica de mapeamento de objetos para tabelas de banco de dados relacionais. O ORM permite que o desenvolvedor utilize objetos e métodos para manipular dados no banco de dados sem a necessidade de escrever SQL diretamente. Além de abstrair a comunicação com o banco de dados, o ORM facilita o desenvolvimento de consultas e lida com diversos aspectos como segurança, otimização, migrações e consistência dos dados.

O Django possui um ORM poderoso que permite a criação de modelos de dados, consultas complexas e migrações de banco de dados de forma simples e eficiente. [Ver mais sobre ORM em Django.](https://docs.djangoproject.com/pt-br/6.0/topics/db/models/)

Outros conceitos que vamos ver é o de migrations e fixtures. Migrations são arquivos que contém as alterações no banco de dados e são gerados pelo ORM sempre que existe alguma alteração no modelo de dados. As migrations representam as alterações no banco de dados e portanto são versionadas e podem ser revertidas. Fixtures são arquivos que contém dados iniciais para popular o banco de dados. Fixtures são úteis para popular o banco de dados com dados de teste ou dados iniciais para a aplicação (dados de configuração).

Nesta aula vamos criar o modelo de dados para o Feedback enviado pelo usuário via formulário de contato, criar a migration para esse modelo e aplicar a migration para criar a tabela no banco de dados. Além disso, vamos verificar os dados no banco de dados utilizando o sqlite browser. 

## Tabela de Feedback

![Modelo de Dados](doc/feedback-table.png)

### Criar Model de Feedback 

- Models são classes que representam as tabelas do banco de dados. Cada atributo da classe representa uma coluna da tabela. O Django possui diversos tipos de campos que representam os tipos de dados do banco de dados. [Ver mais sobre modelos de dados em Django.](https://docs.djangoproject.com/en/5.0/topics/db/models/#fields)
- Vamos criar o modelo que representa o Feedback enviado pelo usuário via formulário de contato
- Foi criado o modelo de dados para `Feedback` em `padarias/models.py`

```python
class Feedback(models.Model):

    nome = models.CharField("Nome", max_length=100)
    email = models.EmailField("Email")
    assunto = models.CharField("Assunto", max_length=200)
    avaliacao = models.IntegerField("Avaliação")
    telefone = models.CharField("Telefone", max_length=20, null=True, blank=True)
    mensagem = models.TextField("Mensagem")
    

    def __str__(self):
      return f"Feedback de {self.nome} - {self.email} - {self.assunto}"

``` 

### Criar Migration

- Criar migration automaticamente para o modelo de dados `Feedback` com o comando `python manage.py makemigrations`
- Verificar que o arquivo de migration foi criado em `padarias/migrations`
- Aplicar a migration com o comando `py manage.py migrate`
- Verificar que a tabela `app_feedback` foi criada no banco de dados

### Verificar Dados no Banco de Dados

- Instalar o sqlite browser: https://sqlitebrowser.org/dl/
- Abrir o arquivo `db.sqlite3` que esta na raiz do projeto com o sqlite browser e verificar se as categorias foram carregadas corretamente
- Existe uma extensão no VS Code chamada `SQLite` que também pode ser utilizada para visualizar o banco de dados

### Salvar os dados de feedback na view de contato
- Alterar a view de contato para salvar os dados do formulário de contato no banco de dados utilizando o modelo de dados `Feedback` criado anteriormente.
- Para isso, vamos importar o modelo de dados `Feedback` na view de contato e criar um novo objeto de feedback com os dados do formulário e salvar esse objeto no banco de dados.

```python 
# app.views.py

from .models import Feedback

def contato(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        assunto = request.POST.get("assunto")
        avaliacao = request.POST.get("avaliacao")
        telefone = request.POST.get("telefone")
        mensagem = request.POST.get("mensagem")

        feedback = Feedback(
            nome=nome,
            email=email,
            assunto=assunto,
            avaliacao=avaliacao,
            telefone=telefone,
            mensagem=mensagem
        )
        feedback.save()

    return render(request, "contato.html")
```

