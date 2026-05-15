"use client";

import Link from "next/link";
import { useParams } from "next/navigation";
import { useEffect, useState } from "react";
import StatusBox from "@/components/StatusBox";

const PADARIAS_URL = process.env.NEXT_PUBLIC_PADARIAS_URL || "http://localhost:8000/api/padarias/";

export default function PadariaDetailPage() {
  const params = useParams();
  const [item, setItem] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    if (!params?.id) return;

    async function load() {
      try {
        setLoading(true);
        setError("");

        const response = await fetch(`${PADARIAS_URL}${params.id}/`);

        if (!response.ok) {
          throw new Error(`Erro ${response.status} ao buscar detalhe`);
        }

        const data = await response.json();
  setItem(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : "Erro ao carregar detalhe");
      } finally {
        setLoading(false);
      }
    }

    load();
  }, [params?.id]);

  if (loading) {
    return (
      <div className="flex items-center gap-3">
        <span className="loading loading-spinner loading-md" />
        <StatusBox message="Carregando detalhe do item..." />
      </div>
    );
  }

  if (error) {
    return <StatusBox type="error" message={error} />;
  }

  if (!item) {
    return <StatusBox message="Item não encontrado." />;
  }

  return (
    <article className="card bg-base-100 border border-base-300 shadow-sm">
      {item.image_url ? (
        <figure>
          <img src={item.image_url} alt={item.nome} className="h-56 w-full object-cover" />
        </figure>
      ) : null}
      <div className="card-body">
        <h3 className="card-title text-2xl">{item.nome}</h3>
        <p className="text-base-content/80">{item.descricao}</p>

        <div className="space-y-1 text-sm">
          <p><strong>Telefone:</strong> {item.telefone || "Não informado"}</p>
          <p><strong>E-mail:</strong> {item.email || "Não informado"}</p>
        </div>

        {item.endereco ? (
          <div className="alert alert-info mt-2">
            <div>
              <p className="font-semibold">Endereço</p>
              <p>
                {item.endereco.rua}, {item.endereco.numero}
                {item.endereco.complemento ? ` - ${item.endereco.complemento}` : ""}
              </p>
              <p>
                {item.endereco.bairro} - {item.endereco.cidade}/{item.endereco.estado}
              </p>
              <p>CEP: {item.endereco.cep}</p>
            </div>
          </div>
        ) : null}

        <p className="text-sm text-base-content/70">
          <strong>Cestas vinculadas:</strong> {Array.isArray(item.cestas) ? item.cestas.length : 0}
        </p>

        <div className="card-actions justify-end">
          <Link href="/padaria" className="btn btn-outline btn-sm">
            ← Voltar para listagem
          </Link>
        </div>
      </div>
    </article>
  );
}
