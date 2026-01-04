import { useEffect, useState } from "react";
import { fetchRuns } from "./api";

export default function RunList({ onSelectRun }) {
  const [runs, setRuns] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchRuns()
      .then(data => {
        setRuns(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Error loading runs:", err);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading evolution runs…</p>;
  if (runs.length === 0) return <p>No runs found.</p>;

  return (
    <div style={{ padding: 20 }}>
      <h2>Evolution Runs</h2>
      <ul style={{ listStyle: "none", padding: 0 }}>
        {runs.map(run => (
          <li
            key={run.id}
            onClick={() => onSelectRun(run.id)}
            style={{
              padding: "10px 15px",
              marginBottom: 10,
              border: "1px solid #ccc",
              borderRadius: 6,
              cursor: "pointer",
              background: "#fafafa"
            }}
          >
            <strong>Run {run.id}</strong> — {run.description || "No description"}
          </li>
        ))}
      </ul>
    </div>
  );
}
