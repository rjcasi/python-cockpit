import React, { useEffect, useState } from "react";
import "./Dashboard.css";
import { renderGraphArena } from "./grapharena.js";
import { renderSortingArena } from "./sortingarenas.js";
import { renderCausalSetArena } from "./causalsetarena.js";
import { renderDSAArena } from "./dsaarena.js";
import { renderMLArena } from "./mlarena.js";   // <-- new



// --- Sorting Arena ---
function SortingArena() {
  const canvasRef = React.useRef(null);
  const [data] = useState([50, 20, 80, 10, 60, 30, 90, 40]);

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    const x = d3.scaleBand().domain(d3.range(data.length)).range([0, 600]).padding(0.1);
    const y = d3.scaleLinear().domain([0, d3.max(data)]).range([300, 0]);

    function draw(arr, highlight = []) {
      ctx.clearRect(0, 0, 600, 300);
      arr.forEach((d, i) => {
        ctx.fillStyle = highlight.includes(i) ? "orange" : "steelblue";
        ctx.fillRect(x(i), y(d), x.bandwidth(), 300 - y(d));
      });
    }

    async function bubbleSort(arr) {
      let a = [...arr];
      for (let i = 0; i < a.length; i++) {
        for (let j = 0; j < a.length - i - 1; j++) {
          draw(a, [j, j + 1]);
          await new Promise(r => setTimeout(r, 400));
          if (a[j] > a[j + 1]) [a[j], a[j + 1]] = [a[j + 1], a[j]];
        }
      }
      draw(a);
    }

    async function quickSort(arr, left = 0, right = arr.length - 1) {
      if (left >= right) return;
      let pivot = arr[right], i = left;
      for (let j = left; j < right; j++) {
        draw(arr, [j, right]);
        await new Promise(r => setTimeout(r, 400));
        if (arr[j] < pivot) {
          [arr[i], arr[j]] = [arr[j], arr[i]];
          i++;
        }
      }
      [arr[i], arr[right]] = [arr[right], arr[i]];
      await quickSort(arr, left, i - 1);
      await quickSort(arr, i + 1, right);
      draw(arr);
    }

    async function mergeSort(arr, start = 0, end = arr.length) {
      if (end - start <= 1) return arr.slice(start, end);
      const mid = Math.floor((start + end) / 2);
      const left = await mergeSort(arr, start, mid);
      const right = await mergeSort(arr, mid, end);
      const merged = [];
      let i = 0, j = 0;
      while (i < left.length && j < right.length) {
        draw(arr, [start + i, mid + j]);
        await new Promise(r => setTimeout(r, 400));
        if (left[i] < right[j]) merged.push(left[i++]);
        else merged.push(right[j++]);
      }
      merged.push(...left.slice(i), ...right.slice(j));
      for (let k = 0; k < merged.length; k++) arr[start + k] = merged[k];
      draw(arr);
      return merged;
    }

    draw(data);

    document.addEventListener("keydown", e => {
      if (e.key === "b") bubbleSort([...data]);
      if (e.key === "q") quickSort([...data]);
      if (e.key === "m") mergeSort([...data]);
    });
  }, [data]);

  return (
    <div className="panel">
      <h2>Sorting Arena</h2>
      <canvas ref={canvasRef} width={600} height={300}></canvas>
      <p>Press <b>b</b> for Bubble Sort, <b>q</b> for Quick Sort, <b>m</b> for Merge Sort</p>
    </div>
  );
}

// --- Graph Arena ---
function GraphArena() {
  const canvasRef = React.useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");

    const graph = {
      A: ["B", "C"],
      B: ["A", "D", "E"],
      C: ["A", "F"],
      D: ["B"],
      E: ["B", "F"],
      F: ["C", "E"]
    };

    const positions = {
      A: [100, 100],
      B: [200, 50],
      C: [200, 150],
      D: [300, 20],
      E: [300, 80],
      F: [300, 180]
    };

    function drawGraph(highlight = []) {
      ctx.clearRect(0, 0, 600, 400);
      Object.keys(graph).forEach(node => {
        graph[node].forEach(neighbor => {
          const [x1, y1] = positions[node];
          const [x2, y2] = positions[neighbor];
          ctx.strokeStyle = "#999";
          ctx.beginPath();
          ctx.moveTo(x1, y1);
          ctx.lineTo(x2, y2);
          ctx.stroke();
        });
      });
      Object.keys(positions).forEach(node => {
        const [x, y] = positions[node];
        ctx.fillStyle = highlight.includes(node) ? "orange" : "steelblue";
        ctx.beginPath();
        ctx.arc(x, y, 20, 0, 2 * Math.PI);
        ctx.fill();
        ctx.fillStyle = "white";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(node, x, y);
      });
    }

    async function bfs(start) {
      const visited = new Set();
      const queue = [start];
      while (queue.length > 0) {
        const node = queue.shift();
        if (!visited.has(node)) {
          visited.add(node);
          drawGraph([node]);
          await new Promise(r => setTimeout(r, 700));
          graph[node].forEach(neighbor => {
            if (!visited.has(neighbor)) queue.push(neighbor);
          });
        }
      }
    }

    async function dfs(start, visited = new Set()) {
      if (visited.has(start)) return;
      visited.add(start);
      drawGraph([start]);
      await new Promise(r => setTimeout(r, 700));
      for (const neighbor of graph[start]) {
        await dfs(neighbor, visited);
      }
    }

    function loadPanel(panelName) {
  const containerId = "panel-container";
  if (panelName === "GraphArena") {
    renderGraphArena(containerId);
  } else if (panelName === "SortingArena") {
    renderSortingArena(containerId);
  } else if (panelName === "CausalSetArena") {
    renderCausalSetArena(containerId);
  } else if (panelName === "DSAArena") {
    renderDSAArena(containerId);
  } else if (panelName === "MLArena") {
    renderMLArena(containerId);   // <-- new route
  }
}

    drawGraph();

    document.addEventListener("keydown", e => {
      if (e.key === "g") bfs("A");   // BFS
      if (e.key === "h") dfs("A");   // DFS
    });
  }, []);

  return (
    <div className="panel">
      <h2>Graph Arena</h2>
      <canvas ref={canvasRef} width={600} height={400}></canvas>
      <p>Press <b>g</b> for BFS, <b>h</b> for DFS</p>
    </div>
  );
}

// --- Dashboard Layout ---
export default function Dashboard() {
  return (
    <div className="dashboard">
      <SortingArena />
      <GraphArena />
    </div>
  );
}