## A2 - Introdução ao HTML e CSS

### Resumo dos Conceitos Importantes

- Sistemas web são, na maioria das vezes, compostos por um cliente e servidor que se comunicam usando o protocolo HTTP e por meio de tecnologias Web como HTML, CSS e JavaScript.
- O servidor web nada mais é que um processo de software que aceita solicitações via protocolo HTTP (a partir de uma determinada porta) e serve arquivos em resposta a essas solicitações. 
- O cliente web geralmente é um navegador que faz solicitações HTTP para um servidor web e exibe o conteúdo recebido.
- Esse conteúdo são páginas HTML, mas também podem ser imagens, scripts, arquivos css, fontes, dados serializados em JSON, entre outros.
- HTML é uma linguagem de marcação que define a estrutura de uma página web.
- CSS é uma linguagem de estilo que define a aparência de uma página web.
- JavaScript é uma linguagem de programação que permite a criação de páginas web interativas por meio de APIs do navegador.

### HTML - HyperText Markup Language
- HTML é uma linguagem de marcação, assim como o Markdown
- Essa marcação é feita por meio de tags, que são elementos que definem a estrutura e o conteúdo de uma página web
- As tags são compostas por um nome e podem ter atributos
- As tags podem ser aninhadas, ou seja, uma dentro da outra, formando uma árvore de elementos HTML.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Minha Página</title>
</head>
<body>
    <h1>Curso de Programação Web</h1>
    <p>Bem vindo querida ou querido 
        <a href="https://pt.wikipedia.org/wiki/Jedi#A_estrutura_da_Ordem_Jedi">
            Padawan!
        </a>
    </p>
</body>
</html>
```
#### Marcação Textual e de Conteúdo
- Uma das principais funções do HTML é marcar o texto, ou seja, definir o tipo de conteúdo que está sendo exibido
- A seguir as principais tags de marcação de texto
    - `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`: títulos
    - `<p>`: parágrafos
    - `<a>`: hiperlinks
    - `<ul>`, `<ol>`: listas não ordenadas e ordenadas
    - `<li>`: itens de lista
    - `<img>`: imagens

### CSS - Cascading Style Sheets
- CSS é uma linguagem de estilo que define a aparência de uma página web
- O CSS é composto por regras de estilo que são aplicadas a elementos HTML
- As regras CSS são compostas por um seletor e um bloco de declarações
- As declarações são compostas por uma propriedade e um valor
- As propriedades definem *o que* será estilizado e os valores definem *como* será estilizado

```css
h1 {
    color: blue;
    font-size: 2rem;
    font-weight: bold;
    font-family: Arial, sans-serif;
}
```

#### Estilizando Elementos Textuais

- As principais propriedades de estilo de texto são:
    - `color`: cor do texto
    - `font-size`: tamanho da fonte
    - `font-weight`: peso da fonte
    - `font-family`: família da fonte
    - `text-align`: alinhamento do texto
    - `text-decoration`: decoração do texto
    - `text-transform`: transformação do texto
    - `line-height`: altura da linha
    - `letter-spacing`: espaçamento entre letras
    - `word-spacing`: espaçamento entre palavras

#### Estilizando Imagens

- As principais propriedades de estilo de imagem são:
    - `width`: largura da imagem
    - `height`: altura da imagem
    - `max-width`: largura máxima da imagem
    - `max-height`: altura máxima da imagem
- Na próxima aula veremos mais propriedades de estilo e como posicionar elementos na página assim como imagens a partir do box model e do normal flow no CSS


### Atividades

### Parte 1

- Instale a extensão `Live Server` no Visual Studio Code ou utilize algum outro servidor local para visualizar a página (ex: `http-server`, `python -m http.server`, etc)
- Em grupo pense em um tema para o site estático de vocês
- Vocês, como grupo, podem definir um tema para as páginas como `séries`, `jogos`, `receitas`, `animes`, `locais`, etc. 
- Cada aluno deve ser responsável por desenvolver uma página HTML simples
- NÃO DEVEM se preocupar com Layout nesse momento (posicionamento dos elementos) apenas estruturação de texto
- A página deve conter no mínimo 3 elementos HTML diferentes como títulos (`h1`, `h2`, `h3`), parágrafos (`p`), listas (`ul`, `ol`), imagens (`img`), links (`a`), etc.
- Incluir css na tag `<style>` no próprio arquivo HTML ou em arquivo a parte
- Não se preocupe com Javascript
- Estilize os elementos textuais da forma como desejar
- Pense na estrutura dos arquivos e pastas
- Caso utilizem imagens, crie uma pasta a parte nomeada como, por exemplo, `img` (ou `images`) e coloque as imagens lá
- Crie um arquivo `index.html` e links para as páginas individuais realizadas 
- Não é necessáro se preocupar com o layout (posicionamento, margem, preenchimento, etc), mas sim com a estruturação do conteúdo e estilo desses
- Realizar o add, commit e push para subir para o repositorio no github

### Opcional Recomendado

- Cada aluno deve criar uma branch com seu nome `git checkout -b seunome` 
- Abrir um **Pull Request** para a branch `main` marcando o seu outro colega de grupo como revisor
- Faça `git fetch --all` e observe o que mudou

### Desafio

- Procure outros elementos textuas e de dados do HTML e inclua na página
- Veja, por exemplo, os elementos: `summary`, `dd`, `blockquote`, `cite`, `abbr`, `code`, `kbd`, `sub`, `sup`, `small`, `strong`, `em`, `time`, `address`, `pre`, `hr`, `br`, `wbr`, `meter`, `progress`

### Parte 2
- Hospede a sua página em algum serviço gratuito de hospedagem 
- GitHub Pages, Cloudflare Pages são algumas opções
- Configure uma ferramenta para expor o servidor web local como o `localtunnel`
- Cole a url da página hospedada no Google Docs de Atividade disponível no Portal

