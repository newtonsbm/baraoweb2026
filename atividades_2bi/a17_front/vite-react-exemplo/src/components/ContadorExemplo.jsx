import { useState } from 'react'
import Card from './Card'

// Exemplo: useState - Contador
export default function ContadorExemplo() {
  const [contador, setContador] = useState(0)

  return (
    <Card
      titulo="📊 useState - Contador"
      conteudo={
        <div className="space-y-4">
          <p className="text-2xl font-bold text-primary">{contador}</p>
          <div className="flex gap-2">
            <button
              className="btn btn-sm btn-primary"
              onClick={() => setContador(contador + 1)}
            >
              ➕ Incrementar
            </button>
            <button
              className="btn btn-sm btn-error"
              onClick={() => setContador(0)}
            >
              🔄 Resetar
            </button>
          </div>
          <p className="text-sm text-gray-500">
            Clique nos botões para mudar o estado (contador)
          </p>
        </div>
      }
    />
  )
}
