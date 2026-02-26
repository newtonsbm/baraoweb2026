# A3 - Tags Semânticas e Layout HTML

Vamos utilizar as tags estruturais semânticas do HTML e box model do CSS, assim como o Normal Flow e Flexbox Layout, para reproduzir diferentes tipos de layout.

- Cada um do grupo pode escolher um dos seguintes layouts para reproduzir (lembre de nomear os arquivos com nomes diferentes) ou criar outro próprio:
    - [Layouts de Exemplo](https://www.figma.com/design/Fzpxk9W4nwNlPKzARlRDxS/Web---Layouts?node-id=3106-6930&t=yNxN7zw411rUlxIU-1)
- Primeiro defina a estrutura do HTML utilizando tags semânticas como:
    - `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`
    - EVITE o uso de `div` e `span` 
- Depois, utilize o CSS para montar o layout
    - Construa o layout utilizando Flexbox (`display: flex` no elemento pai)
    - Para melhor controle do layout, utilize as seguintes propriedades CSS:
    - `width`, `height`, `min-width`, `min-height`, `max-width`, `max-height`: para definir as dimensões dos elementos
    - é possível utilizar porcentagem para definir tamanhos relativos
    - `margin`, `padding`, `border`: para definir o espaçamento entre os elementos
- Não é necessário se preocupar com o conteúdo, mas sim com a estrutura e layout, mas se preferir aproveite e crie um conteúdo fictício para o layout
- Realizar o add, commit e push das alterações

## Dicas
 
- Centralizando elementos horizontalmente:
    - Utilize `margin: 0 auto` para centralizar elementos com `width` definido
- Centralizando elementos verticalmente:
    - `align-content: center` em um elemento com `display: block` e `height` definido 
- Dicas de Flexbox:
    - `display: flex` no elemento pai para ativar o Flexbox
    - `flex-direction: row` para organizar os elementos em linha (padrão)
    - `flex-direction: column` para organizar os elementos em coluna
    - `justify-content: center` para centralizar os elementos horizontalmente
    - `align-items: center` para centralizar os elementos verticalmente
    - `gap: 20px` para adicionar um espaçamento de 20px entre os elementos filhos

## Desafio

- Torne o layout responsivo utilizando media queries para ao menos 2 tamanhos de tela: desktop e mobile
- Desafio 2:
    - Crie um componente de 1 card com imagem, título, descrição e botão de ação ou texto de link

## Extra
- Veja o material sobre Grid Layout: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Basic_concepts_of_grid_layout 
- Tente implementar o mesmo layout utilizando Grid Layout

