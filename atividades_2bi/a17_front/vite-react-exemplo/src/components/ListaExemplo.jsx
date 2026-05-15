import { useState } from 'react'
import Card from './Card'

// Exemplo: Lista com map
export default function ListaExemplo() {
  const [tarefas, setTarefas] = useState([
    { id: 1, titulo: '📚 Aprender React' },
    { id: 2, titulo: '🎨 Usar Tailwind CSS' },
    { id: 3, titulo: '🚀 Criar SPA' },
  ])

  const [novaTarefa, setNovaTarefa] = useState('')

  const adicionarTarefa = () => {
    if (novaTarefa.trim()) {
      setTarefas([
        ...tarefas,
        { id: Date.now(), titulo: novaTarefa }
      ])
      setNovaTarefa('')
    }
  }

  const removerTarefa = (id) => {
    setTarefas(tarefas.filter((t) => t.id !== id))
  }

  return (
    <Card
      titulo="📋 map() - Lista de Tarefas"
      conteudo={
        <div className="space-y-4">
          <div className="flex gap-2">
            <input
              type="text"
              placeholder="Nova tarefa..."
              className="input input-bordered flex-1"
              value={novaTarefa}
              onChange={(e) => setNovaTarefa(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && adicionarTarefa()}
            />
            <button
              className="btn btn-primary"
              onClick={adicionarTarefa}
            >
              ➕
            </button>
          </div>
          <ul className="menu bg-base-100 rounded-box">
            {tarefas.map((tarefa) => (
              <li key={tarefa.id} className="flex justify-between items-center">
                <span>{tarefa.titulo}</span>
                <button
                  className="btn btn-xs btn-ghost"
                  onClick={() => removerTarefa(tarefa.id)}
                >
                  ✕
                </button>
              </li>
            ))}
          </ul>
          <p className="text-sm text-gray-500">
            Total: {tarefas.length} tarefa(s)
          </p>
        </div>
      }
    />
  )
}
