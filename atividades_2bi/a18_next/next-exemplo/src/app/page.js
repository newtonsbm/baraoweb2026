"use client";

import Link from "next/link";

export default function Home() {
  return (
    <section className="space-y-8">
      <header className="space-y-3">
        <h2 className="text-3xl font-bold">Aula: Next.js SPA com CSR</h2>
        <p className="max-w-3xl text-base-content/80">
          Este projeto demonstra arquitetura com App Router, componentes reutilizáveis,
          rotas aninhadas e integração com backend Django usando <strong>fetch no cliente</strong>.
        </p>
      </header>

      <div className="grid gap-4 md:grid-cols-2">
        <article className="card bg-base-100 shadow-sm border border-base-300">
          <div className="card-body">
          <h3 className="font-semibold">1) Arquitetura</h3>
          <p className="text-sm text-base-content/70">
            Estrutura por responsabilidades: <code>app/</code> e <code>components/</code>,
            com fetch direto nas páginas para ficar didático.
          </p>
          </div>
        </article>
        <article className="card bg-base-100 shadow-sm border border-base-300">
          <div className="card-body">
          <h3 className="font-semibold">2) Rotas</h3>
          <p className="text-sm text-base-content/70">
            Rotas com App Router: listagem em <code>/padaria</code> e detalhe em
            <code> /padaria/[id]</code>.
          </p>
          </div>
        </article>
        <article className="card bg-base-100 shadow-sm border border-base-300">
          <div className="card-body">
          <h3 className="font-semibold">3) Fetch da API</h3>
          <p className="text-sm text-base-content/70">
            Chamadas diretas ao endpoint <code>/padarias</code> com <code>fetch</code> dentro do componente.
          </p>
          </div>
        </article>
        <article className="card bg-base-100 shadow-sm border border-base-300">
          <div className="card-body">
          <h3 className="font-semibold">4) CSR</h3>
          <p className="text-sm text-base-content/70">
            Páginas interativas com <code>"use client"</code>, <code>useEffect</code> e
            <code> useState</code>.
          </p>
          </div>
        </article>
      </div>

      <div className="flex flex-wrap gap-3">
        <Link href="/padaria" className="btn btn-primary btn-sm sm:btn-md">
          Abrir listagem da padaria
        </Link>
        <a
          href="https://nextjs.org/docs/app/getting-started"
          target="_blank"
          rel="noreferrer"
          className="btn btn-outline btn-sm sm:btn-md"
        >
          Docs oficiais (App Router)
        </a>
      </div>

      <p className="text-xs text-base-content/60">
        Configure <code>NEXT_PUBLIC_PADARIAS_URL</code> se sua API Django estiver em URL diferente de <code>http://localhost:8000/api/padarias/</code>.
      </p>
    </section>
  );
}
