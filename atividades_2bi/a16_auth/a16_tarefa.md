# A16 - Seguranca e Autenticacao em APIs

## Atividade
Escolha entre essas duas opções. 

1 - Utilize o projeto Café com Pão que esta na pasta A16
- Implemente uma rota autenticada para alterar o perfil do usuário
- Para isso necessário criar um schema novo para a atualização do perfil (ProfileUpdateSchema) e uma rota PATCH ou PUT que recebe esse schema e atualiza as informações do usuário autenticado.
- Os campos são: nome, telefone, cpf e data_nascimento

2 - Idéia própria, continuação da A15
- Continue a partir da atividade anterior (A15) caso vc tenha desenvolvido uma API própria e agora adicione autenticação usando JWT.
- Copie o código da A15 para a pasta A16 
- Instale a lib `django-ninja-jwt` e siga a documentação para configurar as rotas de login, refresh e verify. Para isso uso `uv add django-ninja-jwt` e depois `uv run manage.py migrate` para criar as tabelas necessárias.
- Implemente a rota de cadastro de usuário 

## Desafio extra (opcional)
- Implementar expiracao do token e refresh.
- Adicionar rotas de logout (invalidacao de token).

## Objetivo
Compreender os principais conceitos de autenticacao em APIs e servicos web e aplicar esses conceitos no projeto Cafe com Pao, dando continuidade a A15.

## Conceitos Principais (Resumo Didatico)
Autenticacao em APIs existe para garantir que apenas clientes autorizados consigam acessar recursos sensiveis. A seguir, os conceitos mais usados em servicos web:

### 1) API Key
- Um token simples enviado pelo cliente (query, header ou body).
- Vantagem: facil de usar e implementar.
- Desvantagem: menos segura se vazada, sem expiracao por padrao.
- Uso tipico: integracoes simples e APIs publicas com limite de uso.

### 2) Basic Auth
- Usuario e senha codificados em Base64 no header `Authorization`.
- Vantagem: simples e padrao.
- Desvantagem: exige HTTPS, nao possui expiração nem escopo.
- Uso tipico: ambientes internos ou prototipos.

### 3) Session / Cookie Auth
- O servidor cria uma sessao e retorna um cookie para o cliente.
- Vantagem: comum em aplicacoes web tradicionais.
- Desvantagem: menos indicado para APIs consumidas por apps ou multiplataforma.
- Uso tipico: web apps com login via browser.

### 4) Token Bearer (JWT)
- O servidor emite um token (JSON Web Token) com informacoes do usuario.
- O cliente envia o token no header `Authorization: Bearer <token>`.
- Vantagem: escalavel, funciona bem em apps mobile/web.
- Desvantagem: precisa de cuidado com expiracao e renovacao.
- Uso tipico: APIs REST modernas.

### 5) OAuth2 (Delegacao de acesso)
- Permite login via Google/GitHub e compartilhamento seguro de acesso.
- Vantagem: padrao de mercado, seguro e escalavel.
- Desvantagem: fluxo mais complexo.
- Uso tipico: login social e integracoes entre plataformas.

## Boas Praticas de Seguranca em APIs
- Sempre usar HTTPS (nunca trafegar credenciais em HTTP).
- Proteger rotas sensiveis com autenticacao.
- Usar tokens com expiracao e renovacao.
- Implementar rate limiting (limitar tentativas e requisicoes).
- Nunca expor dados sensiveis no corpo da resposta.
- Validar dados de entrada (evitar SQL Injection e outros ataques).

## Passo a passo do que foi alterado no projeto Cafe com Pao

Na A15, criamos uma API REST para o projeto Cafe com Pao (cestas, contato, perfil). Na A16, vamos adicionar uma camada de autenticacao para proteger rotas de perfil e permitir acesso seguro via token.
Instalamos a biblioteca `django-ninja-jwt` para facilitar a implementacao de JWT. Criamos rotas para login (obter token) e protegemos a rota de perfil para exigir um token valido. Agora, apenas usuarios autenticados podem acessar suas informacoes de perfil, garantindo mais seguranca para os dados dos usuarios.

Com isso temos, 3 rotas essenciais:

- `POST /api/auth/token/` - Para obter um token JWT usando email e senha.
- `POST /api/auth/token/refresh/` - Para renovar o access token usando um refresh token valido.
- `POST /api/auth/token/verify/` - Para verificar se um token JWT é valido.

Além disso, temos a rota de cadastro de usuario (`POST /api/auth/register/`) para criar novos usuarios e a rota de perfil (`GET /api/perfil/`) protegida por JWT.

