// Componente genérico que envolve o conteúdo
export default function Card({ titulo, conteudo }) {
  return (
    <div className="card bg-base-200 rounded-lg p-6 shadow-md">
      <h2 className="card-title text-lg font-bold mb-4">{titulo}</h2>
      <div className="card-body p-0">
        {conteudo}
      </div>
    </div>
  )
}
