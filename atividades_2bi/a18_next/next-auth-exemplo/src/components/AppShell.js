import Link from "next/link";

export default function AppShell({ children }) {
  return (
    <div className="min-h-screen">
      <header className="border-b border-base-300 bg-base-100">
        <nav className="navbar mx-auto w-full max-w-5xl px-4 sm:px-6">
          <div className="flex-1">
            <span className="text-lg font-bold">Exemplo Next.js</span>
          </div>
          <div className="flex-none gap-2">
            <Link href="/" className="btn btn-ghost btn-sm">Início</Link>
            <Link href="/padaria" className="btn btn-ghost btn-sm">Padaria</Link>
            <Link href="/auth/cadastro" className="btn btn-ghost btn-sm">Cadastro</Link>
            <Link href="/auth/login" className="btn btn-ghost btn-sm">Login</Link>
            <Link href="/perfil" className="btn btn-ghost btn-sm">Perfil</Link>
          </div>
        </nav>
      </header>

      <main className="mx-auto w-full max-w-5xl px-4 py-8 sm:px-6">{children}</main>
    </div>
  );
}
