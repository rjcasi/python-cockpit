import React, { useState } from "react";

const GraphArena = () => {
  const [visited, setVisited] = useState([]);

  const graph = {
    A: ["B", "C"],
    B: ["D", "E"],
    C: ["F"],
    D: [],
    E: ["F"],
    F: []
  };

  const bfs = (start) => {
    let queue = [start];
    let seen = [];
    while (queue.length > 0) {
      let node = queue.shift();
      if (!seen.includes(node)) {
        seen.push(node);
        queue.push(...graph[node]);
      }
    }
    setVisited(seen);
  };

  return (
    <div>
      <h2>Graph Arena (BFS)</h2>
      <button onClick={() => bfs("A")}>Run BFS from A</button>
      <p>Visited Order: {visited.join(" → ")}</p>
    </div>
  );
};

export default GraphArena;