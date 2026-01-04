import { useEffect, useState } from "react";

export default function RunList() {
  const [runs, setRuns] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:8000/evolution/runs")
      .then((res) => res.json())
      .then((data) => {
        setRuns(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching runs:", err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading evolution runs...</p>;
  }

  return (
    <div>
      <h2>Evolution Runs</h2>
      {runs.length === 0 && <p>No runs found.</p>}

      <ul>
        {runs.map((run) => (
          <li key={run.id}>
            <strong>{run.name}</strong> — {run.status}
          </li>
        ))}
      </ul>
    </div>
  );
}
