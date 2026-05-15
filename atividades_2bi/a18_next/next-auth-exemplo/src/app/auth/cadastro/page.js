"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { registerUser } from "@/lib/auth-client";

const initialForm = {
  first_name: "",
  last_name: "",
  email: "",
  password: "",
  confirmPassword: "",
};

export default function CadastroPage() {
  const router = useRouter();
  const [form, setForm] = useState(initialForm);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  function onChange(event) {
    const { name, value } = event.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  }

  async function onSubmit(event) {
    event.preventDefault();
    setError("");
    setSuccess("");

    if (form.password !== form.confirmPassword) {
      setError("As senhas não conferem.");
      return;
    }

    try {
      setLoading(true);
      await registerUser({
        email: form.email,
        password: form.password,
        first_name: form.first_name,
        last_name: form.last_name,
      });

      setSuccess("Cadastro realizado com sucesso. Redirecionando para login...");
      setTimeout(() => {
        router.push("/auth/login");
      }, 1000);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Erro ao cadastrar usuário");
    } finally {
      setLoading(false);
    }
  }

  return (
    <section className="mx-auto w-full max-w-lg">
      <div className="card border border-base-300 bg-base-100 shadow-sm">
        <div className="card-body">
          <h1 className="card-title text-2xl">Cadastro de usuário</h1>
          <p className="text-sm text-base-content/70">
            Crie sua conta para acessar o perfil via JWT.
          </p>

          <form className="mt-3 space-y-3" onSubmit={onSubmit}>
            <label className="form-control w-full">
              <span className="label-text">Nome</span>
              <input
                type="text"
                name="first_name"
                value={form.first_name}
                onChange={onChange}
                className="input input-bordered w-full"
              />
            </label>

            <label className="form-control w-full">
              <span className="label-text">Sobrenome</span>
              <input
                type="text"
                name="last_name"
                value={form.last_name}
                onChange={onChange}
                className="input input-bordered w-full"
              />
            </label>

            <label className="form-control w-full">
              <span className="label-text">E-mail</span>
              <input
                type="email"
                name="email"
                value={form.email}
                onChange={onChange}
                className="input input-bordered w-full"
                required
              />
            </label>

            <label className="form-control w-full">
              <span className="label-text">Senha</span>
              <input
                type="password"
                name="password"
                value={form.password}
                onChange={onChange}
                className="input input-bordered w-full"
                required
              />
            </label>

            <label className="form-control w-full">
              <span className="label-text">Confirmar senha</span>
              <input
                type="password"
                name="confirmPassword"
                value={form.confirmPassword}
                onChange={onChange}
                className="input input-bordered w-full"
                required
              />
            </label>

            {error ? <div className="alert alert-error text-sm">{error}</div> : null}
            {success ? <div className="alert alert-success text-sm">{success}</div> : null}

            <button type="submit" className="btn btn-primary w-full" disabled={loading}>
              {loading ? "Cadastrando..." : "Cadastrar"}
            </button>
          </form>

          <p className="mt-2 text-sm">
            Já tem conta? <Link href="/auth/login" className="link link-primary">Faça login</Link>
          </p>
        </div>
      </div>
    </section>
  );
}
