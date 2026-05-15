# 🎓 React + DaisyUI - SPA Didática

Uma aplicação React super simples para ensinar os conceitos fundamentais de React aos alunos.

## 📦 Instalação

```bash
# Instalar dependências
npm install

# Ou com yarn
yarn install
```

## 🚀 Executar

```bash
# Development server
npm run dev

# Ou com yarn
yarn dev
```

A aplicação abrirá em `http://localhost:5173`

## 📚 Conceitos Ensinados

### 1️⃣ **useState - Contador**
- Como criar e gerenciar estado local
- Atualizar estado com `setContador()`
- Re-renderização automática

```jsx
const [contador, setContador] = useState(0)
<button onClick={() => setContador(contador + 1)}>+</button>
```

### 2️⃣ **Eventos - Formulário**
- Manipular eventos de input (`onChange`)
- Atualizar estado com dados de formulário
- Renderizar valores em tempo real

```jsx
<input 
  value={nome}
  onChange={(e) => setNome(e.target.value)}
/>
```

### 3️⃣ **map() - Lista de Tarefas**
- Renderizar listas com `.map()`
- Usar `key` prop para eficiência
- Adicionar/remover itens da lista

```jsx
{tarefas.map((tarefa) => (
  <li key={tarefa.id}>{tarefa.titulo}</li>
))}
```

### 4️⃣ **Renderização Condicional**
- Mostrar/ocultar elementos baseado em estado
- Usar operador ternário (`? :`)
- Múltiplas condições

```jsx
{logado ? (
  <p>Bem-vindo!</p>
) : (
  <p>Faça login</p>
)}
```

### 5️⃣ **Props - Reutilização**
- Passar dados de pai para filho
- Desestruturação de props
- Componentes reutilizáveis

```jsx
<CartaoProduto nome="Café" preco="5.00" emoji="☕" />

function CartaoProduto({ nome, preco, emoji }) {
  // ...
}
```

### 6️⃣ **Componentes**
- Estrutura e organização
- Um arquivo = um componente
- Props e State isolados

## 🎨 Tecnologias

- **React 19** - Biblioteca UI
- **Vite** - Build tool rápido
- **Tailwind CSS** - Estilos utilitários
- **DaisyUI** - Componentes pré-estilizados

## 📁 Estrutura de Pastas

```
src/
├── App.jsx      # Componente principal
├── App.css      # Estilos
├── main.jsx     # Ponto de entrada
├── index.css    # Estilos globais
└── assets/      # Imagens, fontes, etc
```

## 💡 Como Usar em Aula

### Apresentação Progressiva

1. **Comece com setState**: Mostre o contador
   - "Veja como o estado muda e o componente re-renderiza"

2. **Introduza eventos**: Mostre o formulário
   - "Cada keypress atualiza o estado em tempo real"

3. **Mostre map()**: Mostre a lista de tarefas
   - "Renderizar listas dinamicamente com map()"

4. **Condicional**: Mostre o exemplo de login
   - "Renderizar diferentes coisas baseado em estado"

5. **Props**: Mostre os cartões de produto
   - "Reutilizar componentes com dados diferentes"

### Desafios para os Alunos

**Fácil:**
- Adicionar botão para decrementar no contador
- Adicionar tema claro/escuro com DaisyUI

**Médio:**
- Adicionar marcar tarefas como completas
- Filtrar tarefas por status

**Difícil:**
- Salvar tarefas em localStorage
- Conectar com API backend (cafecompao)
- Criar componente de autenticação

## 🔗 Conectar com Backend

Para conectar com a API do Cafe com Pao:

```jsx
useEffect(() => {
  fetch('http://localhost:8000/api/cestas/')
    .then(res => res.json())
    .then(data => setCestas(data))
}, [])
```

## 📝 Notas para Alunos

- **Hot Module Replacement (HMR)**: Salve o arquivo e a página atualiza automaticamente
- **DevTools**: Use React DevTools para debugar componentes
- **Props vs State**: Props são imutáveis, State é mutável
- **Key prop**: Sempre use ID único em listas, não índice

## 🎯 Próximos Passos

1. Adicione mais componentes
2. Divida App.jsx em múltiplos arquivos
3. Use `useEffect` para buscar dados
4. Implemente autenticação JWT
5. Conecte com backend Django

---

**Feito com ❤️ para ensinar React**
