# A18 - NextJS - Framework React

## Atividade

- Utilize a estrutura do projeto NextJS que esta na pasta A18 e crie uma aplicação web
- Precisa ter pelo menos 2 páginas
- Defina um layout novo para a sua aplicação

## Principais conceitos

### O que é NextJS?

O **Next.js** é um framework de código aberto criado pela Vercel, construído sobre a biblioteca React. Enquanto o React foca na interface (UI), o Next.js provê a infraestrutura necessária para aplicações prontas para produção, oferecendo ferramentas de roteamento, renderização híbrida (SSR/SSG), otimização de imagens e suporte a API Routes "out of the box".

### Vantagens do NextJS

* **SEO Facilitado:** Ao contrário do React puro (SPA), o Next permite que o conteúdo seja renderizado no servidor, tornando-o visível para crawlers de busca.
* **Performance:** Possui otimização automática de fontes, imagens e scripts.
* **Zero Config:** Suporte nativo a TypeScript, ESLint e Tailwind CSS sem necessidade de configurar Webpack ou Babel manualmente.
* **Roteamento baseado em arquivos:** Não é necessário instalar bibliotecas externas como o `react-router-dom`.

### Páginas e Rotas

O Next.js utiliza o sistema de **File-system Routing**. No diretório `app` (App Router):

* Cada pasta representa um segmento da URL.
* O arquivo `page.tsx` dentro de uma pasta torna aquela rota acessível.
* **Rotas Dinâmicas:** Pastas nomeadas com colchetes, como `[id]`, permitem capturar parâmetros variáveis da URL (ex: `/produto/123`).

### Componentes e Layouts

* **Layouts (`layout.tsx`):** São componentes que envolvem as páginas e preservam o estado durante a navegação (úteis para Navbars e Footers). Eles não são renderizados novamente quando o usuário navega entre rotas filhas.
* **Server vs Client Components:** Por padrão, no App Router, todos os componentes são **Server Components**. Para usar hooks como `useState` ou `useEffect`, deve-se adicionar a diretiva `"use client"` no topo do arquivo.

### Autenticação no CSR com API Externa

Para autenticar uma SPA/CSR com um backend externo (Django, Node, etc.):

1. **Login:** O cliente envia as credenciais para a API e recebe um token (geralmente JWT).
2. **Armazenamento:** O token deve ser armazenado preferencialmente em **Cookies (httpOnly)** por segurança, ou em `localStorage` (com ressalvas).
3. **Interceptor:** Configura-se um interceptor (no Axios ou Fetch) para anexar o token no Header `Authorization: Bearer <token>` em cada requisição subsequente.
