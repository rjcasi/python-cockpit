import { useEffect, useState } from "react";
import { getAgent, getGenome } from "./api";

export default function AgentDetail({ agentId, onBack, onViewGenome }) {
  const [agent, setAgent] = useState(null);
  const [genome, setGenome] = useState(null);

  useEffect(() => {
    getAgent(agentId).then(setAgent);
    getGenome(agentId).then(setGenome);
  }, [agentId]);

  if (!agent) return <p>Loading agent…</p>;

  return (
    <div style={{ padding: 20 }}>
      <button onClick={onBack} style={{ marginBottom: "20px" }}>
        Back
      </button>

      <h2>Agent {agentId}</h2>

      <p><strong>Fitness:</strong> {agent.fitness}</p>
      <p><strong>Genome Length:</strong> {agent.genome_length}</p>

      <button onClick={onViewGenome} style={{ marginTop: "10px" }}>
        View Genome
      </button>

      {genome && (
        <>
          <h3>Genome (raw)</h3>
          <pre style={{ background: "#f0f0f0", padding: "10px" }}>
{JSON.stringify(genome, null, 2)}
          </pre>
        </>
      )}
    </div>
  );
}
