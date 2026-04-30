# A14 - Autenticação e Autorização

## Atividade

- Navegar nos arquivos e verificar como esta implementado o sistema de autenticação
- Vamos permitir adicionar novas informações ao usuário
- Para isso vamos criar um model chamado `Perfil` que tem relacao 1-1 com `User`
- O model `Perfil` deve conter os campos `telefone`, `cpf`, `data_nascimento` para armazenar o telefone e o CPF e a data de nascimento do usuário
- Vamos criar uma view para o usuario logado poder editar as informações do seu perfil. Essa view deve ser protegida com o decorator `login_required` para garantir que apenas usuários logados possam acessar essa área. O template dessa view deve conter um formulário para o usuário editar as informações do seu perfil. O formulário deve enviar os dados para a view de edição de perfil.
- Após criar a view, precisamos criar o template com form para editar o perfil e configurar a rota corretamente
- Por fim adicionar um link para a página de edição do perfil dentro da area logada (`dashboard`) para que o usuário possa acessar a página de edição do perfil facilmente.

* dica utilize de modo consciente o Copilot para auxiliar nessas etapas já que foram conceitos já vistos nas aulas anteriores

## Resumo dos Conceitos Importantes

- Autenticação é o processo de verificar a identidade de um usuário entre diferentes acessos e diferentes dispositivos.
- É necessário sempre ter uma forma de representar unicamente um usuário. Isso pode ser feito através de um nome de usuário, e-mail, telefone, token ou CPF. 
- Também é necessário uma forma de verificar se o usuário é quem ele diz ser. Isso pode ser feito através de uma senha, token, biometria ou outro método de autenticação.
- Existem diferentes formas de autenticação, como autenticação por senha, autenticação por token, autenticação por biometria, por servidores de autenticação, entre outras. O Django possui suporte nativo para autenticação por senha e autenticação por token.
- Autorização é o processo de verificar se um usuário tem permissão para acessar um recurso ou executar uma ação. Isso pode ser feito através de permissões, grupos e regras de acesso.
- O Django possui suporte nativo para autorização através de permissões e grupos. As permissões são utilizadas para verificar se um usuário tem permissão para acessar um recurso ou executar uma ação. Os grupos são utilizados para agrupar permissões e facilitar a atribuição de permissões a usuários.
- No modelo de Server Rendering, o usuário logado é identificado através de um cookie de sessão. O cookie de sessão é criado quando o usuário faz o login e é utilizado para identificar o usuário em requisições futuras. O Django possui suporte nativo para autenticação de usuários e gerenciamento de sessões. Isso é comum em outros frameworks como Ruby on Rails, Laravel, Spring, entre outros. Já no modelo de Client Rendering, o usuário logado é identificado através de um token JWT (JSON Web Token) que é enviado no header da requisição. O token JWT é criado quando o usuário faz o login e é utilizado para identificar o usuário em requisições futuras. O Django possui suporte nativo para autenticação por token através do pacote `djangorestframework-simplejwt` que pode ser utilizado para criar uma API RESTful com autenticação por token. Veremos autenticação por token e JWT em uma atividade futura quando falarmos de API e Serviços Web.

## Passo a Passo do que foi realizado no projeto

### Cadastro de Usuário

- Vamos criar a `view`, a rota em `urls.py` e o template na pasta `templates/registration` para o cadastro de usuário e também para login baseado nos protótipos `prototipo/registration_form.html` e `prototipo/registration_login.html`
- No arquivo `views.py` criara view `register` e a view `dashboard_main` que será a view que o usuário vai ser redirecionado após a criação da conta e após logar

```python
# No inicio do arquivo realizar as importacoes necessarias
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Padaria, Cesta


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_verification = request.POST.get('password_verification')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        context = {
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
        }

        if password != password_verification:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'registration/form.html', context)

        if User.objects.filter(username=email).exists():
            messages.error(request, 'Este email já está registrado.')
            return render(request, 'registration/form.html', context)

        user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
        login(request, user)
        return redirect('dashboard_main')

    return render(request, 'registration/form.html')


@login_required
def dashboard_main(request):
    return render(request, 'dashboard/main.html')
```

