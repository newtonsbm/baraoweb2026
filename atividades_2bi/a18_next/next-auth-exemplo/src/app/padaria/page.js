"use client";

import { useEffect, useState } from "react";
import PadariaCard from "@/components/PadariaCard";
import StatusBox from "@/components/StatusBox";

const PADARIAS_URL = process.env.NEXT_PUBLIC_PADARIAS_URL || "http://localhost:8000/api/padarias/";

export default function PadariaPage() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function load() {
      try {
        setLoading(true);
        setError("");

        const response = await fetch(PADARIAS_URL);

        if (!response.ok) {
          throw new Error(`Erro ${response.status} ao buscar dados`);
        }

        const data = await response.json();
        setItems(Array.isArray(data) ? data : []);
      } catch (err) {
        setError(err instanceof Error ? err.message : "Erro ao carregar padaria");
      } finally {
        setLoading(false);
      }
    }

    load();
  }, []);

  if (loading) {
    return (
      <div className="flex items-center gap-3">
        <span className="loading loading-spinner loading-md" />
        <StatusBox message="Carregando itens da padaria..." />
      </div>
    );
  }

  if (error) {
    return <StatusBox type="error" message={error} />;
  }

  if (!items.length) {
    return <StatusBox message="Nenhum item encontrado na API." />;
  }

  return (
    <div className="grid gap-5 sm:grid-cols-2">
      {items.map((item) => (
        <PadariaCard key={item.id} item={item} />
      ))}
    </div>
  );
}
