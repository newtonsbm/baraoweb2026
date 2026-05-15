export default function PadariaLayout({ children }) {
  return (
    <section>
      <h2 className="text-2xl font-bold">Lista de Padaria</h2>
      <div className="divider my-4" />
      {children}
    </section>
  );
}