- Importar o decorator `login_required` e a função `login` do Django para fazer o login do usuário após o cadastro assim como o model `User` e `messages` para exibir mensagens de erro
- O decorator `login_required` é utilizado para verificar se o usuário está logado. Caso o usuário não esteja logado, ele será redirecionado para a página de login. Esse decorator pode ser utilizado em qualquer view que precise de autenticação.
- A função `login` é utilizada para fazer o login do usuário após o cadastro. Essa função recebe o request e o usuário como parâmetros e faz o login do usuário na sessão. Django verifica se o usuário permanece logado utilizando o cookie de sessão. O cookie de sessão é criado quando o usuário faz o login e é utilizado para identificar o usuário em requisições futuras. O Django possui suporte nativo para autenticação de usuários e gerenciamento de sessões.
- O método `create_user` é utilizado para criar um novo usuário no banco de dados. Esse método recebe o nome de usuário, e-mail, senha, nome e sobrenome como parâmetros e cria um novo usuário no banco de dados. O Django possui suporte nativo para criação de usuários e gerenciamento de senhas. O método `create_user` também gera um hash da senha do usuário para garantir a segurança da senha.
- A lib `messages` é utilizada para exibir mensagens de erro ou sucesso para o usuário. Essa lib permite exibir mensagens de forma simples e eficiente. O Django possui suporte nativo para exibição de mensagens e gerenciamento de sessões. As mensagens são armazenadas na sessão do usuário e podem ser exibidas em qualquer template.

### Criar Rota para Cadastro de Usuário

- Em `urls.py` criar a rota para a view `register` e a view `dashboard_main` além de incluir as outras rotas de autenticação do Django presentes em `django.contrib.auth.urls`

```python
urlpatterns = [
    ...
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/register/', padarias_views.register, name='register'),
    path('dashboard/', padarias_views.dashboard_main, name='dashboard_main'),
    ...
]
```

### Template de Cadastro de Usuário

- Utilizando o protótipo `prototipo/registration_form.html` criar o template `templates/registration/form.html` para o cadastro de usuário. Esse template deve conter um formulário com os campos de e-mail, senha, confirmação de senha, nome e sobrenome. O formulário deve enviar os dados para a view `register`.
- O template de cadastro de usuário exibe um formulário com os campos de e-mail, senha, confirmação de senha, nome e sobrenome. O formulário envia os dados para a view `register` que irá criar o usuário no banco de dados. O template também exibe um botão para redirecionar o usuário para a página de login caso ele já tenha uma conta.
- Criar o template do dashboard em `templates/dashboard/main.html` que será exibido após o login do usuário. Esse template deve exibir uma mensagem de boas-vindas e o nome do usuário logado


### Configuração de Login e Logout

- Vamos configurar a página de login já que a lógica de autenticação já está pronta e sua url ja foi importada anteriormente
- Configurações gerais de autenticação e autorização estão no arquivo `settings.py` do projeto.
- Principais configurações:
- `LOGIN_REDIRECT_URL`: URL de redirecionamento após o login. O Django possui uma URL de redirecionamento padrão, mas podemos criar uma URL de redirecionamento personalizada.
- `LOGOUT_REDIRECT_URL`: URL de redirecionamento após o logout. O Django possui uma URL de redirecionamento padrão, mas podemos criar uma URL de redirecionamento personalizada.

```python
# login redirect
LOGIN_REDIRECT_URL = 'dashboard_main'
LOGOUT_REDIRECT_URL = 'home'
```

- Criar a página de login baseada no protótipo `prototipo/registration_login.html` em `templates/registration/login.html`
- Vamos alterar o header para exibir o nome do usuário logado caso ele esteja se nào vamos enviá-lo a página de login
- No arquivo `components/header.html` vamos alterar para incluir esse link


### Área Logada e Logout

- Django já possui uma `view` com a lógica de logout assim como uma rota pré-configurada. Essa rota é chamada `logout` e já está importada no arquivo `urls.py` do projeto
- Vamos criar uma area logada, para isso precisamos de uma nova view `dashboard` e um template em `templates/dashboard/main.html` para exibir uma mensagem de boas-vindas e o nome do usuário logado. Essa view deve ser protegida com o decorator `login_required` para garantir que apenas usuários logados possam acessar essa área.
- O template lista as informações do usuário logado utilizando a variável `request.user` que é disponibilizada pelo Django em todas as views e templates. Essa variável contém as informações do usuário logado, como nome, email, etc. O template também exibe um link para logout que redireciona o usuário para a página de logout do Django.
- Nesta area tem opção de logout, para isso basta clicar no link de logout que redireciona o usuário para a página de logout do Django. O Django possui uma view pré-configurada para logout que é chamada `LogoutView` e já está importada no arquivo `urls.py` do projeto. Essa view é responsável por fazer o logout do usuário e redirecioná-lo para a página de logout definida na configuração `LOGOUT_REDIRECT_URL` do arquivo `settings.py` do projeto.
- Vamos incluir um botão de logout nessa tela e vamos alterar o header para exibir o nome do usuário logado caso ele esteja se não vamos enviá-lo a página de login. Para isso, vamos alterar o template `components/header.html` para incluir um link para a página de login caso o usuário não esteja logado e um link para a página de logout caso o usuário esteja logado. 
