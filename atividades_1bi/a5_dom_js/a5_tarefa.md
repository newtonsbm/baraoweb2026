# A5 - Javascript DOM e Eventos

## Atividades

- Vamos criar um jogo simples ou um app simples utilizando javascript para realizar manipulação do DOM
- O importante é treinar a manipulação do DOM e eventos em javascript
- Veja os exemplos disponíveis na pasta "exemplos"
- Utilize outras libs para facilitar como Alpine.JS
- Para o CSS podem utilizar algum framework como Tailwind ou Bootstrap ou escrever o CSS do zero


## Resumo dos Conceitos Importantes

Javascript é uma linguagem de programação de alto nível, interpretada, orientada a objetos e multi-paradigma. Ela é a linguagem padrão executada nos navegadores web e permite a criação de páginas web interativas.
DOM (Document Object Model) é uma interface de programação que representa a estrutura de um documento HTML como uma árvore de objetos.
A manipulação do DOM é feita por meio de métodos e propriedades que permitem a criação, remoção, alteração e leitura de elementos HTML.
Eventos são ações que ocorrem em um documento HTML, como cliques, teclas pressionadas, movimentos do mouse, etc.
Os eventos são tratados por meio de event handlers, que são funções que são executadas quando um evento ocorre.

## Introdução ao Javascript

- ECMA Script é a especificação padrão da linguagem Javascript
- Javascript pode ser executada no navegador ou no servidor (Node.js)
- Vamos focar em Javascript no navegador, ou seja, no client-side principalmente para manipulação do DOM e eventos
- Podemos incluir o Javascript de três formas: inline, interno e externo
- Inline é quando o código Javascript é incluído diretamente no HTML:

```html
    <button onclick="alert('Hello World!')">Click me</button>
```

- Interno é quando o código Javascript é incluído dentro de uma tag `<script>` no HTML:

```html
    <script>
        alert('Hello World!');
    </script>
```

- Externo é quando o código Javascript é incluído em um arquivo separado e referenciado no HTML:

```html
    <script src="script.js"></script>
```
```javascript
    alert('Hello World!');
```

## Manipulando o DOM

- Para manipular o DOM, utilizamos o objeto `document` que representa o documento HTML
- Podemos acessar elementos HTML por meio de métodos como `getElementById`, `getElementsByClassName`, `getElementsByTagName`, `querySelector`, `querySelectorAll`
- Exemplo:

```html
    <div id="div1">Hello World!</div>
    <div class="div2">Div com Class!</div>
    <div class="container">
        <p>Parágrafo 1</p>
        <p>Parágrafo 2</p>
    </div>
    <script>
        const div1 = document.getElementById('div1');
        const div2 = document.getElementsByClassName('div2');
        const ps_container = document.querySelectorAll('.container p');
    </script>
```	

- Podemos alterar o conteúdo, estilo e atributos dos elementos HTML por meio de propriedades como `innerHTML`, `innerText`, `style`, `setAttribute`, etc
- Exemplo:

```html
    <div id="div1">Hello World!</div>
    <script>
        const div1 = document.getElementById('div1');
        div1.innerHTML = 'Olá Mundo!';
        div1.style.color = 'red';
        div1.setAttribute('class', 'nova-classe');
    </script>
```

- Podemos criar, adicionar e remover elementos HTML por meio de métodos como `createElement`, `appendChild`, `removeChild`, etc
- Exemplo:

```html
    <div id="container"></div>
    <script>
        const container = document.getElementById('container');
        const p = document.createElement('p');
        p.innerText = 'Novo Parágrafo';
        container.appendChild(p);
    </script>
```

## Eventos

- Eventos são ações que ocorrem em um documento HTML, como cliques, teclas pressionadas, movimentos do mouse, etc
- Podemos tratar eventos por meio de event handlers, que são funções que são executadas quando um evento ocorre
- Exemplo:

```html
    <button id="btn">Click me</button>
    <script>
        const btn = document.getElementById('btn');
        btn.addEventListener('click', function() {
            alert('Hello World!');
        });
    </script>
```

## Gerenciadores de Pacote e Bundler

- Gerenciadores de pacote ajudam a instalar, atualizar e remover dependencias do projeto
- O npm vem com o Node.js e e o gerenciador mais comum
- O Yarn e uma alternativa ao npm, com foco em velocidade, cache e comandos consistentes
- Um bundler organiza o codigo, empacota arquivos e prepara o projeto para desenvolvimento e producao
- O Vite e um bundler moderno, rapido para desenvolvimento e com build otimizado

### Exemplo com npm

```bash
    npm create vite@latest meu-site
    cd meu-site
    npm install
    npm run dev
```

### Exemplo com Yarn

```bash
    yarn create vite meu-site
    cd meu-site
    yarn
    yarn dev
```

## Instalacao no Windows: Node, Yarn e Vite (passo a passo)

### 1) Instalar o Node.js (inclui npm)

1. Acesse https://nodejs.org
2. Baixe a versao LTS (recomendada)
3. Execute o instalador e avance com as opcoes padrao
4. Abra o PowerShell e verifique:

```bash
    node -v
    npm -v
```

### 3) Usar o Vite

Com npm:

```bash
    npm create vite@latest meu-site
    cd meu-site
    npm install
    npm run dev
```


## Desafio Extra

- Crie um projeto Vite com Vanilla JS usando Yarn (ou npm se preferir)
- Configure o projeto com o site feito na atividade anterior (ou desenvolva um novo)
- Atencao: necessário apagar o index.html padrão e o main.js para criar os seus arquivos do zero, ou adaptar os arquivos padrões para o seu projeto
- Não se preocupe em usar o React ou outro framework, o Vite suporta projetos simples de HTML, CSS e JS
- Não utilize a criação de componentes via javascript, crie os elementos diretamente no HTML
- Rode o projeto localmente e verifique no navegador

Exemplo com npm:

```bash
    npm create vite@latest site-novo
    cd site-novo
    npm install
    npm run dev
```

## Desafios Opcionais
- Instale as dependencias do projeto (libs CSS ou JS) usando o npm ou Yarn
- Altere os arquivos de configuraçao do Vite necessários
- Build o seu projeto e verifique a pasta de distribuiçao (dist) para entender como o bundler organiza os arquivos para producao
- Configure o Github Pages para hospedar o seu projeto (opcional, mas recomendado para praticar deploy)

## Troubleshooting

- No Windows, dependendo da instalação do Node e da configuração do PATH pode ser necessário utilizar o `yarn` juntamente com `npm`
- Instale o `yarn`
- Pode ser viw `npm` ou baixando o instalador do `yarn` para windows no site oficial
- Crie o projeto vite com `npm` mas não rode o `npm install` ou `npm run dev`
- Entre na pasta do projeto criado e instale as dependencias usando o `yarn`:

```bash
    yarn
```
- Agora sim pode rodar o servidor tanto faz com yarn ou npm:

```bash
    npm run dev
    # ou
    yarn dev
```
