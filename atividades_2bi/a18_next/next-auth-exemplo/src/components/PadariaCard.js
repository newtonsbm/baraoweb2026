import Link from "next/link";

export default function PadariaCard({ item }) {
  return (
    <article className="card bg-base-100 border border-base-300 shadow-sm">
      {item.image_url ? (
        <figure>
          <img src={item.image_url} alt={item.nome} className="h-40 w-full object-cover" />
        </figure>
      ) : null}
      <div className="card-body">
        <h3 className="card-title text-lg">{item.nome}</h3>
        <p className="text-sm text-base-content/70">{item.descricao}</p>
        <p className="text-sm">Telefone: {item.telefone || "Não informado"}</p>
        <div className="card-actions justify-end">
          <Link href={`/padaria/${item.id}`} className="btn btn-primary btn-sm">
            Ver detalhe
          </Link>
        </div>
      </div>
    </article>
  );
}
