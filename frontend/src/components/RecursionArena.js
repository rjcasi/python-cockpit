import React, { useState } from "react";
import { fib } from "../algorithms/recursion";

export default function RecursionArena() {
  const [n, setN] = useState(10);
  const [result, setResult] = useState(null);

  function runFib() {
    setResult(fib(n));
  }

  return (
    <div>
      <h2>Recursion Arena</h2>
      <input
        type="number"
        value={n}
        onChange={(e) => setN(Number(e.target.value))}
      />
      <button onClick={runFib}>Compute fib(n)</button>
      {result !== null && <p>fib({n}) = {result}</p>}
    </div>
  );
}