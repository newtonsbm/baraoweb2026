# A6 Python e Gerenciadores de Pacotes

## Atividades
- Instalar Python e Django
- Instalar o UV
- Iniciar um projeto Django e rodar o servidor localmente
- Analisar a estrutura de um projeto Django e entender os arquivos principais

### Plus
- Instale o node
- Instale o vite
- Crie um projeto com vite + vanilla JS

## Conteudo da Aula

Python é uma linguagem de programação de alto nível, interpretada e multi-paradigma. É muito utilizada para desenvolvimento backend, ciência de dados, automação e muito mais.

### Pip
- O pip é o gerenciador de pacotes oficial do Python
- Vem instalado por padrão com o Python
- Permite instalar bibliotecas e frameworks de forma simples

### UV (Astral Package Manager)
- O UV é um gerenciador de pacotes moderno e extremamente rápido para Python
- Desenvolvido pela Astral (mesma empresa do Ruff)
- É escrito em Rust e é muito mais rápido que o pip
- Gerencia ambientes virtuais e dependências de forma mais eficiente

### Instalar o UV (Recomendado)

- Entre no site do UV e siga o passo a passo para instalar no seu SO
- Rodar o comando de instalação do UV disponivel no site oficial

Verifique a instalação:

```bash
uv --version
```

- Instalar o python com uv

```bash
uv install python --version 3.13
```

### Instalar somente o Python (Alternativa)

1. Acesse https://www.python.org/downloads/
2. Baixe a versão mais recente
3. Execute o instalador
4. **ATENÇÃO**: Marque a opção "Add Python to PATH" antes de clicar em "Install Now"
5. Após a instalação, abra o PowerShell e verifique:
Alternativa:
- uma outra opcao é instalar via `winget` com o comando `winget install Python.Python.3` (recomendada para evitar problemas de PATH)

```bash
python --version
pip --version
```

### 3) Instalar Django com UV, Criar Projeto e Rodar Servidor

Garanta que você esteja dentro do repositório do projeto no terminal.

**Passo 1: Inicializar projeto com UV**

```bash
uv init nome_do_projeto
cd nome_do_projeto
```

**Passo 2: Adicionar Django como dependência**

```bash
uv add django
```

O UV criará automaticamente um ambiente virtual e gerenciará as dependências no arquivo `pyproject.toml`.

**Passo 3: Criar estrutura Django**

```bash
uv run django-admin startproject config .
```

O `.` no final indica para criar no diretório atual.

**Passo 4: Criar um app Django**

```bash
uv run manage.py startapp app
```

**Passo 5: Iniciar o servidor**

```bash
uv run manage.py runserver
```

O servidor estará rodando em: http://127.0.0.1:8000/

---

### Alternativa: Instalar Django com pip, Criar Projeto e Rodar Servidor

Garanta que você esteja dentro do repositório do projeto no terminal.

**Passo 1: Instalar Django globalmente**

```bash
pip install django
```

**Passo 2: Criar pasta do projeto e entrar nela**

```bash
mkdir nome_do_projeto
cd nome_do_projeto
```

**Passo 3: Criar estrutura Django**

```bash
django-admin startproject config .
```

No Windows, caso o comando acima não funcione, use:

```bash
python -m django startproject config .
```

ou

```bash
py -m django startproject config .
```

O `.` no final indica para criar no diretório atual.

**Passo 4: Criar um app Django**

```bash
python manage.py startapp app
```

**Passo 5: Iniciar o servidor**

```bash
python manage.py runserver
```

O servidor estará rodando em: http://127.0.0.1:8000/