import { useEffect, useState } from "react";

export default function RunList({ onSelectRun }) {
  const [runs, setRuns] = useState([]);

  useEffect(() => {
    fetch("/api/evolution/runs")
      .then(res => res.json())
      .then(setRuns)
      .catch(err => console.error("Failed to load runs:", err));
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h2>Evolution Runs</h2>

      {runs.length === 0 && <p>No runs found.</p>}

      <ul>
        {runs.map(run => (
          <li
            key={run.id}
            style={{ cursor: "pointer", marginBottom: "8px" }}
            onClick={() => onSelectRun(run.id)}
          >
            <strong>Run {run.id}</strong> — {run.description}
          </li>
        ))}
      </ul>
    </div>
  );
}
