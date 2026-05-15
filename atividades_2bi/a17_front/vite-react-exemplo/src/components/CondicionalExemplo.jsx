import { useState } from 'react'
import Card from './Card'

// Exemplo: Condicional
export default function CondicionalExemplo() {
  const [logado, setLogado] = useState(false)

  return (
    <Card
      titulo="❓ Renderização Condicional"
      conteudo={
        <div className="space-y-4">
          <button
            className={`btn w-full ${logado ? 'btn-error' : 'btn-success'}`}
            onClick={() => setLogado(!logado)}
          >
            {logado ? '🔓 Logout' : '🔐 Login'}
          </button>

          {logado ? (
            <div className="alert alert-success">
              <span>✅ Bem-vindo! Você está logado</span>
            </div>
          ) : (
            <div className="alert alert-warning">
              <span>⚠️ Você não está logado</span>
            </div>
          )}
        </div>
      }
    />
  )
}
