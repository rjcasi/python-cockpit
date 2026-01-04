import { useState } from "react";

export default function PopulationTable({ agents, onSelectAgent }) {
  const [sortKey, setSortKey] = useState("fitness");
  const [sortDir, setSortDir] = useState("desc");

  const sortedAgents = [...agents].sort((a, b) => {
    const valA = a[sortKey];
    const valB = b[sortKey];

    if (valA < valB) return sortDir === "asc" ? -1 : 1;
    if (valA > valB) return sortDir === "asc" ? 1 : -1;
    return 0;
  });

  function toggleSort(key) {
    if (sortKey === key) {
      setSortDir(sortDir === "asc" ? "desc" : "asc");
    } else {
      setSortKey(key);
      setSortDir("asc");
    }
  }

  return (
    <div style={{ marginTop: 20 }}>
      <h3>Population Table</h3>

      <table
        style={{
          width: "100%",
          borderCollapse: "collapse",
          marginTop: "10px"
        }}
      >
        <thead>
          <tr>
            <th
              style={headerStyle}
              onClick={() => toggleSort("id")}
            >
              Agent ID {sortKey === "id" ? arrow(sortDir) : ""}
            </th>

            <th
              style={headerStyle}
              onClick={() => toggleSort("fitness")}
            >
              Fitness {sortKey === "fitness" ? arrow(sortDir) : ""}
            </th>

            <th
              style={headerStyle}
              onClick={() => toggleSort("genome_length")}
            >
              Genome Length {sortKey === "genome_length" ? arrow(sortDir) : ""}
            </th>
          </tr>
        </thead>

        <tbody>
          {sortedAgents.map(agent => (
            <tr
              key={agent.id}
              style={{ cursor: "pointer" }}
              onClick={() => onSelectAgent(agent.id)}
            >
              <td style={cellStyle}>{agent.id}</td>
              <td style={cellStyle}>{agent.fitness}</td>
              <td style={cellStyle}>{agent.genome_length}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

const headerStyle = {
  cursor: "pointer",
  padding: "8px",
  borderBottom: "2px solid #ccc",
  textAlign: "left",
  background: "#f0f0f0"
};

const cellStyle = {
  padding: "8px",
  borderBottom: "1px solid #ddd"
};

function arrow(dir) {
  return dir === "asc" ? "▲" : "▼";
}
