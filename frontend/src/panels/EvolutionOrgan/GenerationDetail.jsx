import { useEffect, useState } from "react";
import { getGeneration } from "./api";
import PopulationTable from "./PopulationTable";

export default function GenerationDetail({ runId, genIndex, onBack, onSelectAgent }) {
  const [generation, setGeneration] = useState(null);

  useEffect(() => {
    getGeneration(runId, genIndex).then(setGeneration);
  }, [runId, genIndex]);

  if (!generation) return <p>Loading generation…</p>;

  return (
    <div style={{ padding: 20 }}>
      <button onClick={onBack} style={{ marginBottom: "20px" }}>
        Back
      </button>

      <h2>Generation {genIndex}</h2>

      <p><strong>Best Fitness:</strong> {generation.best_fitness}</p>
      <p><strong>Average Fitness:</strong> {generation.avg_fitness}</p>

      <PopulationTable
        agents={generation.agents}
        onSelectAgent={onSelectAgent}
      />
    </div>
  );
}
