export default function StatusBox({ type = "info", message }) {
  const base = "alert text-sm";

  const styles = {
    info: "alert-info",
    error: "alert-error",
  };

  return <p className={`${base} ${styles[type] || styles.info}`}>{message}</p>;
}
