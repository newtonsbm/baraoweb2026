import { useState } from 'react'
import Card from './Card'

// Exemplo: Formulário com onChange
export default function FormularioExemplo() {
  const [nome, setNome] = useState('')
  const [email, setEmail] = useState('')

  return (
    <Card
      titulo="📝 Eventos - Formulário"
      conteudo={
        <form className="space-y-4">
          <div>
            <input
              type="text"
              placeholder="Digite seu nome"
              className="input input-bordered w-full"
              value={nome}
              onChange={(e) => setNome(e.target.value)}
            />
          </div>
          <div>
            <input
              type="email"
              placeholder="Digite seu email"
              className="input input-bordered w-full"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div className="alert alert-info">
            <span>
              👤 Nome: <strong>{nome || '(vazio)'}</strong>
            </span>
          </div>
          <div className="alert alert-info">
            <span>
              📧 Email: <strong>{email || '(vazio)'}</strong>
            </span>
          </div>
        </form>
      }
    />
  )
}
