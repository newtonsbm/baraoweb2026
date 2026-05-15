# A17 - Aplicacao Frontend com React

## Atividades

- Crie uma aplicação frontend usando React
- Utilize vite com React
- Pode ser uma SPA bem simples como:
  - Um todo list
  - Um jogador de dados
  - Um lista de produtos ou receitas ou séries
  etc
- O importante é usar os conceitos de React: JSX, componentes, props, state, eventos 



## Conceitos principais de desenvolvimento frontend com React

### O que é React?

React é uma **biblioteca JavaScript** criada pelo Facebook para construir interfaces de usuário interativas. Ele permite criar componentes reutilizáveis que gerenciam seu próprio estado e se atualizam automaticamente quando os dados mudam.

**Principais características:**
- ✅ **Baseado em componentes** - interfaces são compostas por componentes independentes
- ✅ **Reatividade** - atualiza automaticamente quando o estado muda
- ✅ **Virtual DOM** - otimiza as atualizações da página
- ✅ **Unidirecional** - fluxo de dados de cima para baixo (parent → children)

### Frontend vs Backend

Na A16, criamos uma **API (Backend)** que:
- Processa requisições
- Acessa banco de dados
- Retorna dados em JSON

Agora vamos criar o **Frontend** que:
- Faz requisições para a API
- Exibe dados para o usuário
- Permite interação (formulários, cliques, etc)

**Diferença:**
```
Backend (API)                Frontend (React)
├── POST /auth/register/    → Formulário de registro
├── POST /auth/token/pair/  → Tela de login
├── GET /certas/            → Lista de cestas
└── GET /perfil/            → Perfil do usuário
```

---

## Conceitos Fundamentais

### JSX (JavaScript XML)

**O que é JSX?**

JSX é uma sintaxe que permite escrever **HTML dentro do JavaScript**. Parece HTML, mas na verdade é JavaScript!

**Exemplo básico:**
```jsx
// JSX
const elemento = <h1>Olá, mundo!</h1>;

// Compilado para JavaScript puro
const elemento = React.createElement('h1', null, 'Olá, mundo!');
```

**JSX com expressões JavaScript:**
```jsx
const nome = "João";
const idade = 25;

// Usar variáveis com {}
const saudacao = <p>Meu nome é {nome} e tenho {idade} anos</p>;

// Operações matemáticas
const resultado = <p>2 + 2 = {2 + 2}</p>;

// Criar lista
const nomes = ["Ana", "Bruno", "Carlos"];
const lista = (
  <ul>
    {nomes.map((nome) => <li key={nome}>{nome}</li>)}
  </ul>
);
```

**Regras do JSX:**
- Um elemento tem que ter um elemento pai
- Use `className` ao invés de `class`
- Use `htmlFor` ao invés de `for`
- Atributos em camelCase: `onClick`, `onChange`, `onSubmit`

---

### Componentes

**O que é um componente?**

Um componente é uma **função em JavaScript que retorna JSX**. É um bloco reutilizável de código.

**Componente simples:**
```jsx
// Componente funcional
function Saudacao() {
  return <h1>Olá, bem-vindo ao Cafe com Pao!</h1>;
}

// Usando o componente
export default function App() {
  return <Saudacao />;
}
```

**Componente com múltiplos elementos:**
```jsx
function CartaoRecipiente() {
  return (
    <div className="card">
      <h2>Receita Deliciosa</h2>
      <p>Uma receita incrivél de frango assado</p>
      <button>Ver Receita</button>
    </div>
  );
}
```

**Reutilizando componentes:**
```jsx
function App() {
  return (
    <div>
      <CartaoRecipiente />
      <CartaoRecipiente />
      <CartaoRecipiente />
    </div>
  );
}
```

---

### Props (Propriedades)

**O que são props?**

Props são **argumentos** passados para um componente. Permitem personalizar componentes reutilizáveis.

**Sintaxe:**
```jsx
// Definir componente que recebe props
function CartaoProduto(props) {
  return (
    <div>
      <h3>{props.nome}</h3>
      <p>R$ {props.preco}</p>
      <p>{props.descricao}</p>
    </div>
  );
}

// Passar props ao usar componente
<CartaoProduto 
  nome="Bolo de Chocolate" 
  preco="25.00" 
  descricao="Bolo caseiro feito com chocolate belga"
/>
```

**Desestruturação (melhor prática):**
```jsx
// Ao invés de props.nome, props.preco...
function CartaoProduto({ nome, preco, descricao }) {
  return (
    <div>
      <h3>{nome}</h3>
      <p>R$ {preco}</p>
      <p>{descricao}</p>
    </div>
  );
}
```

**Props com valores padrão:**
```jsx
function Botao({ texto = "Clique aqui", cor = "azul" }) {
  return <button style={{backgroundColor: cor}}>{texto}</button>;
}

// Usar com valores padrão
<Botao /> // "Clique aqui" em azul

// Sobrescrever valores
<Botao texto="Comprar" cor="verde" />
```

---

### Estado (State)

**O que é estado?**

Estado é um **objeto que armazena dados que podem mudar** durante a execução. Quando o estado muda, o componente é re-renderizado automaticamente.

**Usando o hook `useState`:**
```jsx
import { useState } from 'react';

function Contador() {
  // const [variavel, setVariavel] = useState(valorInicial)
  const [contador, setContador] = useState(0);

  return (
    <div>
      <p>Contador: {contador}</p>
      <button onClick={() => setContador(contador + 1)}>
        Incrementar
      </button>
    </div>
  );
}
```

