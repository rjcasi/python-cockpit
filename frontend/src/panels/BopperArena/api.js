const API_BASE = "http://localhost:8000/evolution";

export async function fetchRuns() {
  const res = await fetch(`${API_BASE}/runs`);
  if (!res.ok) throw new Error("Failed to fetch runs");
  return res.json();
}

export async function fetchRun(runId) {
  const res = await fetch(`${API_BASE}/runs/${runId}`);
  if (!res.ok) throw new Error("Failed to fetch run");
  return res.json();
}

export async function fetchGenerations(runId) {
  const res = await fetch(`${API_BASE}/runs/${runId}/generations`);
  if (!res.ok) throw new Error("Failed to fetch generations");
  return res.json();
}

export async function fetchAgents(genId) {
  const res = await fetch(`${API_BASE}/generations/${genId}/agents`);
  if (!res.ok) throw new Error("Failed to fetch agents");
  return res.json();
}
