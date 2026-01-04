import { useEffect, useState } from "react";
import { getGenerations } from "./api";

export default function GenerationTimeline({ runId, onSelectGeneration }) {
  const [generations, setGenerations] = useState([]);

  useEffect(() => {
    getGenerations(runId)
      .then(setGenerations)
      .catch(err => console.error("Failed to load generations:", err));
  }, [runId]);

  return (
    <div style={{ marginTop: 20 }}>
      <h3>Generation Timeline</h3>

      {generations.length === 0 && <p>No generations found.</p>}

      <ul>
        {generations.map(gen => (
          <li
            key={gen.id}
            style={{ cursor: "pointer", marginBottom: "6px" }}
            onClick={() => onSelectGeneration(gen.generation_index)}
          >
            Generation {gen.generation_index} — Best fitness {gen.best_fitness}
          </li>
        ))}
      </ul>
    </div>
  );
}