**Exemplo com múltiplos estados:**
```jsx
function Formulario() {
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [mensagem, setMensagem] = useState("");

  return (
    <form>
      <input 
        value={nome} 
        onChange={(e) => setNome(e.target.value)}
        placeholder="Digite seu nome"
      />
      <input 
        value={email} 
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Digite seu email"
      />
      <p>Nome: {nome}, Email: {email}</p>
    </form>
  );
}
```

**Estado com dados complexos (arrays/objetos):**
```jsx
function ListaDeTarefas() {
  const [tarefas, setTarefas] = useState([
    { id: 1, titulo: "Estudar React" },
    { id: 2, titulo: "Fazer exercicios" }
  ]);

  const adicionarTarefa = (titulo) => {
    setTarefas([
      ...tarefas,  // Espalhar tarefas existentes
      { id: Date.now(), titulo: titulo }
    ]);
  };

  return (
    <ul>
      {tarefas.map((tarefa) => (
        <li key={tarefa.id}>{tarefa.titulo}</li>
      ))}
    </ul>
  );
}
```

---

### Eventos

**O que são eventos?**

Eventos são **ações do usuário** (clique, digitação, etc). Em React, tratamos eventos com funções callback.

**Eventos comuns:**

```jsx
function ComponenteComEventos() {
  return (
    <div>
      {/* onClick - quando usuário clica */}
      <button onClick={() => alert("Botão clicado!")}>
        Clique em mim
      </button>

      {/* onChange - quando input muda */}
      <input 
        onChange={(e) => console.log(e.target.value)}
        placeholder="Digite algo"
      />

      {/* onSubmit - quando formulário é enviado */}
      <form onSubmit={(e) => {
        e.preventDefault(); // Impedir recarga da página
        console.log("Formulário enviado");
      }}>
        <button type="submit">Enviar</button>
      </form>

      {/* onMouseEnter / onMouseLeave */}
      <div 
        onMouseEnter={() => console.log("Mouse entrou")}
        onMouseLeave={() => console.log("Mouse saiu")}
      >
        Passe o mouse aqui
      </div>

      {/* onFocus / onBlur */}
      <input 
        onFocus={() => console.log("Input focado")}
        onBlur={() => console.log("Input desfocado")}
      />
    </div>
  );
}
```

**Exemplo prático - Contador com eventos:**
```jsx
function Contador() {
  const [numero, setNumero] = useState(0);

  const incrementar = () => setNumero(numero + 1);
  const decrementar = () => setNumero(numero - 1);
  const resetar = () => setNumero(0);

  return (
    <div>
      <p>Numero: {numero}</p>
      <button onClick={incrementar}>+</button>
      <button onClick={decrementar}>-</button>
      <button onClick={resetar}>Resetar</button>
    </div>
  );
}
```

---

### Hooks

**O que são hooks?**

Hooks são **funções especiais que permitem "conectar" ao React**. Eles deixam você usar estado e outras funcionalidades em componentes funcionais.

**Hooks mais comuns:**

**useState** - Gerenciar estado local
```jsx
const [valor, setValor] = useState(inicial);
```

**useEffect** - Executar efeitos colaterais (buscar dados, etc)
```jsx
import { useEffect } from 'react';

function ComponenteComAPI() {
  const [dados, setDados] = useState([]);

  // Executar quando componente monta
  useEffect(() => {
    fetch('/api/cestas')
      .then(res => res.json())
      .then(data => setDados(data));
  }, []); // [] = executar uma unica vez

  return <div>{dados.length} cestas carregadas</div>;
}
```

---

## Fluxo de Dados em React

```
Props (de cima para baixo)
    ↓
Componente Pai
    ↓
    ├─→ Componente Filho 1
    │    └─ Recebe props
    │
    └─→ Componente Filho 2
         └─ Recebe props

Estado (local do componente)
    ↓
useState (gerencia estado)
    ↓
Renderizar componente
    ↓
Usuário interage (evento)
    ↓
Atualizar estado
    ↓
Re-renderizar automaticamente
```

---

## Resumo dos Conceitos

| Conceito | O que é | Exemplo |
|----------|---------|---------|
| **JSX** | Sintaxe que mistura HTML com JavaScript | `<h1>{nome}</h1>` |
| **Componente** | Função que retorna JSX | `function Botao() {...}` |
| **Props** | Argumentos passados para componentes | `<Botao texto="Clique" />` |
| **State** | Dados que mudam durante execução | `const [contador, setContador] = useState(0)` |
| **Eventos** | Ações do usuário | `<button onClick={...}>` |
| **Hooks** | Funções que conectam ao React | `useState`, `useEffect` |
| **Renderização** | Exibir componentes na tela | React atualiza automaticamente |

---

## Rodando uma Aplicação React

### Criar novo projeto
```bash
npm create vite@latest meu-frontend -- --template react
cd meu-frontend
npm install
npm run dev
```

### Estrutura básica
```
src/
├── App.jsx           # Componente principal
├── App.css
├── main.jsx          # Ponto de entrada
└── components/       # Seus componentes
    ├── Botao.jsx
    ├── Cartao.jsx
    └── ...
```

### Exemplo de App.jsx
```jsx
import { useState } from 'react';
import './App.css';

function App() {
  const [contador, setContador] = useState(0);

  return (
    <div>
      <h1>Bem-vindo ao Cafe com Pao</h1>
      <p>Contador: {contador}</p>
      <button onClick={() => setContador(contador + 1)}>
        Incrementar
      </button>
    </div>
  );
}

export default App;
```
