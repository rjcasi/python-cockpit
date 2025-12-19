import React, { useState } from "react";
import { fibDP } from "../algorithms/dp";

export default function DPArena() {
  const [n, setN] = useState(20);
  const [result, setResult] = useState(null);

  function runDP() {
    setResult(fibDP(n));
  }

  return (
    <div>
      <h2>Dynamic Programming Arena</h2>
      <input
        type="number"
        value={n}
        onChange={(e) => setN(Number(e.target.value))}
      />
      <button onClick={runDP}>Compute fibDP(n)</button>
      {result !== null && <p>fibDP({n}) = {result}</p>}
    </div>
  );
}