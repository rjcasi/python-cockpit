import { useEffect, useState } from "react";
import { getRun, getGenerations } from "./api";
import GenerationTimeline from "./GenerationTimeline";

export default function RunDetail({ runId, onBack, onSelectGeneration, onViewTrend }) {
  const [run, setRun] = useState(null);
  const [generations, setGenerations] = useState([]);

  useEffect(() => {
    getRun(runId).then(setRun);
    getGenerations(runId).then(setGenerations);
  }, [runId]);

  if (!run) return <p>Loading run…</p>;

  return (
    <div style={{ padding: 20 }}>
      <button onClick={onBack} style={{ marginBottom: "20px" }}>
        Back
      </button>

      <h2>Run {runId}</h2>

      <p><strong>Description:</strong> {run.description}</p>
      <p><strong>Population Size:</strong> {run.population_size}</p>
      <p><strong>Mutation Rate:</strong> {run.mutation_rate}</p>
      <p><strong>Crossover Rate:</strong> {run.crossover_rate}</p>

      <button onClick={onViewTrend} style={{ marginTop: "10px" }}>
        View Fitness Trend
      </button>

      <GenerationTimeline
        runId={runId}
        onSelectGeneration={onSelectGeneration}
      />
    </div>
  );
}
