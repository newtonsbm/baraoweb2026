# ORM do Django: Resumo Pratico

A ORM (Object Relational Mapper) do Django permite trabalhar com banco de dados usando classes Python, sem escrever SQL manual na maior parte do tempo.

## 1. Exemplo de Models

```python
from django.db import models


class Categoria(models.Model):
	nome = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.nome


class Autor(models.Model):
	nome = models.CharField(max_length=120)
	email = models.EmailField(unique=True)

	def __str__(self):
		return self.nome


class Livro(models.Model):
	titulo = models.CharField(max_length=150)
	preco = models.DecimalField(max_digits=8, decimal_places=2)
	publicado_em = models.DateField(null=True, blank=True)
	ativo = models.BooleanField(default=True)

	# Relacionamentos
	autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="livros")
	categorias = models.ManyToManyField(Categoria, related_name="livros", blank=True)

	def __str__(self):
		return self.titulo
```

## 2. Comandos principais

### 2.1 `makemigrations`

Gera os arquivos de migração com base nas alteracoes dos models.

```bash
uv run manage.py makemigrations
```

### 2.2 `migrate`

Aplica as migrações no banco de dados.

```bash
uv run manage.py migrate
```

### 2.3 `loaddata`

Carrega dados de fixtures (JSON, YAML, XML) para popular o banco.

```bash
uv run manage.py loaddata dados_iniciais.json
uv run manage.py loaddata fixtures/livros.json
```

Observacao: o comando correto e `makemigrations` (no plural).

## 3. CRUD com ORM

Considere que os models acima foram importados:

```python
from loja.models import Autor, Categoria, Livro
from datetime import date
```

### 3.1 Create (Criar)

```python
autor = Autor.objects.create(nome="Machado de Assis", email="machado@email.com")

cat_romance = Categoria.objects.create(nome="Romance")
cat_classico = Categoria.objects.create(nome="Classico")

livro = Livro.objects.create(
	titulo="Dom Casmurro",
	preco=49.90,
	publicado_em=date(1899, 1, 1),
	autor=autor,
)

livro.categorias.add(cat_romance, cat_classico)
```

### 3.2 Read (Consultar)

```python
# Todos
todos = Livro.objects.all()

# Um registro (erro se nao existir)
um_livro = Livro.objects.get(pk=1)

# Primeiro com filtro
primeiro_ativo = Livro.objects.filter(ativo=True).first()

# Ordenacao
mais_caros = Livro.objects.order_by("-preco")
```

### 3.3 Update (Atualizar)

```python
livro = Livro.objects.get(pk=1)
livro.preco = 59.90
livro.save()

# Atualizacao em lote (mais performatica)
Livro.objects.filter(ativo=False).update(ativo=True)
```

### 3.4 Delete (Remover)

```python
livro = Livro.objects.get(pk=1)
livro.delete()

# Remove todos que atendem ao filtro
Livro.objects.filter(ativo=False).delete()
```

## 4. Filtros com relacionamentos (related)

A ORM usa `__` (duplo underscore) para navegar por campos relacionados.

### 4.1 Filtro por `ForeignKey`

```python
# Livros de um autor pelo nome do autor
Livro.objects.filter(autor__nome__icontains="machado")

# Autores que possuem livros ativos
Autor.objects.filter(livros__ativo=True).distinct()
```

### 4.2 Filtro por `ManyToMany`

```python
# Livros de uma categoria especifica
Livro.objects.filter(categorias__nome="Romance")

# Categorias que possuem livro com preco maior que 50
Categoria.objects.filter(livros__preco__gt=50).distinct()
```

### 4.3 Exemplos uteis de lookup

```python
Livro.objects.filter(titulo__icontains="potter")   # contem (case-insensitive)
Livro.objects.filter(preco__gte=30, preco__lte=80)    # faixa de valores
Livro.objects.filter(publicado_em__year=1999)         # ano da data
Livro.objects.exclude(ativo=True)                     # negacao
```

## 5. Boas praticas rapidas

- Use `related_name` para facilitar consultas reversas.
- Use `select_related()` para `ForeignKey` e `prefetch_related()` para `ManyToMany` em consultas com desempenho critico.
- Prefira `get_object_or_404` em views quando buscar por ID.
- Use migrations pequenas e frequentes durante o desenvolvimento.

