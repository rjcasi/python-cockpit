import { useEffect, useState } from "react";
import { getGenome } from "./api";

export default function GenomeGraph({ agentId, onBack }) {
  const [genome, setGenome] = useState(null);

  useEffect(() => {
    getGenome(agentId)
      .then(setGenome)
      .catch(err => console.error("Failed to load genome:", err));
  }, [agentId]);

  if (!genome) return <p>Loading genome…</p>;

  return (
    <div style={{ padding: 20 }}>
      <button onClick={onBack} style={{ marginBottom: "20px" }}>
        Back
      </button>

      <h2>Genome Visualization</h2>
      <p><strong>Agent:</strong> {agentId}</p>

      <div
        style={{
          marginTop: "20px",
          padding: "15px",
          background: "#f7f7f7",
          borderRadius: "8px",
          border: "1px solid #ddd",
          fontFamily: "monospace",
          overflowX: "auto"
        }}
      >
        {Array.isArray(genome) ? (
          <div style={{ display: "flex", gap: "6px", flexWrap: "wrap" }}>
            {genome.map((gene, i) => (
              <div
                key={i}
                style={{
                  padding: "6px 10px",
                  background: "#e0eaff",
                  borderRadius: "4px",
                  border: "1px solid #aac4ff"
                }}
              >
                {gene}
              </div>
            ))}
          </div>
        ) : (
          <pre>{JSON.stringify(genome, null, 2)}</pre>
        )}
      </div>
    </div>
  );
}
