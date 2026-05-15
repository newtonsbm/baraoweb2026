"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { loginUser, saveTokens } from "@/lib/auth-client";

export default function LoginPage() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function onSubmit(event) {
    event.preventDefault();
    setError("");

    try {
      setLoading(true);
      const tokens = await loginUser({ email, password });
      saveTokens(tokens);
      router.push("/perfil");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Erro ao realizar login");
    } finally {
      setLoading(false);
    }
  }

  return (
    <section className="mx-auto w-full max-w-lg">
      <div className="card border border-base-300 bg-base-100 shadow-sm">
        <div className="card-body">
          <h1 className="card-title text-2xl">Login</h1>
          <p className="text-sm text-base-content/70">
            Use seu e-mail e senha para obter o token JWT.
          </p>

          <form className="mt-3 space-y-3" onSubmit={onSubmit}>
            <label className="form-control w-full">
              <span className="label-text">E-mail</span>
              <input
                type="email"
                value={email}
                onChange={(event) => setEmail(event.target.value)}
                className="input input-bordered w-full"
                required
              />
            </label>

            <label className="form-control w-full">
              <span className="label-text">Senha</span>
              <input
                type="password"
                value={password}
                onChange={(event) => setPassword(event.target.value)}
                className="input input-bordered w-full"
                required
              />
            </label>

            {error ? <div className="alert alert-error text-sm">{error}</div> : null}

            <button type="submit" className="btn btn-primary w-full" disabled={loading}>
              {loading ? "Entrando..." : "Entrar"}
            </button>
          </form>

          <p className="mt-2 text-sm">
            Ainda não tem conta? <Link href="/auth/cadastro" className="link link-primary">Cadastre-se</Link>
          </p>
        </div>
      </div>
    </section>
  );
}
