"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import {
  clearTokens,
  getPerfil,
  readTokens,
  refreshAccessToken,
  saveTokens,
} from "@/lib/auth-client";

export default function PerfilPage() {
  const [perfil, setPerfil] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadPerfil() {
      try {
        setLoading(true);
        setError("");

        const { access, refresh } = readTokens();
        if (!access) {
          setError("Você precisa fazer login para acessar o perfil.");
          return;
        }

        try {
          const data = await getPerfil(access);
          setPerfil(data);
          return;
        } catch {
          if (!refresh) {
            throw new Error("Sessão expirada. Faça login novamente.");
          }
        }

        const refreshed = await refreshAccessToken(refresh);
        saveTokens({ access: refreshed.access, refresh });
        const data = await getPerfil(refreshed.access);
        setPerfil(data);
      } catch (err) {
        clearTokens();
        setError(err instanceof Error ? err.message : "Erro ao carregar perfil");
      } finally {
        setLoading(false);
      }
    }

    loadPerfil();
  }, []);

  if (loading) {
    return (
      <div className="flex items-center gap-3">
        <span className="loading loading-spinner loading-md" />
        <p className="text-sm">Carregando perfil...</p>
      </div>
    );
  }

  if (error) {
    return (
      <section className="mx-auto max-w-xl">
        <div className="alert alert-error text-sm">{error}</div>
        <div className="mt-4 flex gap-2">
          <Link href="/auth/login" className="btn btn-primary btn-sm">Ir para login</Link>
          <Link href="/auth/cadastro" className="btn btn-outline btn-sm">Criar conta</Link>
        </div>
      </section>
    );
  }

  return (
    <section className="mx-auto w-full max-w-2xl">
      <div className="card border border-base-300 bg-base-100 shadow-sm">
        <div className="card-body space-y-3">
          <h1 className="card-title text-2xl">Meu perfil</h1>

          <div className="stats stats-vertical border border-base-300 bg-base-200 sm:stats-horizontal">
            <div className="stat">
              <div className="stat-title">Nome</div>
              <div className="stat-value text-lg">
                {perfil?.user?.first_name || "-"} {perfil?.user?.last_name || ""}
              </div>
            </div>
            <div className="stat">
              <div className="stat-title">E-mail</div>
              <div className="stat-value text-lg break-all">{perfil?.user?.email || "-"}</div>
            </div>
          </div>

          <div className="grid gap-2 text-sm sm:grid-cols-2">
            <p><strong>Telefone:</strong> {perfil?.telefone || "Não informado"}</p>
            <p><strong>CPF:</strong> {perfil?.cpf || "Não informado"}</p>
            <p><strong>Data de nascimento:</strong> {perfil?.data_nascimento || "Não informada"}</p>
            <p><strong>ID do perfil:</strong> {perfil?.id || "-"}</p>
          </div>

          <div className="card-actions justify-end">
            <button
              type="button"
              className="btn btn-outline btn-sm"
              onClick={() => {
                clearTokens();
                window.location.href = "/auth/login";
              }}
            >
              Sair
            </button>
          </div>
        </div>
      </div>
    </section>
  );
}
