// Exemplo: Props - Cartão de produto
export default function CartaoProduto({ nome, preco, emoji }) {
  return (
    <div className="card bg-base-100 border border-base-300">
      <div className="card-body items-center text-center">
        <div className="text-4xl">{emoji}</div>
        <h3 className="card-title">{nome}</h3>
        <p className="text-2xl font-bold text-primary">R$ {preco}</p>
        <button className="btn btn-sm btn-primary">
          🛒 Adicionar
        </button>
      </div>
    </div>
  )
}
