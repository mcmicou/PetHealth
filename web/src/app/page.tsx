"use client";

import { useEffect, useState } from "react";

import Image from "next/image";

export default function Home() {
  const [apiResponse, setApiResponse] = useState<string>("Loading...");

  useEffect(() => {
    fetch("http://localhost:8000/health")
      .then((res) => res.json())
      .then((data) => setApiResponse(JSON.stringify(data)))
      .catch((err) => setApiResponse("Error: " + err.message));
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>PetHealth Frontend</h1>
      <p>Backend says: {apiResponse}</p>
    </div>
  );
}
