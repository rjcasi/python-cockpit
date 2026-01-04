import { useEffect, useState } from "react";
import { getFitnessHistory } from "./api";

export default function TelemetryTrend({ runId, onBack }) {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    getFitnessHistory(runId)
      .then(setHistory)
      .catch(err => console.error("Failed to load fitness history:", err));
  }, [runId]);

  if (!history || history.length === 0) {
    return <p>Loading fitness trend…</p>;
  }

  // Extract values
  const points = history.map((h) => h.best_fitness);
  const max = Math.max(...points);
  const min = Math.min(...points);

  // SVG dimensions
  const width = 600;
  const height = 200;
  const padding = 20;

  // Convert data to SVG coordinates
  const scaleX = (i) =>
    padding + (i / (points.length - 1)) * (width - padding * 2);

  const scaleY = (v) =>
    height - padding - ((v - min) / (max - min)) * (height - padding * 2);

  const pathData = points
    .map((v, i) => `${i === 0 ? "M" : "L"} ${scaleX(i)} ${scaleY(v)}`)
    .join(" ");

  return (
    <div style={{ padding: 20 }}>
      <button onClick={onBack} style={{ marginBottom: "20px" }}>
        Back
      </button>

      <h2>Fitness Trend</h2>
      <p><strong>Run:</strong> {runId}</p>

      <svg width={width} height={height} style={{ border: "1px solid #ccc" }}>
        {/* Line path */}
        <path
          d={pathData}
          fill="none"
          stroke="#0077ff"
          strokeWidth="2"
        />

        {/* Points */}
        {points.map((v, i) => (
          <circle
            key={i}
            cx={scaleX(i)}
            cy={scaleY(v)}
            r="3"
            fill="#0077ff"
          />
        ))}
      </svg>

      <p style={{ marginTop: "10px" }}>
        <strong>Min Fitness:</strong> {min}  
        <br />
        <strong>Max Fitness:</strong> {max}
      </p>
    </div>
  );
}
