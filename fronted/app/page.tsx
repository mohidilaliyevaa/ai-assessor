"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [status, setStatus] = useState("Tekshirilmoqda...");

  useEffect(() => {
    fetch("http://localhost:8000/health")
      .then((res) => res.json())
      .then((data) => setStatus(`Backend: ${data.status}`))
      .catch(() => setStatus("Backend bilan aloqa yo'q"));
  }, []);

  return (
    <main className="flex min-h-screen flex-col items-center justify-center gap-4">
      <h1 className="text-4xl font-bold">AI-Assessor</h1>
      <p className="text-lg">{status}</p>
    </main>
  );
}