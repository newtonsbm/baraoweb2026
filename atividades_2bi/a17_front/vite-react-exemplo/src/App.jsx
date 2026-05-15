import {
  Card,
  ContadorExemplo,
  FormularioExemplo,
  CondicionalExemplo,
  ListaExemplo,
  CartaoProduto
} from './components'

export default function App() {
  return (
    <div className="min-h-screen bg-base-200 py-6 px-4">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <header className="text-center mb-8">
          <h1 className="text-4xl font-bold mb-2">⚛️ React + DaisyUI</h1>
          <p className="text-lg text-gray-600">Uma SPA simples e didática para aprender React</p>
        </header>

        {/* Grid de exemplos */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
          <ContadorExemplo />
          <FormularioExemplo />
          <CondicionalExemplo />
          
          {/* Exemplo de props com múltiplos usos */}
          <Card
            titulo="🛍️ Props - Produtos"
            conteudo={
              <div className="grid grid-cols-2 gap-3">
                <CartaoProduto emoji="☕" nome="Café" preco="5.00" />
                <CartaoProduto emoji="🥐" nome="Pão" preco="3.00" />
              </div>
            }
          />
        </div>

        {/* Lista em tela cheia */}
        <ListaExemplo />

        {/* Footer */}
        <footer className="text-center mt-8 text-gray-500">
          <p>Conceitos aprendidos: useState, map(), Props, Eventos, Condicional</p>
        </footer>
      </div>
    </div>
  )
}
